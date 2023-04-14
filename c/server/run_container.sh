#!/bin/bash

docker run -it --rm --network-alias z33_c_server --hostname z33_c_server --network z33_network --name z33_c_server z33_task1_1_c_server --ip 172.21.33.0 8000
