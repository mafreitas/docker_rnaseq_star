#!/usr/bin/env bash

IMAGE="chip_seq:latest"

docker run -it -v $PWD:/share $IMAGE