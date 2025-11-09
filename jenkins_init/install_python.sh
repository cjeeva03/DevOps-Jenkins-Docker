#!/bin/bash
set -e
apt-get update && apt-get install -y python3 python3-pip
ln -s /usr/bin/python3 /usr/local/bin/python
