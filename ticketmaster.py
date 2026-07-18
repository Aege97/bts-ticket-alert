from enum import Enum
from playwright.sync_api import sync_playwright
from config import EVENT_URL


class Status(Enum):
    AVAILABLE = "available"
    SOLD_OUT = "sold_out"
    ERROR = "error"


def check_availability():
    print("\n🔥 ===== TICKETMASTER VERSION 3 ===== 🔥\n")

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

            page.goto(
                EVENT_URL,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            page.wait_for_timeout(10000)

            print(f"📍 URL FINAL: {page.url}")
            print(f"📄 TÍTULO: {page.title()}")

            html = page.content()

            print("\n========== PRIMEROS 2000 CARACTERES DEL HTML ==========\n")
            print(html[:2000])
            print("\n========== FIN HTML ==========\n")

            browser.close()

            return Status.SOLD_OUT

    except Exception as e:
        print("❌ ERROR:", e)
        return Status.ERROR