# This defines the environment for all docker-compose apps

FROM python

ENV PYTHONUNBUFFERED 1

ENV COMPOSE_CONVERT_WINDOWS_PATHS=1

RUN mkdir /jackwu_ca

COPY . /jackwu_ca

WORKDIR /jackwu_ca

RUN pip install -r requirements.txt && \
    pip install django-storages && \
    pip install google-cloud-storage && \
    # Update packages
    apt-get -qq update && \
    # Apache web server
    apt-get install --yes apache2 apache2-dev && \
    # mod_wsgi
    pip install mod_wsgi && \
    cat httpd.conf >> /etc/apache2/httpd.conf
