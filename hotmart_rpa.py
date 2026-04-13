from playwright.sync_api import sync_playwright
import time 

with sync_playwright() as pw:
    nav = pw.chromium.launch(headless=False)

    page = nav.new_page()

    page.goto("https://sso.hotmart.com/login?systemOrigin=app-hotmart&service=https://app.hotmart.com/")
    
    try:
        page.get_by_role("button", name="OK")
    except Exception:
        print(Exception)


    page.get_by_role("textbox", name="Email").fill("")
    page.get_by_role("textbox", name="Password").fill("")
    page.locator("[data-test-id=\"login-submit\"]").click()

    time.sleep(10)
    nav.close()
