FROM mageai/mageai:latest
ARG PIP=pip3
# Install OpenJDK 11
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk
RUN ${PIP} install pyspark
ENV MAGE_DATA_DIR=
