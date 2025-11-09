FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /home/appuser
COPY flask-ci-cd/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY flask-ci-cd/app/ ./app/
COPY flask-ci-cd/tests/ ./tests/
WORKDIR /home/appuser/app
EXPOSE 5000
# CMD ["python", "-m", "app.main"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
