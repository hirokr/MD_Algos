import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)

def log_info(message: str) -> None:
    logging.info(message)