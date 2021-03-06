FROM ubuntu:latest
#The next command sets root password s 1234 inside the container
RUN echo "root:123456" | chpasswd
# This adds a user named 'nonrootuser' and creates password as 1234 and adds them to sudoers list
RUN useradd -ms /bin/bash nonrootuser
RUN echo "nonrootuser:123456" | chpasswd
# Gets sudo and adds nonrootuser to the list of sudoers
RUN apt-get update && apt-get install --no-install-recommends --yes python3
RUN apt-get install sudo -y
RUN usermod -aG sudo nonrootuser
#Important things to get
RUN apt-get install wget -y
RUN apt install git -y
RUN apt-get install python3-pip -y
#GETTING BACKEND LIBRARIRES
# pandas numpy requests amazon-product-review-scraper wordcloud nltk
#INSTALL NLTK DEPENDENCIES
USER nonrootuser
COPY ./amazon_sentiment/resources/ /resources/
COPY requirements.txt /resources/
RUN pip install -r /resources/requirements.txt
RUN python3 /resources/nltk_prerequisites.py
USER root
RUN rm -rf /resources
#This switches user into 'nonroot' and changes working directory into home of that user
USER nonrootuser
# RUN apt-get install python3-venv -y
RUN mkdir /home/nonrootuser/codes
# COPY run.py /home/nonrootuser/codes
# COPY amazon_sentiment /home/nonrootuser/codes/
WORKDIR /home/nonrootuser/codes