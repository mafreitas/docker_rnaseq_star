#!/usr/bin/env bash

IMAGE="chip_seq:latest"
GENOMES="/Users/mfreitas/repos/docker_rnaseq_star/genomes"
docker run -it -v $PWD:/share -v $GENOMES:/genomes $IMAGE