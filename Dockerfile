FROM ubuntu
RUN apt-get update

# install python environment
RUN apt-get install -y python --fix-missing
RUN apt-get install -y python3-pip
RUN apt-get install language-pack-en-base -y
RUN apt-get install htop -y
RUN apt-get install vim -y

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install flask-classful

ENV LC_ALL='en_US.utf8'

# copy executble scripts
COPY server /root/server

CMD python3 /root/server/main.py