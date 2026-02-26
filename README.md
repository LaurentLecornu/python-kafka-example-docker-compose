[kafka_README.md](https://github.com/user-attachments/files/25567417/kafka_README.md)
# Example : Kafka



## Step 1 : Kafka

2 versions : 
- version mono broker
- version cluster with 3 brokers et 1 controller


The steps :

1. Build and start the docker image
2. Open terminals and run the test

We will create a stream, send it to Kafka and consume it from kafka.
![Markdown preferences pane](./images/docker-compose.pdf)


## Stack

- Docker
- image docker apache/kafka:4.2.0
- librairie python kafka-python-ng
- Python 3.11 slim

## How to use

### Using Docker Compose

The configuration will create 3 clusters with 4 containers:

- kafka 
  - broker-1 container
  - kafdrop container
- consumer
  - consumer container
- publisher 
  - producer container

in 3 docker-compose.

- The first 2 containers for Kafka (kafka services)
- the second one for the publisher service (with topic creation)
- the third one for the consumer service  (read the kafka server)

We launch in three terminals.

You will need Docker installed to follow the next steps. To create and run the image use the following command:

if your are in the directory *kafka*

```bash
docker-compose -f docker-compose_apache_mono_kafdrop.yml up -d
```

wait few minuites (until the end of kafka services starting )

In an other terminal :
if your are in the directory *producer*

```bash
docker-compose up -d
```

In an other terminal :
if your are in the directory *consumer*

```bash
docker-compose up -d
```
or 
```
docker-compose -f consumer/docker-compose.yml up -d
```

The Publisher (producer) container sends data to Kafka.

The Consumer container is a script that aims to wait and receive messages from Kafka.

And the kafdrop container will provide acess to  web UI for viewing Kafka topics and browsing consumer groups that can be accessed at `http://localhost:19000`.

Some shell files help for these commands


## Project Structure
Below is a project structure created:

```
cmd .
├── README.md
├── architecture_lambda.pdf
├── kafka
│   ├── docker-compose_apache_mono_kafdrop.yml
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
    │   ├── producer_generate-random-events.py
    └── requirements.txt
```



## Help and Resources
You can read more about the tools documentation:

- [Docker](https://docs.docker.com/get-started/overview/)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Kafka](https://kafka.apache.org)
- [Kafka-python](https://kafka-python.readthedocs.io/en/master/)
