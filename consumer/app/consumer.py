import time
import json
from datetime import datetime
from kafka import KafkaAdminClient, KafkaConsumer

def consumer_from_kafka(topic):

    consumer = KafkaConsumer(topic, bootstrap_servers='broker-1:19092',auto_offset_reset="earliest",
enable_auto_commit=True, auto_commit_interval_ms=1000)
    consumer.subscribe([topic])

    city_stations={}
    # if consumer.empt
    for message in consumer:
        event_sensor = json.loads(message.value.decode())
        print(event_sensor)
        #print("da",datetime.utcfromtimestamp(station["last_update"]/1000).strftime('%Y-%m-%d %H:%M:%S'))
    
    consumer.close()



def main():
    print("consumer : ")
    topic = 'kafka-demo-events'
    try:
        admin = KafkaAdminClient(bootstrap_servers='broker-1:19092')
    except Exception:
        pass

    consumer_from_kafka(topic)

if __name__ == "__main__":
    main()
    
