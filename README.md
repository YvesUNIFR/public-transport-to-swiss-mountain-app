# Public transport to Swiss Mountains - Destination Finder

## Goal and vision
**Public transport to Swiss Mountains** is a personal project initiated in 2023 with the aim of promoting the use of public transportation for mountain sports in Switzerland. Its primary objective is to provide information about the most efficient routes via public transportation to reach various altitudes in Switzerland. This project is designed to assist users in discovering new destinations for snow sports or simply finding an enjoyable spots with breathtaking views and fresh air atop Switzerland mountains, all while promoting environmental preservation.

This application is published on [Streamlit Cloud](https://public-transport-to-swiss-mountain.streamlit.app/)

## Data sources
Ths application is based on following data sources:
* GTFS data and public transport stops list from the [Open data platform mobility Switzerland](https://opentransportdata.swiss/)
* Snow coverage data from [Exolabs](https://www.exolabs.ch/)
Many thanks to the data providers.

## Usage
Create `.env` from `.env.example`
```
pip install -r requirements.txt
dotenv run streamlit run app/main.py
```

## Requirements
* Python 3.11
* Schedules generated with the [Travel planner](https://gitlab.com/public-transport-to-swiss-mountains/travel-planner)

## Support
If you're interested into this project, please feel free to contact the [author on Linkedin](https://www.linkedin.com/in/hausermarc/).

## Roadmap
The project is a MVP. After this initial phase, new features could be added, for example:
- API server to allow the integration in third-party systems

## Contributing
Ideas and feedbacks are very appreciated. Feel free to contact the [author on Linkedin](https://www.linkedin.com/in/hausermarc/) to discuss directly the way you would like to contribute to the project. See also the [contribution guidelines](https://gitlab.com/public-transport-to-swiss-mountains/travel-planner/-/blob/main/CONTRIBUTING.md).

## Adding your favorite starting location
Do you want to be able to select your favorite starting location and/or having the guarantee that the schedules are updated on a regular basis?
It is possible if you're ready to contribute financially to the corresponding computing costs. Please contact the author in case of interest.

## Original repository
The original repository is on [Gitlab](https://gitlab.com/public-transport-to-swiss-mountains/destination-finder). The Github repo is a clone allowing a deployment to Streamlit Cloud.

## License
See [license file](https://gitlab.com/public-transport-to-swiss-mountains/travel-planner/-/blob/main/LICENSE?ref_type=heads).
