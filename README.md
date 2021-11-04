# jif-api
RESTful API backend for pyadi-jif

Note that this project uses [poetry](https://python-poetry.org) for management.

## Set up dev environment
poetry install --no-root

## Start Server
python -m uvicorn core:app --reload --host=0.0.0.0