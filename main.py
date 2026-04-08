from playwright.sync_api import sync_playwright
import time


with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)


    time.sleep(4)
    navegador.close()