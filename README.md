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


The documentation for local development will assume that the `python` command refers to the interpreter mentioned above (unless a virtualenv is set).

### macOS / Linux

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
$ docker-compose up --build

2. 1bis. if the image has already been build and you want to run this same image (no re-build):      
$ docker-compose up 

3. Visit `http://localhost:8000` in a web browser:                
-> the website should be displayed, and you should be able to see some profiles and locations

#### Interact with the docker container 
1. List all containers:     
$ docker ps -a

2. Enter the docker Orange County container (via a bash terminal):     
$ docker exec -ti p13_orange_county_web_1 /bin/bash  (the container must be running)


##### Checks
The following indications assume that you are in the docker container in a bash shell

#### Linting 
$ flake8     

#### Unitests
$ pytest      

#### Interact with the Database
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from profiles_profile
where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
