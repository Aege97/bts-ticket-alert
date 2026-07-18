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
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-dev-shm-usage"
                ]
            )

            page = browser.new_page()

            print("🌐 Abriendo Ticketmaster...")

            page.goto(
                EVENT_URL,
                wait_until="networkidle",
                timeout=60000
            )

            page.wait_for_timeout(8000)

            html = page.content()
            text = page.locator("body").inner_text()

            with open("pagina.html", "w", encoding="utf-8") as f:
                f.write(html)

            with open("ultimo_texto.txt", "w", encoding="utf-8") as f:
                f.write(text)

            print("=" * 40)
            print(text[:1000])
            print("=" * 40)

            browser.close()

            return Status.SOLD_OUT

    except Exception as e:
        print("❌ ERROR EN TICKETMASTER:", e)
        return Status.ERROR