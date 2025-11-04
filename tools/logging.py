import logging
import sys

class Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)5s - %(message)s",
        encoding="UTF-8",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)