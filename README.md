# python-kafka-docker
The main objective in this project was to learn how to create an application that sends and receives a message from Kafka, using Docker and docker-compose tools.

## Stack

- Docker
- Kafka-python
- Python 3.11

## How to use

### Using Docker Compose 
You will need Docker installed to follow the next steps. To create and run the image use the following command:

```bash
> docker-compose up --build &
```

The configuration will create a cluster with 5 containers:

- Consumer container
- Publisher container
- kafka container
- kafdrop container
- zookeeper container

The Publisher container sends data to Kafka.

The Consumer container is a script that aims to wait and receive messages from Kafka.

And the kafdrop container will provide acess to  web UI for viewing Kafka topics and browsing consumer groups that can be accessed at `http://localhost:19000`.


## Project Structure
Below is a project structure created:

```
cmd .
├── README.md
├── docker-compose.yml
├── consumer
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   └── main.py
│   └── requirements.txt
└── producer
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── generate-random-events.py
    └── requirements.txt
```



## Help and Resources
You can read more about the tools documentation:

- [Docker](https://docs.docker.com/get-started/overview/)
- [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
- [Kafka](https://kafka.apache.org)
- [Kafka-python](https://kafka-python.readthedocs.io/en/master/)