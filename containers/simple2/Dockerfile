FROM python:3.11-alpine
RUN apk update && mkdir -p /app
COPY tmp_app/* /app/
ADD requirements.txt /app
ENTRYPOINT ["/bin/sh","/app/run.sh"]
