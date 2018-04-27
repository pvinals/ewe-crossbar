#!/bin/sh

#Reset docker machine if exists
docker stop crossbar
docker rm crossbar

#Create the image
docker build -t crossbar -f Dockerfile .

#Run crossbar localhost:8081
docker run --rm -it --name crossbar --network=sefarad_sefarad-network -p 8081:8081 -p 8082:8082 -p 1883:1883 crossbar