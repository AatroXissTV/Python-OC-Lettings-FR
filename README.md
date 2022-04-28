# Orange County Lettings

# Status
[![CircleCI](https://circleci.com/gh/AatroXissTV/Python-OC-Lettings-FR/tree/master.svg?style=svg)](https://circleci.com/gh/AatroXissTV/Python-OC-Lettings-FR/tree/master)

# Quick Access

1. [Informations](#informations)
2. [Local development](#local-development)
3. [Deployment](#deployment)

# Informations

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

# local development

## Prerequisites

- A Github account
- Git and SQLite3 installed on your computer
- Python 3.10.2 installed

## Clone the repository

- `cd path/to/your/project`
- `git clone https://github.com/aatroxisstv/Python-OC-Lettings-FR.git`

## Create a virtual environment

  - `cd path/to/your/project`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`

## Environnement variables: .env file

To generate a .env file please launch the `python_setup_env.py` script.
You can modify the .env file to your needs with:
  - URL of sentry (SENTRY_DSN).
  - The DEBUG variable (DEBUG).

## Launch the project

- `cd path/to/your/project`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- Make migrations: `python manage.py migrate`
- load initial data: `python manage.py loaddata data.json`
- launch the server: `python manage.py runserver`
- Go to `http://127.0.0.1:8000/` in your browser.

## Linting

- `cd path/to/your/project`
- Activate the virtual environment: `source .venv/bin/activate`
- launch flake8: `flake8`

## Unit tests

  - `cd path/to/your/project`
  - Activate the virtual environment: `source .venv/bin/activate`
  - launch the tests suite: `pytest`

# Docker

# Deployment
