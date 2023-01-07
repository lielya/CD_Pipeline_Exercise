FROM ubuntu:latest
# ENV VERSION=1.2.0
# USER root
# RUN apt-get update
# RUN apt-get upgrade -y
# RUN apt-get install -y python3
# RUN apt-get install vim -y
# RUN apt-get install zip -y
# RUN apt-get install unzip -y
COPY ./zip_job.py /tmp
COPY ./is_file_exist /tmp
CMD cat /etc/os-release && /bin/bash /tmp/is_file_exist