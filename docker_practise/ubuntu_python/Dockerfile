FROM ubuntu:20.04
RUN apt-get update

# change python3.10 to any preferred python version you like
# some extra questions
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y python3.10
RUN apt-get install -y python3-pip

RUN su -
RUN apt-get install sudo -y
RUN sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

# change the url to any preferred python version
# go check https://www.python.org/ftp/python/ for available versions
# ex: wget https://www.python.org/ftp/python/x.xx.x/Python-x.xx.x.tgz
# ex: tar -xf Python-x.xx.x.tgz
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tgz
RUN tar -xf Python-3.10.7.tgz

# change the directory name according to the preferred python version
# ex: /tmp/Python-x.xx.x/configure --enable-optimizations
RUN /tmp/Python-3.10.7/configure --enable-optimizations

RUN sudo make altinstall
RUN sudo make install

# set /root as login directory
WORKDIR /root