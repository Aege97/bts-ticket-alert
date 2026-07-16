import random
import time
from datetime import datetime

from ticketmaster import check_availability, Status
from telegram_service import send_message
from state import load_state, save_state
from config import CHECK_INTERVAL_MIN, CHECK_INTERVAL_MAX


def start():

    print("🤖 Ticket Sentinel iniciado\n")

    while True:

        now = datetime.now().strftime("%H:%M:%S")

        print(f"[{now}] Revisando Ticketmaster...")

        status = check_availability()

        print("📌 Status recibido:", status)

        previous = load_state()["available"]

        print("📌 Estado guardado:", previous)

        if status == Status.ERROR:

            print("⚠️ Error cargando Ticketmaster.\n")

        elif status == Status.SOLD_OUT:

            print("❌ Sigue agotado.\n")

            save_state(False)

        elif status == Status.AVAILABLE:

            if not previous:

                print("🚨 CAMBIO DETECTADO")

                send_message(
                    "🚨 ¡POSIBLE DISPONIBILIDAD!\n\nhttps://www.ticketmaster.co/event/bts-world-tour-2026"
                )

                save_state(True)

            else:

                print("✅ Sigue disponible.\n")

        wait = random.randint(
            CHECK_INTERVAL_MIN,
            CHECK_INTERVAL_MAX
        )

        print(f"⏳ Esperando {wait} segundos...\n")

        time.sleep(wait)