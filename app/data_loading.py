import polars as pl
import streamlit as st
from config.config import Config

CH_ISO_COUNTRYCODE = 'CH'


@st.cache_data(ttl=3600)
def load_stops():
    """Load public transport stops list

    Returns:
        PL dataframe: public transport stops
    """
    return (
        pl.read_csv(Config.STOPS_PATH, separator=';')
        .filter(
            pl.col('isoCountryCode').eq(CH_ISO_COUNTRYCODE),
            pl.col('stopPoint').eq(True)
        )
        .select(
            'number',
            'designationOfficial',
            'wgs84East',
            'wgs84North',
            'height'
        )
    )


@st.cache_data(ttl=60)
def unique_start_stations() -> list[str]:
    """Get unique start stations

    Returns:
        List of unique start station names
    """
    return load_traveltimes()['start_stn'].unique().sort()


@st.cache_data(ttl=3600)
def load_traveltimes():
    """Load traveltimes list

    Returns:
        PL dataframe: traveltimes list
    """
    return (
        pl.read_csv(Config.TRAVELTIMES_PATH, separator=';')
        .with_columns(
            pl.col('start_time').cast(pl.Datetime()),
            pl.col('stop_time').cast(pl.Datetime())
        )
        .with_columns(
            duration_min=(
                pl.col('stop_time') - pl.col('start_time')
            ).dt.total_minutes()
        ).with_columns(
            hours=(
                pl.col('duration_min') / 60)
                .cast(pl.Int8)
                .cast(pl.String),
            minutes=(pl.col('duration_min') % 60)
                .cast(pl.Int8)
                .cast(pl.String)
                .str.zfill(2)
        )
    )


@st.cache_data(ttl=3600)
def load_snow_coverage():
    """Load snow coverage data

    Returns:
        Snow coverage for each possible destination
    """
    return (pl.read_csv(Config.SNOW_COVERAGE_PATH, separator=';'))
