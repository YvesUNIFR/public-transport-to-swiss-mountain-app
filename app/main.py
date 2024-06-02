import polars as pl
import streamlit as st
from data_loading import load_stops, load_traveltimes, load_snow_coverage
from pdk_map import display_map
from i18n import LANG, get_i18n_strings, change_language_sel

st.set_page_config(
    page_title='Public transport to swiss mountains'
)

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
    print(load_traveltimes()['start_stn'].unique())
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
    on_change=change_language_sel)
start_location = st.sidebar.selectbox(
    f'{texts.menu_starting_location}:', ['Bern'])
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
