## Project

 Orange County Lettings Website

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.9+
- Docker and Docker Compose (https://docs.docker.com/get-docker/ or https://docs.docker.com/engine/install/)
- (Docker Desktop - not mandatory, only for convenience)
- Sentry account with access rights on the project
(https://sentry.io/organizations/cn-films/projects/orange-county-lettings-website/?project=6543858)

### macOS / Linux

___The documentation for local development will assume that___
___the `python` command refers to the interpreter mentioned above (unless a virtualenv is set).___

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/AxAks/P13_Orange_County.git`

#### Add the required environment variables

1. Create a .env file at the project root:
   $ `cd P13_Orange_County`
   $ `touch .env`
   $ `echo SECRET_KEY='[YourSecretKey]' > .env`
   $ `echo DB_NAME='oc-lettings-site.sqlite3' >> .env`

#### Launch the project in a docker container

1. On first launch (the image first needs to be built):      
   $ `docker-compose up --build`

2. (1.bis) if the image has already been build, and you want to run this same image (no re-build):      
   $ `docker-compose up`

3. Visit `http://localhost:8000` in a web browser:                
   -> the website should be displayed, and you should be able to see some profiles and locations

#### Interact with the docker container

1. List all containers:     
   $ `docker ps -a`

2. Enter the docker Orange County container (via a bash terminal):     
   $ `docker exec -ti p13_orange_county_web_1 /bin/bash`  (the container must be running)

##### Checks

___The following indications assume that you are in the docker container in a bash shell___

#### Linting

    $ `flake8`     

#### Unittests

    $ `pytest`

#### Administration interface

1. With the Docker container launched

- Visit `http://localhost:8000/admin`
- login with user `admin`, and password `Abc1234!`

#### Errors monitoring

1. the monitoring is reachable at:

- https://sentry.io/organizations/cn-films/projects/orange-county-lettings-website/?project=6543858
  -> you will need to create an account and request access

- The Issues tab lists all captured issues
