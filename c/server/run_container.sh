#!/bin/bash

docker run -it -d --rm --network-alias z33_c_server --hostname z33_c_server --network z33_network --name z33_c_server z33_task1_1_c_server 8000
