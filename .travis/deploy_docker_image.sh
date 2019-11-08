#!/bin/sh

docker login -u $DOCKER_USERNAME -p $DOCKER_PWD
TAG="latest"

docker build -t akgeodude/scrapeme:latest .
docker push akgeodude/scrapeme:latest
