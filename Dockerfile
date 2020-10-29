FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

ENV COMPOSE_CONVERT_WINDOWS_PATHS=1

RUN mkdir /jackwu_ca

WORKDIR /jackwu_ca

COPY . /jackwu_ca

RUN apt-get -y update && \
    apt-get -y upgrade && \
    pip install -r requirements.txt && \
    pip install django-storages && \
    pip install google-cloud-storage && \
    pip install gunicorn && \
    apt-get -y update && \
    apt-get -y upgrade
    # SSL-certificate (run this before docker-compose up) -----------------------------
#    apt-get -y install snapd
#    service snapd start
#    snap install core
#    snap refresh core
#    apt-get remove certbot
#    snap install --classic certbot
#    ln -s /snap/bin/certbot /usr/bin/certbot
#    certbot certonly --standalone
#    apt-get -y update
#    apt-get -y upgrade
    # ----------------------------------------------------------------------------------------