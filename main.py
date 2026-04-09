from playwright.sync_api import sync_playwright, expect
import time


with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)

    contexto = navegador.new_context()

    # Abrir nova página no navegador
    pagina = contexto.new_page()

    # Navegar para uma página
    pagina.goto("https://hashtagtreinamentos.com")

    # pegar informações da página
    # print(pagina.title())

    # Selecionar um elemento na tela
    # 1ª forma - Xpath
    # pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()

    #2ª forma - get_buy
    botao_quero_aprender = pagina.get_by_role("link", name="Quero aprender")

    with contexto.expect_page() as pagina2_info:
        botao_quero_aprender.click()

    # Como capturar mais de um elemento
    # links = pagina.get_by_role("link").all()
    # for link in links:
    #     print(link)

    # Criando uma nova página em branco
    # pagina2 = contexto.new_page()

    # nova página -> criar contextos e depois 
    pagina2 = pagina2_info.value
    pagina2.goto("https://hashtagtreinamentos.com/curso-python")

    # Inserindo no formulario
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill("joão")
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill("kmillakaua@gmail.com")
    pagina2.get_by_role("button", name="Quero acessar as informações").click()

    # Esperar um elemento na tela
    novo_butao = pagina2.get_by_role("link", name="quero garantir uma vaga")
    
    expect(novo_butao).to_be_visible()
    novo_butao.click()

    time.sleep(10)
    navegador.close()