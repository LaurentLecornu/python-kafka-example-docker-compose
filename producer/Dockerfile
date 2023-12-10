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

# Make a directory for our app
WORKDIR /publisher

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY ./app ./app

# Run the application
CMD ["python", "app/producer.py","velib-stations"]

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
