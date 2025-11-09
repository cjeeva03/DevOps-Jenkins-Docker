FROM jenkins/jenkins:lts
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3.13-venv && \
    ln -s /usr/bin/python3 /usr/local/bin/python && \
    rm -rf /var/lib/apt/lists/*
USER jenkins

