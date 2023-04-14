#!/bin/bash

sh ./create_container.sh
sh "clear"
echo "
Container created
"
sh "docker images | grep z33"
sleep 1s
sh "clear"
echo "
Running container...
"
sh ./run_container.sh