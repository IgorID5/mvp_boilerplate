FROM python:3.8.12-slim

COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models

RUN pip install -r requirements.txt

# RUN CONTAINER LOCALLY
#CMD uvicorn package_folder.api_file:app --host 0.0.0.0

# RUN CONTAINER DEPLOYED
CMD uvicorn package_folder.api_file:app --host 0.0.0.0 --port $PORT
