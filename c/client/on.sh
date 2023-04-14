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
echo "
Container created"
docker ps | grep z33
sleep 3s
docker logs --follow z33_c_client