from enum import Enum
from playwright.sync_api import sync_playwright
from config import EVENT_URL


class Status(Enum):
    AVAILABLE = "available"
    SOLD_OUT = "sold_out"
    ERROR = "error"


def check_availability():
    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            print("🌐 Abriendo Ticketmaster...")

            page.goto(
                EVENT_URL,
                wait_until="domcontentloaded",
                timeout=30000
            )

            page.wait_for_timeout(8000)

            text = page.locator("body").inner_text().upper()

            with open("ultimo_texto.txt", "w", encoding="utf-8") as f:
                f.write(text)

            contiene_agotado = "AGOTADO" in text

            print("========================================")
            print("¿Contiene AGOTADO?:", contiene_agotado)
            print("========================================")

            browser.close()

            if contiene_agotado:
                print("➡️ DEVOLVIENDO Status.SOLD_OUT")
                return Status.SOLD_OUT

            print("➡️ DEVOLVIENDO Status.AVAILABLE")
            return Status.AVAILABLE

    except Exception as e:

        print("❌ ERROR EN TICKETMASTER:", e)

        return Status.ERROR