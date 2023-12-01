
import logging
import os, time
import json

from kafka import KafkaAdminClient, KafkaConsumer

import sys

def consumer_from_kafka(topic):
    consumer = KafkaConsumer(bootstrap_servers='kafka:29092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
    consumer.subscribe(['spark-demo-events'])


    for message in consumer:
        print(message)

    consumer.close()

def main():
    print("consumer : ")
    topic = 'spark-demo-events'
    try:
        admin = KafkaAdminClient(bootstrap_servers='kafka:29092')
    except Exception:
        pass

    while True:
        print("b")
        consumer_from_kafka(topic)
        time.sleep(15)

   


if __name__ == "__main__":
    main()
    
