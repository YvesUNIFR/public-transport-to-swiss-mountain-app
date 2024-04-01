# Public transport to Swiss Mountains - Destination Finder

## Goal and vision
**Public transport to Swiss Mountains** is a personal project initiated in 2023 with the aim of promoting the use of public transportation for mountain sports in Switzerland. Its primary objective is to provide information about the most efficient routes via public transportation to reach various altitudes in Switzerland. This project is designed to assist users in discovering new destinations for snow sports or simply finding an enjoyable spots with breathtaking views and fresh air atop Switzerland mountains, all while promoting environmental preservation.

## Project status
This project is still in a very early stage (actually proof of concept).

## Travel planner
This respository contains the core functionality of the system. The travel planner's purpose is to calculate the duration between a given starting location and all possible destinations based on specific criteria. The travel planner relies on the [MOTIS Project](https://motis-project.de/). The underlying data utilzied include OpenStreatMaps data provided by [Geofabrik GmbH](https://www.geofabrik.de/) and time tables and public transport stop lists distributed by the [Open data platform mobility Switzerland](https://opentransportdata.swiss/)

## Usage
TBD

## Support
If you're interested into this project, please feel free to contact the [author on Linkedin](https://www.linkedin.com/in/hausermarc/).

## Roadmap
The project is still in a very early stage. Following steps are planned for a MVP:
- Finish travel planner
- Deployment on ephemeral infrastructure for periodical master travel planner list updates
- Deployment of central database
- Frontend for direct user interaction
- API server to allow the integration in third-party systems

After this initial phase, new features could be added, for example:
- Usage of snow height information to enable additional more specific filters
- Adding multiple starting locations to cover the biggest cities of Switzerland
- Map visualization of the possible destinations


## Contributing
Ideas and feedbacks are very appreciated. Feel free to contact the [author on Linkedin](https://www.linkedin.com/in/hausermarc/) to discuss directly the way you would like to contribute to the project. See also the [contribution guidelines](https://gitlab.com/public-transport-to-swiss-mountains/travel-planner/-/blob/main/CONTRIBUTING.md).

## License
See [license file](https://gitlab.com/public-transport-to-swiss-mountains/travel-planner/-/blob/main/LICENSE?ref_type=heads).
