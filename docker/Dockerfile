FROM ubuntu:16.04
#FROM armv7/armhf-ubuntu

# Add code directory
RUN mkdir /code
WORKDIR /code

# Update dist
RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y python3 python3-pip
#RUN apk --update add python3

# Get git
RUN apt-get install -y git
#RUN apk --update add git

ARG RECLONE-GIT

# Get vizier framework
RUN git clone https://github.com/robotarium/vizier.git
RUN pip3 install vizier/python/

# Get UDP service
RUN git clone https://github.com/robotarium/udpservice.git
RUN pip3 install udpservice/
