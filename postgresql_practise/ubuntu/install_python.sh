#!/bin/bash

apt-get update
su -
apt-get install sudo -y
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget -y
cd /tmp
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
tar -xf Python-3.8.12.tgz
cd Python-3.8.12
./configure --enable-optimizations
sudo make altinstall
sudo make install