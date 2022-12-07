#swarm mode


docker rm -f myhost1 myhost2 myhost3 myhost0
docker network rm  myapp-network


docker swarm init 

docker swarm join-token worker

docker network create \
	--driver overlay \
	--attachable myapp-network


docker run -dit --name myhost0 -p 9998:9999 -v $(pwd)/webserver:/www --network myapp-network php:7.4 php -S 0.0.0.0:9999 -t /www
docker run -dit --name myhost1 -p 9999:9999 -v $(pwd)/webserver:/www --network myapp-network python:3.11-alpine python3 -m http.server -d /www 9999
docker run -dit --name myhost2 --network myapp-network alpine:3.11 /bin/sh -c 'apk update && apk add curl;while true;do sleep 10000;done'
docker run -dit --name myhost3 --network myapp-network alpine:3.11 /bin/sh -c 'apk update && apk add curl;while true;do sleep 10000;done'
