# Kafka Project Documentation



## Project Overview

This project demonstrates two different Kafka deployment scenarios using Docker:

1. **Mono-Broker**: 1 Broker + Kafdrop.
2. **Cluster**: 3 Brokers + 1 Dedicated Controller + Kafdrop.

The workflow involves building a stream, publishing it to a Kafka topic, and consuming that stream in real-time.



## Tech Stack

- **Infrastructue**: Docker & Docer Compose
- **Kafka**: ```apache/kafka:4.2.0``` (KRaft mode)
- **Web UI**: ```obsidiandynamics/kafdrop``` (Available at ```http://localhost:19000```
- **Langage**: Python 3.11-slim-bullseye
- **Librairie**: ```kafka-python-ng```

## Project Structure
Below is a project structure created:

```
├── consumer
│   ├── app
│   │   ├── __init__.py
│   │   └── consumer.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── requirements.txt
├── images
│   ├── docker-compose_cluster.pdf
│   └── docker-compose_mono.pdf
├── kafka
│   ├── doc_tmp
│   │   ├── docker-compose_apache_c2B_kafdrop.yml
│   │   ├── docker-compose_apache_mono.yml
│   │   ├── docker-compose_mono_control.yml
│   │   ├── docker-compose_mono.yml
│   │   ├── docker-compose_ori.yml
│   │   └── docker-compose_ori1.yml
│   ├── docker-compose_apache_mono_kafdrop.yml
│   └── docker-compose-apache_cluster_kafdrop.yml
├── producer
│   ├── app
│   │   ├── __init__.py
│   │   ├── generate-random-event_1_capteur.py
│   │   ├── kafka_create_topic_2_partitions.py
│   │   ├── kafka_create_topic.py
│   │   ├── kafka_remove_topic.py
│   │   └── producer_generate-random-events.py
│   ├── docker-compose_jupyter.yml
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── Dockerfile_jupyter
│   ├── requirements_jupyter.txt
│   └── requirements.txt
├── exec-consumer.sh
├── exec-producer_example_1.sh
├── exec-producer_example_2.sh
├── exec-spark_example_1.sh
├── exec-spark_example_2.sh
├── exec-spark_example_3.sh
├── exec-spark_example_4.sh
├── exec-spark.sh
├── kafka_README.md
├── stop-docker-kafka-producer-consumer-cluster.sh
└── stop-docker-kafka-producer-consumer-mono.sh   
```

## Usage Instruction

### 1. Launching the Infrastructure

You can start the environment using the provided shell scripts or by running the compose files manually.

#### Option A: Mono-Broker Version

```
Bash
# Using the script
./start-docker-kafka-producer-consumer-mono.sh

# Or manually:
cd kafka && docker compose -f docker-compose_apache_mono_kafdrop.yml up -d 
cd ../consumer && docker compose up -d
cd ../producer && docker compose up -d
```

#### Option B: Cluster Version (3 Brokers)

```
Bash
# Using the script
./start-docker-kafka-producer-consumer-cluster.sh

# Or manually:
cd kafka && docker compose -f docker-compose-apache_cluster_kafdrop.yml up -d 
cd ../consumer && docker compose up -d
cd ../producer && docker compose up -d
```

The configuration will create 3 clusters with 4 containers:

- consumer
  - consumer container
- publisher 
  - producer container
- kafka (version mono)
  - broker-1 container
  - kafdrop container
 <img src="./images/docker-compose_mono.pdf" title="Docker mono cluster" />
- kafka (version cluster)
  - controller container
  - broker-1 container
  - broker-2 container
  - broker-3 container
  - kafdrop container 
<img src="./images/docker-compose_cluster.pdf" title="Docker mono cluster" />


### 2. Monitoring with Kafdrop

Once the containers are healthy, open your browser to view topics, partitions, and consumer groups:

URL: <http://localhost:19000>

## Running the Examples
To see the data in motion, open two terminal windows:

### Step 1: Start the Consumer

The consumer will wait for incoming messages.

```
Bash
./exec-consumer.sh
# Internally runs: docker exec consumer python consumer.py
```

### Step 2: Start the Producer

The producer will begin generating random event data and sending it to Kafka.

```
Bash
./exec-producer_example_1.sh
# Internally runs: docker exec producer python producer_generate-random-events.py
```

## Helpful Resources

- [Docker Documentation](https://docs.docker.com/get-started/overview/)
- [Kafdrop Github](https://github.com/obsidiandynamics/kafdrop)
- [Apache Kafka Documentation](https://kafka.apache.org)
- [Kafka-python-ng](https://pypi.org/project/kafka-python-ng/)
