NAMA=myapp
NAMAIMAGE=myapp:v1.0
docker rm -f $NAMA
docker run -dit \
	--name $NAMA \
	-p 9999:5000 \
	$NAMAIMAGE
