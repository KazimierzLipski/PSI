#!/bin/bash

sh ./create_container.sh
reset
echo "
Container created
"
sh "docker images | grep z33"
sleep 1s
reset
echo "
Running container...
"
sh ./run_container.sh