#!/bin/bash
function conclude () {
  echo
  echo "==> Concluding experiment"

  ./postExperiment.sh $1
  exit
}
./rollback.sh

if [ "$2" == "--protected" ]; then
  echo "running with MTFS"
  docker run -it -v /datasets:/home/john -v $(pwd)/malware:/malware --privileged --device /dev/fuse --env HOME=/home/john mtfs-testbed-protected && conclude $1
else
  docker run -it -v /datasets:/home/john -v $(pwd)/malware:/malware --env HOME=/home/john mtfs-testbed bash && conclude $1
fi

echo
echo ".. Did you build the Dockerfile?"


