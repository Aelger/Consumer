from kafka import KafkaConsumer
import os
import logging
import pprint
# import json
import base64

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

"""
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    value = json.loads(message.value.decode("utf-8"))
    log.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          value))
"""

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    decoded_value = message.value.decode('utf-8')
    decoded_payload = base64.b64decode(decoded_value['payload']['EMISECC'])
    log.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          decoded_payload))
