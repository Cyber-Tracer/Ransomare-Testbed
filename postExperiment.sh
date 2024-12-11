#/bin/bash

SNAPSHOT=tank/datasets@post-$1
sudo zfs snapshot $SNAPSHOT

mkdir -p diffs
sudo zfs diff -FtH tank/datasets@baseline $SNAPSHOT 2>&1 | tee -a diffs/diff-$1.txt
