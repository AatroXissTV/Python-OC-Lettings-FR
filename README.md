# Orange Country Lettings

### Tech Stack and Status

[![CircleCI](https://circleci.com/gh/AatroXissTV/Python-OC-Lettings-FR/tree/master.svg?style=svg)](https://circleci.com/gh/AatroXissTV/Python-OC-Lettings-FR/tree/master)

## Quick Access

1. [Informations](#informations)
2. [Local development](#local-development)
3. [Docker](#docker)
4. [Deployment](#deployment)

## Informations

This is the deliverable of the 13th project of Python App Development course from OpenClassrooms.
It has been tested on **Python 3.10.2 - Django 3.0 and Windows 11**.

Several changes have been made to the original [code](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR) to make it more readable and to make it more maintainable.
1. Reducing technical debt with:
  - Fixed linting errors
  - Fixed pluralization errors
2. Redesigned the code to be more modular. 
  - Code is now split in 3 folders (home, profiles, lettings)
  - Convert oc_lettings_site into a django app.
  - Design a test suite.
3. Develop a CI/CD pipeline with [CircleCI](https://circleci.com/) and [Heroku](https://www.heroku.com/).

  The CI/CD pipeline is as follows:
  - Compiling: execute linting and tests suite
  - Contenerization: create and push an image to Docker Hub if commit has been made on master branch
  - Deployment: deploy the site with Heroku if commit has been made on master branch
  - Monitoring: monitor the site with [Sentry](https://sentry.io/).

## local development

### Prerequisites
To use the project locally, you need to have:
- GitHub account with read access to this repository
- Git CLI installed
- SQLite3 CLI installed
- Python 3.10.2 installed

### Clone the repository & create a virtual environment
To install the project locally, you need to clone the repository, create and activate a virtual environment.
    
    ```
    cd path/to/your/project
    git clone https://github.com/aatroxisstv/Python-OC-Lettings-FR.git
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### Environnement variables
You can generate a .env file by launching the `python_setup_env.py` script.
It will be used to configure the project.
You can modify the .env file to your needs with:
  - SENTRY_DSN: You will need to add your sentry dsn url here. [Here](https://docs.sentry.io/platforms/python/guides/django/) is how to generate one.
  - DEBUG=0 (False) or DEBUG=1 (True) (False by default).

When using this file, a DJANGO_SECRET_KEY environment variable will be created.

### Setup the project
Please make sure your virtual environment is activated.

    ```
    cd path/to/your/project
    source .venv/bin/activate
    ```

To setup the project, you need to install the requirements.txt file.
You will also need to migrate the database and add the data in the database.
    
    ```
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata data.json
    ```

You can execute the tests suite by running:
    
    ```
    pytest
    ```

And you can make sure linting is ok by running:
    
    ```
    flake8
    ```

## Docker

The project is built with Docker and therefore tou can build a docker image to run it locally or pull it from Docker Hub.
We will explain how these two methods work in the next sections.

Make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Build a docker image to run the project locally
You will need to have the project cloned and activated.
Make sure that the .env file has been properly generated (see [Environnement variables](#environnement-variables)).
To build the docker image, you need to run:
    
    ```
    docker build -t <image-name> .
    ```

where `<image-name>` is the name you want to give to your image.
To run it locally, you need to run:
    
    ```
    docker run -rm -p 8000:8000 --env-file .env <image-name>
    ```	

You can now access the app at `http://127.0.0.1:8000/`.

### Pull the image from Docker Hub and run it locally
First, you need to login to Docker Hub and go to this repository: `https://hub.docker.com/r/aatroxiss/oc-lettings`
Then copy the tag of the image you want to pull: preferably `latest`.
You can then run:
    
    ```
    docker pull aatroxisstv/oc-lettings:latest
    docker run -rm -p 8000:8000 --env-file .env aatroxisstv/oc-lettings:latest
    ```

You can now access the app at `http://127.0.0.1:8000/`.

## Deployment

The deployment of the app is automated with the CircleCI pipeline. When updates are pushed to the GitHub repository, the pipeline triggers the test suite and code linting for **all project branches**. If updates are pushed to the master branch, the pipeline triggers the test suite, code linting and the deployment of the app. The deployment is done **if and if only** the tests and linting are successful.

Here is the workflow of the CircleCI pipeline:
- Build the docker image, run the tests suite and code linting
- Push the image to Docker Hub
- Deploy the app on Heroku **if and if only** the tests and linting are successful

### Prerequisites
In order to deploy the project on Heroku, you need to have:
- GitHub account
- Heroku account
- CircleCI account (linked to your GitHub account)
- Docker account
- Sentry account

### Deployment setup

#### CircleCI
For this step we will assume that you have already done these steps:
- Clone the repository
- Setup the virtual environment
- Created the required accounts
You will need to create a new project on CircleCI and link it to your GitHub repository. Select the master branch as a source for the .circleci/config.yml file.

To run the CircleCI pipeline, you need to set the environment variables:

 | CircleCI variable | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| DOCKER_LOGIN      | Docker account username                                                                          |
| DOCKER_PASSWORD   | Docker account password                                                                          |
| DOCKER_REPO       | Docker repository name                                                                           |
| HEROKU_API_KEY    | Heroku API Key, can be found in account settings (Heroku API KEY)                                |
| HEROKU_APP_NAME   | Heroku app name: The deployed app will be accessed via `https://<HEROKU_APP_NAME>.herokuapp.com` |
| HEROKU_TOKEN      | Heroku token, can be found in account settings (Heroku API Key) same as HEROKU_API_KEY           |
| SECRET_KEY        | Django secret key that has been generated in your .env file                                      |
| SENTRY_DSN        | Sentry project URL                                                                               |

### Docker

Create a DockerHub repository. The repository name must match the DOCKER_REPO environment variable set in CircleCI.
The CircleCI workflow will build and push the app image in the DockerHub repository. All images are tagged with the CircleCI commit SHA ($CIRCLE_SHA1).

### Heroku

To create an app in your account, serveral methods exists:
- Method 1: Create the app manually on the heroku website. To be hooked up to the CircleCI pipeline, the name of the app must match the HEROKU_APP_NAME environment variable set in CircleCI. AND install Heroku Postgres addon for the database.
- Method 2: Create the app via the Heroku CLI. Use the command `heroku apps:create <app-name> --region eu --addons=heroku-postgresql`. The app name must match the HEROKU_APP_NAME environment variable set in CircleCI.

For the first commit please make sur to uncomment lines on the .circleci/config.yml file.
The commented lines will:
- delete contentypes from the basic database.
- Load the data in the database.
- Set the sentry dsn as an environment variable.

### Sentry

After creating a Sentry account, you will need to create a new Django project. You will need to get the SENTRY_DSN environment variable that can be found under the project settings > Client Keys.
Please make sure that this variable is set in the .env file and CircleCI.

Sentry error logging can be tested via the `/sentry-debug/` route.