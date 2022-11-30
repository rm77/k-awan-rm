mkdir -p tmp_app && cp -R ../app/* tmp_app
docker build -t myapp:v1.0 -f Dockerfile .
rm -rf tmp_app
