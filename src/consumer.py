from kafka import KafkaConsumer
import os
import pprint
from utils import parse, logger
from dotenv import load_dotenv


# load envars
load_dotenv()

logger = logger.getLogger()

bootstrap_server = os.environ.get("BOOTSTRAP_SERVER")
topic = os.environ.get("TOPIC")

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_server,
)

logger.info("#################### TOPICS ####################")
logger.info(consumer.topics())
logger.info("#################### CONFIGS ####################")
logger.info(pprint.pformat(consumer.config))
logger.info("#################### END ####################")


for message in consumer:
    to_print = parse.str_to_dict(message)
    logger.info(to_print)
