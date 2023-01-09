from kafka import KafkaConsumer
import pprint
import logging
#import os

log = logging.getLogger("my-logger")
logging.basicConfig(level=logging.INFO)

#topic = os.environ.get("TOPIC")
#bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")


consumer = KafkaConsumer("postgres-jdbc-football_players",bootstrap_servers='host.docker.internal:19092')
log.info("TOPIC SUSCRIBED", consumer.topics())
print("TOPIC SUSCRIBED", consumer.topics())

log.info("#################### CONFIGS ####################")
print("#################### CONFIGS ####################")
log.info(consumer.config)
pprint.pprint(consumer.config)
log.info("#################### END ####################")
print("#################### END ####################")

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    log.info(message)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
