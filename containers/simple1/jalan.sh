docker rm -f python-container
docker  run --name python-container \
            -p 9999:5000 \
            -v ${PWD}/../app:/app  \
            -ti python:3.11-alpine  sh /app/run.sh
