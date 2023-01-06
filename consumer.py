from kafka import KafkaConsumer
import os


topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")


consumer = KafkaConsumer(topic, 
    bootstrap_server, 
    auto_offset_reset='earliest', 
    enable_auto_commit=True, 
    group_id='my-group')


for msg in consumer:
    print (msg)