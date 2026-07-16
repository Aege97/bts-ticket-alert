from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
EVENT_URL = os.getenv("EVENT_URL")

CHECK_INTERVAL_MIN = int(os.getenv("CHECK_INTERVAL_MIN", 20))
CHECK_INTERVAL_MAX = int(os.getenv("CHECK_INTERVAL_MAX", 40))