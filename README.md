## Project

 Orange County Lettings Website

## Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.9+
- Docker (v20.10+) and Docker Compose      
(https://docs.docker.com/get-docker/ or https://docs.docker.com/engine/install/)
- (Docker Desktop - not mandatory, only for convenience)
- Sentry account with access rights on the project     
(https://sentry.io/organizations/cn-films/projects/orange-county-lettings-website/?project=6543858)
- Heroku account with access rights on the project

## Development

### macOS / Linux

___The documentation for local development will assume that___
___the `python` command refers to the interpreter mentioned above.___

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/AxAks/P13_Orange_County.git`

#### Create a virtualenv and install requirements

At the project root:
- python -m virtualenv venv
- pip install -r requirements.txt

#### Add the required environment variables

1. Create a .env file at the project root:
2. Example of .env file:       
   `SECRET_KEY=MySecretKey`         
   `DEBUG=True`       
   `ALLOWED_HOSTS='*'`          
   `PORT=8000`   
   `DB_NAME=oc-lettings-site.sqlite3`
   `SENTRY_DSN=https://74f290ff50b1436daf464e567f3de6cb@o1289316.ingest.sentry.io/6543858`

#### Launch the project (not in container)
$ `python manage.py runserver`

#### CI/CD (continuous integration/deployment)
- pushes to master will trigger= linting checks, tests, build and save an image to DockerHub, deploy to heroku 
- pushes to any other branch will only trigger:  linting checks and tests
  (see .circleci/config.yml)


## Local Deployment:
#### Add the required environment variables
1. Create a .env file at the project root:
Example of .env file:    
   `SECRET_KEY=MySecretKey`         
   `DEBUG=True`       
   `ALLOWED_HOSTS='*'`          
   `PORT=8000`   
   `DB_NAME=oc-lettings-site.sqlite3`
   `SENTRY_DSN=https://74f290ff50b1436daf464e567f3de6cb@o1289316.ingest.sentry.io/6543858`
#### Download and launch the project (within container)
2. one-line command:
$ `docker run -p 8000:8000 --env-file .env -d --name p13_orange_county_app 'oclettings/p13_orange_county_app:latest'`

3. Visit `http://localhost:8000` in a web browser:                
-> the website should be displayed, and you should be able to see some profiles and locations

For admin interface:
- Visit `http://localhost:8000/admin`
- login with user `admin`, and password `Abc1234!`


#### Interact with the docker container (when created locally):
- stop container   
$ `docker stop p13_orange_county_app`
- start container after it has been stopped   
$ `docker start p13_orange_county_app`
- enter the container with bash (the container must be running)  
$ `docker exec -ti p13_orange_county_app /bin/bash`   
- delete container (container must be stopped)   
$ `docker rm p13_orange_county_app`  
- delete image   
$ `docker image rm 'oclettings/p13_orange_county_app:latest'`   
or    
$ `docker image ls`     
$ `docker image rm [IMAGE ID]`
- list all containers:     
$ `docker ps -a`

#### Errors monitoring

1. the monitoring is available on Sentry and reachable at:

- https://sentry.io/organizations/cn-films/projects/orange-county-lettings-website/?project=6543858    
  -> you will need to create an account and request access

  -> The Issues tab lists all captured issues


#### Manual Checks
1. Linting   
from outside the docker container     
$ `docker exec -ti p13_orange_county_app flake8`    
from inside the docker container   
$ `flake8`     

2. Unit tests    
from outside the docker container     
$ `docker exec -ti p13_orange_county_app pytest`     
from inside the docker container      
$ `pytest`    

## Note on Heroku (for Production):

Continuous Integration and Deployment is handled by circleCI:  
- It verifies the code when it is pushed to GitHub.    
-> The code is validated only if the linting and tests phases pass     

- If the push is made on branch Master  
-> CircleCi builds and save an image to DockerHub      
-> Once the image is on DockerHub, CircleCI deploys the app on Heroku     

Once on Heroku, the application is available at:        
https://p13-oc-lettings.herokuapp.com

