FROM python:3.9.5-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y && apt-get install -y gcc python3-dev libpq-dev musl-dev libc-dev gettext cron

WORKDIR .

# Install dependencies.
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copying local code to the container image.
COPY . .
