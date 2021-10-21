# Ajut.md • [Live](https://www.ajut.md/)

[![GitHub contributors](https://img.shields.io/github/contributors/code4moldova/ajut.md.svg?style=for-the-badge)](https://github.com/code4moldova/ajut.md/graphs/contributors) [![GitHub last commit](https://img.shields.io/github/last-commit/code4moldova/ajut.md.svg?style=for-the-badge)](https://github.com/code4moldova/ajut.md/commits/master) [![License: MPL 2.0](https://img.shields.io/badge/license-MPL%202.0-brightgreen.svg?style=for-the-badge)](https://opensource.org/licenses/MPL-2.0)

![Build status](https://github.com/code4moldova/ajut.md/workflows/ajut-dev/badge.svg)

This project is the result of the 2019 Civic Labs research. You can view the knowledge base of the project on the [Ro Help](https://civiclabs.ro/ro/solutions/aid-management-hub) Civic Labs page. This project is adjusted for the NGO's needs from Republic of Moldova by Code 4 Moldova.

Check out the [prototype](https://www.figma.com/proto/Fm1mdnskOPnJCX1AWgpR3U/Ajut.md_Web-Design_UI?node-id=1%3A2&viewport=-265%2C-331%2C0.12936504185199738&scaling=scale-down-width) and [admin](https://www.figma.com/proto/Fm1mdnskOPnJCX1AWgpR3U/Ajut.md_Web-Design_UI?node-id=169%3A45&viewport=329%2C197%2C0.29047635197639465&scaling=min-zoom) as well!

Ajut.md is a platform meant to help NGOs during an emergency situation. The NGOs can ask for donations, resources or volunteers, and users can browse the needs that various NGOs have. Initially prototyped by Code4Romania with an earthquake in mind, this project was pushed at the forefront of Code4Romania [Tech for Social Good](https://tfsg.code4.ro/ro/) development program during the COVID-19 pandemic.

[See the project live](https://www.ajut.md/)

Objective: Safe and coherent collection of aid.

How: The application displays verified and validated NGOs for the collection and distribution of resources.

Concept developed as part of the Civic Labs program of Code for Romania.

[Contributing](#contributing) | [Built with](#built-with) | [Deployment](#deployment) | [Feedback](#feedback) | [License](#license) | [About Code4MD](#about-code4md)

## Contributing

This project is built by amazing volunteers and you can be one of them! Here's a list of ways in [which you can contribute to this project](.github/CONTRIBUTING.md).

If you want to make any change to this repository, please **make a fork first**.

Help us out by testing this project in the [staging environment](http://dev.ajut.md/). If you see something that doesn't quite work the way you expect it to, open an Issue. Make sure to describe what you _expect to happen_ and _what is actually happening_ in detail.

If you would like to suggest new functionality, open an Issue and mark it as a __[Feature request]__. Please be specific about why you think this functionality will be of use. If you can, please include some visual description of what you would like the UI to look like, if you are suggesting new UI elements. 

## Built With

Django

### Programming languages

Python 3

### Development
Docker is used to run the development version, so you'll need to install [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/).
Once installed, you just need to copy `cp .env.example .env` and run `docker-compose up` and point your browser to http://localhost:8000/,

A seed command is being run on each start, so you can have fresh new random data to play with. 

In case you are using WSL with Docker for Desktop (version 2.2.0.4) on Windows: you need to have your repository on the Windows file system rather than on the WSL one because otherwise the volume won't be mounted (solution inspired from this work around: https://github.com/docker/for-win/issues/2151#issuecomment-402163189)

If you want to make migrations, run tests or add a dependency, you can get into the web container using:
```bash
docker-compose exec web sh
./manage makemigrations
pip install <my cool dependency>
```

We're using black for formatting and each push is checked against it. Running 
```bash
black --line-length 120 --target-version py38
```
before a commit will do the trick.

## Deployment
The deployment process is fully automated using AWS CodeBuild and ECS. Each time a PR is merged on master, a new docker image build is trigger and if it's successful, [the staging environment](http://dev.ajut.md/) will point to your latest changes.

The production environment is closely monitored by [Sentry](https://sentry.io).

## Feedback

* Request a new feature on GitHub.
* Vote for popular feature requests.
* File a bug in GitHub Issues.
* Email us with other feedback contact@code4.md

## License

This project is licensed under the MPL 2.0 License - see the [LICENSE](LICENSE) file for details

## About Code4Md

Started in 2020, Code for Moldova is a civic tech NGO, official member of the Code for All network. We have a community of over 100 volunteers (developers, ux/ui, communications, data scientists, graphic designers, devops, it security and more) who work pro-bono for developing digital solutions to solve social problems. #techforsocialgood. If you want to learn more details about our projects [visit our site](https://www.code4.md/) or if you want to talk to one of our staff members, please e-mail us at contact@code4.md.

Last, but not least, we rely on donations to ensure the infrastructure, logistics and management of our community that is widely spread across 5 timezones, coding for social change to make Moldova and the world a better place. If you want to support us, [you can do it here](https://code4.md/donate/).
