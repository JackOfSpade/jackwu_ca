FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

ENV COMPOSE_CONVERT_WINDOWS_PATHS=1

RUN mkdir /jackwu_ca

WORKDIR /jackwu_ca

# Copy commands cannot be chained like RUN
COPY . /jackwu_ca

RUN apt-get -y update && \
    apt-get -y upgrade && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install django-storages && \
    pip install google-cloud-storage && \
    pip install gunicorn && \
    mkdir static && \
    # test
    apt-get -y install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio && \
    apt-get -y update && \
    apt-get -y upgrade