#!/bin/bash

sh ./create_container.sh
sleep 2s
reset
echo "
Container created
"
docker images | grep z33_task1_2_python_client
sleep 5s
reset
echo "
Running container...
"
sh ./run_container.sh $1
sleep 2s
reset