# Set python version
ARG BASE_CONTAINER=python:3.11-alpine

# Set the base image 
FROM python:3.11-alpine

# Adds metadata to image.
LABEL maintainer="Laurent"

# dont write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# dont buffer to stdout/stderr
ENV PYTHONUNBUFFERED 1

# Sets the user name to use when running the image.
USER root
RUN apk update 

# Make a directory for app
WORKDIR /consumer

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir && pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir --user -r /req.txt

# Copy source code
COPY ./app ./app

# Run the application
CMD ["python", "app/consumer.py"]
