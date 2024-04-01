import os


class Config:
    """General settings"""
    DATA_CONTAINER_ROOT = os.getenv('DATA_CONTAINER_ROOT')
    STOPS_PATH = DATA_CONTAINER_ROOT + '/stops.csv'
    TRAVELTIMES_PATH = DATA_CONTAINER_ROOT + '/traveltimes.csv'
