from kafka import KafkaConsumer
import logging
import pprint
import os

log = logging.getLogger("CONSUMER-LOG")
logging.basicConfig(level=logging.INFO)


topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")


consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server)


log.info("#################### TOPICS ####################")
log.info(consumer.topics())
log.info("#################### CONFIGS ####################")
log.info(pprint.pformat(consumer.config))
log.info("#################### END ####################")


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    log.info(message.value.decode('utf-8'))