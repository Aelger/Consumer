from kafka import KafkaConsumer
import os
import logging
import pprint

topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")

log = logging.getLogger("CONSUMER-LOG")
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_server,
)

log.info("#################### TOPICS ####################")
log.info(consumer.topics())
log.info("#################### CONFIGS ####################")
log.info(pprint.pformat(consumer.config))
log.info("#################### END ####################")

for message in consumer:
    print(message.value.decode("utf-8"))