# consumer = KafkaConsumer("oracle-jdbc-M_ELASTICPLZ", bootstrap_servers="localhost:9092")

from confluent_kafka import Consumer, KafkaError


settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest'
}

def on_assign(consumer, partitions):
    for partition in partitions:
        partition.offset = 0

def on_message(message):
    if message.error() is not None:
        if message.error().code() == KafkaError._PARTITION_EOF:
            print("Reached end of partition.")
        else:
            print(f"Error while retrieving message: {message.error()}")
    else:
        print(f"Key: {message.key()}, Value: {message.value().decode('utf-8')}")

consumer = Consumer(settings)
consumer.subscribe(['oracle-jdbc-M_ELASTICPLZ'])
consumer.assign([])
consumer.poll(0)

# consumer.seek_to_beginning()
consumer.assign([p for p in consumer.assignment()])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError.PARTITION_EOF:
            print("Reached end of partition.")
        else:
            print(f"Error while retrieving message: {msg.error()}")
    else:
        on_message(msg)