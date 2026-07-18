import logging
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "ticketbot.log")

os.makedirs(LOG_FOLDER, exist_ok=True)

logger = logging.getLogger("TicketSentinel")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

if not logger.handlers:

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file)