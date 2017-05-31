FROM ubuntu:16.04

# Add code directory
ADD . /code
WORKDIR /code

# Update dist
RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y python3 python3-pip
RUN pip3 install paho-mqtt

ENTRYPOINT ["python3", "udpservice.py"]
