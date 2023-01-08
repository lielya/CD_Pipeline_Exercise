FROM ubuntu:latest
ENV VERSION=1.2.0
USER root
RUN apt-get update 
RUN apt-get upgrade -y 
RUN apt-get install -y python3 vim zip unzip
COPY ./zip_job.py /tmp
COPY ./is_file_exist /tmp
CMD cat /etc/os-release && /bin/bash /tmp/is_file_exist
