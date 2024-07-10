import polars as pl
import streamlit as st
from data_loading import (
    load_snow_coverage,
    load_stops,
    load_traveltimes,
    unique_start_stations,
)
from i18n import LANG, change_language_sel, get_i18n_strings
from pdk_map import display_map

st.set_page_config(
    page_title='Public transport to swiss mountains'
)


def change_start_loc_sel():
    """Update start location query parameter
    """
    st.query_params['start'] = st.session_state['start_loc_sel']


def destinations(
    min_altitude_m: int,
    max_altitude_m: int,
    max_duration_min: float,
    start_location_stn: str,
    min_snow_depth_cm: int = 0
):
    """Load filtered destination list

    Arguments:
        min_altitude_m -- Minimum altitude [m]
        max_altitude_m -- Maximum altitude [m]
        max_duration_min -- Maximum duration [min]

    Returns:
        PL dataframe: list of destinations
    """
    return (
        load_traveltimes()
        .join(load_stops(), left_on='stop_stn', right_on='designationOfficial')
        .join(load_snow_coverage(), on='number')
        .filter(
            pl.col('height') >= min_altitude_m,
            pl.col('height') <= max_altitude_m,
            pl.col('duration_min') <= max_duration_min,
            pl.col('start_stn').eq(start_location_stn),
            pl.col('snow_depth') >= min_snow_depth_cm
        )
    )


texts = get_i18n_strings()

st.title(texts.app_title)
st.text(texts.app_introduction)


language_sel = st.sidebar.selectbox(
    label=f'{texts.menu_language}:',
    options=LANG.keys(),
    index=int(list(LANG.keys()).index(st.query_params['language'])),
    key='language_sel',
    on_change=change_language_sel
)

if 'start' not in st.query_params:
    st.query_params['start'] = unique_start_stations()[0]
start_location = st.sidebar.selectbox(
    label=f'{texts.menu_starting_location}:',
    options=unique_start_stations(),
    index=int(list(unique_start_stations()).index(st.query_params['start'])),
    key='start_loc_sel',
    on_change=change_start_loc_sel
)

min_altitude = st.sidebar.number_input(
    f'{texts.menu_min_altitude} [m]:', 1000, 4000, 1200)
max_altitude = st.sidebar.number_input(
    f'{texts.menu_max_altitude} [m]:', 1000, 4000, 4000)
min_snow_depth = st.sidebar.number_input(
    f'{texts.menu_min_snow_depth} [cm]:', 0, 999, 0)
max_duration = st.sidebar.number_input(
    f'{texts.menu_max_duration} [min]:', 1, 999, 90,
)

data = destinations(
    min_altitude_m=min_altitude,
    max_altitude_m=max_altitude,
    max_duration_min=max_duration,
    start_location_stn=start_location,
    min_snow_depth_cm=min_snow_depth
)

display_map(data, texts)
