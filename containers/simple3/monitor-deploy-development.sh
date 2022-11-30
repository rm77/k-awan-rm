targetrepo=development
gitrepo=https://github.com/rm77/k-awan-dev-example.git
portmap=9999:5000
mkdir -p tmp_app
touch versioninfo
git clone $gitrepo tmp_app
CDIR=$(pwd)
while true;
do
  cd tmp_app
  git checkout $targetrepo
  git pull origin $targetrepo
  info=$(git log --oneline --decorate origin/$targetrepo | sha256sum )
  currentinfo=$(cat $CDIR/versioninfo | sha256sum)
  nama=$targetrepo
  [[ $info == $currentinfo ]] && echo "sama" || ( echo "terjadi perubahan"; echo $info > $CDIR/versioninfo ; docker build -t "$nama" . ; docker rm -f $nama; docker run -d --name $nama -p $portmap $nama )
  sleep 10
  cd $CDIR
done
