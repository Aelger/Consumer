# Deriving the latest base image
FROM registry.redhat.io/rhel8/python-39

ENV TOPIC="Default topic"
ENV BOOTSTRAP_SERVER="my-cluster-kafka-dos-kafka-bootstrap:9092"

# Labels as key value pair
LABEL Maintainer="Alegre Sandoval Duarte"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# I have chosen /usr/app/src
WORKDIR /usr/app/src


# To COPY the remote file at working directory in container
COPY consumer.py ./
# Now the structure looks like this '/usr/app/src/test.py'
COPY requirements.txt ./


RUN pip3 install -r requirements.txt


# CMD instruction should be used to run the software
# Contained by your image, along with any arguments.
CMD [ "python", "./consumer.py"]