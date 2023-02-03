from kafka import KafkaConsumer
import logging
import pprint
import json
import os

log = logging.getLogger("CONSUMER-LOG")
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")


consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server, value_deserializer=lambda m: json.loads(m.decode('ascii')))


log.info("#################### TOPICS ####################")
log.info(consumer.topics())
log.info("#################### CONFIGS ####################")
log.info(pprint.pformat(consumer.config))
log.info("#################### END ####################")


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    message