# util/logger.py
import logging
import os

log_dir = "logs"
log_file = os.path.join(log_dir, "cine.log")
log_format = "%(asctime)s - %(levelname)s - %(message)s"
filemode = "a"


def setup_logger() -> None:
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format=log_format,
        filemode=filemode
    )


logger = logging.getLogger(__name__)
