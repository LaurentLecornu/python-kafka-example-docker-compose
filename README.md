# Lab 2 : Kafka

## Architecture Lambda

## Step 1 : Kafka


The steps :

1. Build and start the docker image
2. Open terminals and run the test

We will create a stream, send it to Kafka and consume it from kafka.
![Markdown preferences pane](architecture_big_data.pdf)


## Stack

- Docker
- Kafka-python
- Python 3.11

## How to use

### Using Docker Compose

The configuration will create a cluster with 5 containers:

- kafka container
- kafdrop container
- zookeeper container
- Consumer container
- Publisher container

in 3 docker-compose.

- The first 3 containers for Kafka (kafka services)
- The producer (with topic creation)
- The consumer (read the kafka server)

We launch in three terminals.

You will need Docker installed to follow the next steps. To create and run the image use the following command:

if your are in the directory *kafka*

```bash
docker-compose up --build &
```

wait few minuites (until the end of kafka services starting )

In an other terminal :
if your are in the directory *producer*

```bash
docker-compose up --build &
```

In an other terminal :
if your are in the directory *consumer*

```bash
docker-compose up --build &
```
or 
```
docker-compose -f consumer/docker-compose.yml up -d
```

The Publisher container sends data to Kafka.

The Consumer container is a script that aims to wait and receive messages from Kafka.

And the kafdrop container will provide acess to  web UI for viewing Kafka topics and browsing consumer groups that can be accessed at `http://localhost:19000`.


## Project Structure
Below is a project structure created:

```
cmd .
├── README.md
├── architecture_lambda.pdf
├── kafka
│   ├── docker-compose.yml
├── consumer
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   └── consumer.py
│   └── requirements.txt
└── producer
│   ├── docker-compose.yml
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── producer.py
    └── requirements.txt
```



## Help and Resources
You can read more about the tools documentation:

- [Docker](https://docs.docker.com/get-started/overview/)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Kafka](https://kafka.apache.org)
- [Kafka-python](https://kafka-python.readthedocs.io/en/master/)