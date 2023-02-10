import logging

def getLogger():
    log = logging.getLogger("CONSUMER-LOG")
    logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    )

    return log