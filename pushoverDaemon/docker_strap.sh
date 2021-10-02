#!/usr/bin/env bash

docker build -t pushover_daemon:1.0 .

docker create --name pushd_$(date +"%m_%d_%H_%M") pushover_daemon:1.0
