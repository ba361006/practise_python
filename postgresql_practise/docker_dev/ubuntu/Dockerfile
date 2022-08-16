FROM ubuntu:18.04

RUN apt-get update
WORKDIR /root/code
COPY install_python.sh .
COPY app.py .
COPY requirements.txt requirements.txt

RUN ["/bin/bash", "./install_python.sh"]

RUN python3 -m pip install -r requirements.txt


ENTRYPOINT ["/bin/bash"]