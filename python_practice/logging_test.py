import logging

logging.basicConfig(filename="my_err.log", format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
logging.disable(level=logging.INFO)
logging.info("email sent")

try:
    1/0
except Exception as e:
    logging.error(e)
