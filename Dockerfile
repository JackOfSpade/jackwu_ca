FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

ENV COMPOSE_CONVERT_WINDOWS_PATHS=1

RUN mkdir /jackwu_ca

WORKDIR /jackwu_ca

COPY . /jackwu_ca

RUN apt-get -y update && \
    apt-get -y upgrade && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install django-storages && \
    pip install google-cloud-storage && \
    pip install gunicorn && \
    mkdir static && \
    apt-get -y update && \
    apt-get -y upgrade