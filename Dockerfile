# Base the image on Debian 7
# Picked Debian because it's small and what runs on the bot
# https://registry.hub.docker.com/_/debian/
FROM debian:7.7
MAINTAINER Vijay Thiagarajan <kvijay1995@gmail.com>

# These are the packages installed via setup/setup_bone.sh
# https://github.com/IEEERobotics/bot2014/blob/master/setup/setup_bone.sh
RUN apt-get update && apt-get install -y python-pip \
                                         python-smbus \
                                         git \
                                         libzmq-dev \
                                         python-zmq \
                                         python-dev \
                                         python-yaml \
                                         python-numpy \
                                         python3.2 \
                                         python \
                                         wget \
                                         vim \
                                         tmux

# By default, start a server
CMD ["./Video_server.py"]
