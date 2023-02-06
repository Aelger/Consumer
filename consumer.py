from kafka import KafkaConsumer
import logging
import pprint
import json
import os
import base64
import decimal


log = logging.getLogger("CONSUMER-LOG")
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

topic = os.environ.get("TOPIC")
bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_server,
    group_id="my-group-id",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
)

log.info("#################### TOPICS ####################")
log.info(consumer.topics())
log.info("#################### CONFIGS ####################")
log.info(pprint.pformat(consumer.config))
log.info("#################### END ####################")


for message in consumer:
    payload = message.value["payload"]
    decoded_payload = {}
    for k, v in payload.items():
        v = str(v)
        if len(v) < 13:
            decoded_string = base64.b64decode(v).decode("utf-8")
            try:
                decoded_payload[k] = decimal.Decimal(decoded_string)
            except decimal.InvalidOperation:
            # Handle the error
                decoded_payload[k] = None
    print(
        f"Received message: topic={message.topic}, partition={message.partition}, offset={message.offset}, value={decoded_payload}"
    )
