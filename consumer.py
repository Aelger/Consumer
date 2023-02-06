from kafka import KafkaConsumer

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    group_id='my-group',
    auto_offset_reset='earliest'
)

for message in consumer:
    print(message.value.decode())