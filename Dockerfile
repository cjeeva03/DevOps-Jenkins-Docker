FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /home/appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY flask-ci-cd/app/ ./app/
COPY flask-ci-cd/tests/ ./tests/
EXPOSE 5000
CMD ["python", "-m", "app.main"]
