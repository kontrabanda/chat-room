#!/usr/bin/env bash

docker run -it --network chat_room_net --name chat_room_server chat_room_server
docker container rm chat_room_server
