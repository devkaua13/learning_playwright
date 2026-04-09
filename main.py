from playwright.sync_api import sync_playwright
import time


with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    # Abrir o navegador
    pagina = navegador.new_page()

    # Navegar para uma página
    pagina.goto("https://hashtagtreinamentos.com")

    # pegar informações da página
    print(pagina.title())

    # Selecionar um elemento na tela
    # 1ª forma - Xpath
    # pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()

    #2ª forma - get_buy
    pagina.get_by_role("link", name="Quero aprender").click()

    time.sleep(4)
    navegador.close()