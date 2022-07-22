## Project

 Orange County Lettings Website

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.9+
- Docker (v20.10+) and Docker Compose (https://docs.docker.com/get-docker/ or https://docs.docker.com/engine/install/)
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
   $ `echo DEBUG='[True/False]' >> .env`
   $ `echo SENTRY_DSN='https://74f290ff50b1436daf464e567f3de6cb@o1289316.ingest.sentry.io/6543858' >> .env`
#### Launch the project in a docker container

1. Make sure the docker daemon is up
   $ `sudo systemctl status docker.service`
   -> to stop daemon: $ `sudo systemctl stop docker.service`
   -> to start daemon: $ `sudo systemctl start docker.service`
   or Launch Docker Desktop
2. 

3. Build the Docker Image:      
   $ `sudo docker build . -t [image_tagname]`

4. On first launch (the image first needs to be built)
   $ `sudo docker run -p 8000:8000 --env-file ./.env  [image_name/ID]`
5. Stop/Start Docker container:
   $ `sudo docker stop [container_name/ID]`
   $ `sudo docker start [container_name/ID]`

   1. Visit `http://localhost:8000` in a web browser:                
      -> the website should be displayed, and you should be able to see some profiles and locations

#### Interact with the docker container

1. List all containers:     
   $ `docker ps -a`

2. Enter the docker Orange County container (via a bash terminal):     
   $ `docker exec -ti [container_name] /bin/bash`  (the container must be running)

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

  -> The Issues tab lists all captured issues






------
