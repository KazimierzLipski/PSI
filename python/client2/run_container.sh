#!/bin/bash

docker run --rm -it --network-alias z33_python_client2 --hostname z33_python_client2 --network z33_network --name z33_python_client2 z33_task1_2_python_client $1 $2
