#!/bin/bash

docker run --volume /home/robotarium/Git/RobotariumRepositories/robotarium_nodes/udp_service:/code/ \
	-d -p 4999:4999/udp \
robotarium:udp_service "udp_ports.json" "192.168.1.2" "4999" \
#python3 "/code/udpservice.py" "/code/udp_ports.json" "192.168.1.2" "4999"
