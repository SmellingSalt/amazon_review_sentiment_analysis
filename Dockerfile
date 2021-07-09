#Build it with docker build . -t tensorflow
# Create an image with docker run tensorflow --gpus all
FROM tensorflow/tensorflow
#The next command sets root password s 1234 inside the container
RUN echo "root:123456" | chpasswd
# This adds a user named 'nonrootuser' and creates password as 1234 and adds them to sudoers list
RUN useradd -ms /bin/bash nonrootuser
RUN echo "nonrootuser:123456" | chpasswd
# Gets sudo and adds nonrootuser to the list of sudoers
RUN apt-get update
RUN apt-get install sudo -y
RUN usermod -aG sudo nonrootuser
#Important things to get
RUN apt-get install wget -y
RUN apt install git -y
RUN apt-get install python3-venv -y
#This switches user into 'nonroot' and changes working directory into home of that user
USER nonrootuser
RUN mkdir /home/nonrootuser/codes
WORKDIR /home/nonrootuser