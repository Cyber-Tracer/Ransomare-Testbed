FROM ubuntu:20.04

RUN apt-get update && apt install vim python3 python3-pip git -y && pip install pyinstaller
