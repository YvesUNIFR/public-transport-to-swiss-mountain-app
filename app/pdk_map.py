import polars as pl
import pydeck as pdk
import streamlit as st
from i18n import Dictionary


def display_map(destinations: pl.DataFrame, texts: Dictionary):
    """Display destinations map

    Arguments:
        destinations -- List of destinations
    """
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=destinations.to_pandas(),
        pickable=True,
        get_position=['wgs84East', 'wgs84North'],
        radius_min_pixels=5,
        radius_max_pixels=80,
        get_fill_color=[220, 0, 0]
    )
    view_state = pdk.ViewState(latitude=47.0, longitude=7.5, zoom=6)

    chart = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            'text': (
                texts.tooltip_stop + ': {stop_stn}\n'
                + texts.tooltip_altitude + ': {height} m\n'
                + texts.tooltip_duration + ': {hours}:{minutes}'
            )
        }
    )

    st.pydeck_chart(chart, use_container_width=True)
