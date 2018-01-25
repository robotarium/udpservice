#!/bin/bash

sudo docker build --build-arg RECLONE-GIT=$(date +%s) --tag robotarium:udp_general_purpose .
