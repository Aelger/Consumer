from kafka import KafkaConsumer
import logging
import pprint
import os
import json

log = logging.getLogger("CONSUMER-LOG")
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")


consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server)


log.info("#################### TOPICS ####################")
log.info(consumer.topics())
log.info("#################### CONFIGS ####################")
log.info(pprint.pformat(consumer.config))
log.info("#################### END ####################")
print("VAMOS BOCA!")


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    try:
        record = json.loads(message.value.decode('utf-8'))
        print(record)
    except:
        print("Error al decodificar el mensaje")