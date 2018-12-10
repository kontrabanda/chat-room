#!/usr/bin/env bash

if [[ -z "$1" ]]
  then
    echo "Please type client name"
    exit 1
fi

docker run -it --network chat_room_net --name $1 chat_room_client
docker container rm $1
