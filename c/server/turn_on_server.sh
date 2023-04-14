#!/bin/bash

sh ./create_container.sh
sleep 2s
reset
echo "
Container created
"
docker images | grep z33
sleep 5s
reset
echo "
Running container...
"
sh ./run_container.sh