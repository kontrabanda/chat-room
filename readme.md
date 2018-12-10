#DOCKER

##NETWORK
* docker network create --driver bridge chat_room_net
* docker network inspect chat_room_net
* docker network rm chat_room_net

##SERVER
* docker build -t chat_room_server -f ./server/Dockerfile .
* docker run -it --network chat_room_net --name chat_room_server chat_room_server
* docker container rm chat_room_server

##CLIENT
* docker build -t chat_room_client -f ./client/Dockerfile .
* docker run -it --network chat_room_net --name chat_room_client chat_room_client
* docker container rm chat_room_client
