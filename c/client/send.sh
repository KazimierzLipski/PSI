#!/bin/bash

sh ./create_container.sh
sleep 2s
reset
echo "
Container created
"
docker images | grep z33_task1_1_c_client
sleep 5s
reset
echo "
Running container...
"
sh ./run_container.sh $1
echo "
Container created"
docker ps | grep z33_task1_1_c_client
sleep 5s
reset
sh ./off.sh
reset