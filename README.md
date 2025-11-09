
# CI/CD Pipeline with Jenkins + Docker

Set up a local Jenkins pipeline to build, test, and run a Dockerized app.


## Pre-Requisites

 - [Docker Engine](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
    - [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
    - [Linux](https://docs.docker.com/desktop/setup/install/linux/)
    - [Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
  - [Jenkins Docker](https://www.jenkins.io/doc/book/installing/docker/)
  - [Git Bash](https://git-scm.com/install/)


## Task

- A minimal Flask app with a unit test
- Dockerfile to containerise the app
- Jenkinsfile (Declarative pipeline) that checks out the repo, runs the tests, builds the image and starts a container
- **Optional** email/Slack notification blocks



## Layout

```sh
flask-ci-cd/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md

```
## Quick start (local)

### 1. Clone the repo
```bash
git clone https://github.com/cjeeva03/DevOps-Jenkins-Docker.git
cd flask-ci-cd
```
### 2. Run the app locally (no Docker)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.main 
```
### 3. Jenkins Setup
```bash
docker compose up -d
```
__Jenkins Plugin__

- Pipeline
- Git
- Docker Pipeline
- Email Extension (if you want email)
- Slack Notification (if you want Slack)
### 4. Build & run with Docker
```bash
docker build -t flask-ci-cd .
docker run -p 5000:5000 flask-ci-cd
```
Visit `http://localhost:5000/health` – you should see `{"status":"ok"}`.


## Roadmap

### commit history
    1. initial commit
    2. Error faced - [python -m venv venv] Jenkinsfile - Added seperate python docker
    3. Removed python docker and modified jenkins image
    4. python error fix venv setup

