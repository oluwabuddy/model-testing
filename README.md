<<<<<<< HEAD
# model-testing
=======
# About
This repo contains a typical app that allows creating an entity that takes time to process. The /model endpoint creates the model in the backend. However, the corresponding saved entity can only transition to the state "SUCCESS" after 5 minutes. Consumers of its api, then have to poll the get endpoint till the 5 minutes is elapsed.

The application frontend consists of two pages; model and result pages. The model page allows the user set the name of the model that will trained in the backend. The training takes about 5 minutes to complete. While the model is in the training phase, the status will be `PROCESSING`. Once the training is done, the status will be `SUCCESS`.

On the result page, if the model training status is `PROCESSING`, only the status will be shown. If it is `SUCCESS`, a graph will appear.

# Local run

## backend
0. [optional] install (and activate) a python virtual enviornment
1. Install the requirements via the command: `pip install -r requirements.txt`
2. you are good to go, to run,
```
fastapi dev api/main.py
```
The backend api is then available at http://127.0.0.1:8000/
the corresponding swagger docs: http://127.0.0.1:8000/docs


## frontend
!! make sure the backend is running at first

0. [optional] install (and activate) a python virtual enviornment
1. Install the requirements via the command: `pip install -r requirements.txt`
2. you are good to go, to run,
```
streamlit run frontend/Model.py --server.port 8001
```

The frontend is then available at http://127.0.0.1:8001/


# Docker
To build: ` docker-compose -f docker-compose.local.yml build`

To run: `docker-compose -f docker-compose.local.yml up`
>>>>>>> fb16ab6 (Initial commit - API and Cypresss tests)
