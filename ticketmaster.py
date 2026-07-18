from enum import Enum
from playwright.sync_api import sync_playwright
from config import EVENT_URL


class Status(Enum):
    AVAILABLE = "available"
    SOLD_OUT = "sold_out"
    ERROR = "error"


def check_availability():
    print("\n🔥 ===== TICKETMASTER VERSION 2 ===== 🔥\n")

    try:
        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                ],
            )

            page = browser.new_page()

            print("🌐 Abriendo Ticketmaster... VERSION 2")

            page.goto(
                EVENT_URL,
                wait_until="networkidle",
                timeout=60000,
            )

            page.wait_for_timeout(8000)

            html = page.content()
            text = page.locator("body").inner_text()

            print("\n========== PRIMEROS 1000 CARACTERES ==========\n")
            print(text[:1000])
            print("\n========== FIN ==========\n")

            with open("pagina.html", "w", encoding="utf-8") as f:
                f.write(html)

            with open("ultimo_texto.txt", "w", encoding="utf-8") as f:
                f.write(text)

            browser.close()

            print("⚠️ DEVOLVIENDO SOLD_OUT SOLO PARA PRUEBAS")

            return Status.SOLD_OUT

    except Exception as e:
        print("\n❌ ERROR EN TICKETMASTER")
        print(e)
        return Status.ERROR