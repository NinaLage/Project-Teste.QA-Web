
# test_pesquisa_blogdoagi.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import traceback


# Dados e Pastas Blog

URL = "https://blog.agibank.com.br/"

PASTA_SCREENSHOTS = "screenshots"

if not os.path.exists(PASTA_SCREENSHOTS):
    os.makedirs(PASTA_SCREENSHOTS)


# Navegador 

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


# Driver

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 30)


# Pesquisa


def executar_pesquisa(texto_pesquisa, nome_teste):

    try:

        print("\n=================================================")
        print(f"Executando teste: {nome_teste}")
        print("=================================================")

        
        # Step 1 - Abrir navegador
        

        driver.get("about:blank")

        print("1. Navegador aberto em branco")

        time.sleep(2)

        
        # Step 2 - Informar URL
    

        driver.get(URL)

        print(f"2. URL acessada: {URL}")

        # Aguarda carregamento
        time.sleep(5)

        
        # Step 3 - Cehcar URL correta
        

        if "blog.agibank.com.br" in driver.current_url:

            print("3. URL carregada com sucesso")

        else:

            print("3. Erro ao carregar URL")

        
        # Step 4 - Clicar na Lupa para pesquisa
        

        possiveis_botoes = [
            'button[aria-label*="Busca"]',
            'button[aria-label*="Pesquisar"]',
            '.search-toggle',
            '.search-button',
            'button[class*="search"]',
            'a[class*="search"]'
        ]

        btn_lupa = None

        for seletor in possiveis_botoes:

            elementos = driver.find_elements(
                By.CSS_SELECTOR,
                seletor
            )

            if elementos:

                for elemento in elementos:

                    try:

                        if elemento.is_displayed():

                            btn_lupa = elemento

                            print(f"Botão encontrado: {seletor}")

                            break

                    except:
                        pass

            if btn_lupa:
                break

        if not btn_lupa:

            raise Exception(
                "Botão da busca não encontrado"
            )

        # Scroll até botão
        driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            btn_lupa
        )

        time.sleep(1)

        # Clique via JavaScript
        driver.execute_script(
            "arguments[0].click();",
            btn_lupa
        )

        print("4. Campo pesquisa aberto")

        # Screenshot debug
        driver.save_screenshot(
            os.path.join(
                PASTA_SCREENSHOTS,
                f"{nome_teste}_debug_lupa.png"
            )
        )

        
        # Step 5 - Campo Busca localizado
    

        time.sleep(3)

        possiveis_campos = [
            'input[type="search"]',
            'input[name="s"]',
            'input[name="search"]',
            'input[placeholder*="Busca"]',
            'input[placeholder*="Pesquisar"]',
            '.search-field',
            '.search-input'
        ]

        campo_busca = None

        for seletor in possiveis_campos:

            elementos = driver.find_elements(
                By.CSS_SELECTOR,
                seletor
            )

            if elementos:

                for elemento in elementos:

                    try:

                        if elemento.is_displayed():

                            campo_busca = elemento

                            print(f"Campo encontrado: {seletor}")

                            break

                    except:
                        pass

            if campo_busca:
                break

        if not campo_busca:

            print("\nINPUTS ENCONTRADOS:\n")

            inputs = driver.find_elements(By.TAG_NAME, "input")

            for i in inputs:

                try:
                    print(i.get_attribute("outerHTML"))
                except:
                    pass

            raise Exception(
                "Campo de busca não encontrado"
            )

        
        # Step 6 - Digitar palavra para pesquisa
    

        campo_busca.clear()

        campo_busca.send_keys(texto_pesquisa)

        print(f'5. Texto digitado: "{texto_pesquisa}"')

        time.sleep(1)

        campo_busca.send_keys(Keys.ENTER)

        print("6. ENTER realizado")

        # Aguarda resultados
        time.sleep(5)

        
        # Step 7 - Resultados
        

        body = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        if "INSS" in body.upper():

            print("Resultado encontrado com sucesso")

        else:

            print("Resultado NÃO encontrado")

        
        # Step 8 - Captura Evidencia Final 
        

        nome_arquivo = os.path.join(
            PASTA_SCREENSHOTS,
            f"{nome_teste}.png"
        )

        driver.save_screenshot(nome_arquivo)

        print(f"Screenshot salvo: {nome_arquivo}")

    except Exception:

        print("\nERRO DETALHADO:")
        traceback.print_exc()

try:

    
    # Caso de Teste 1.1 - CAIXA ALTA
    

    executar_pesquisa(
        texto_pesquisa="INSS",
        nome_teste="cenario_1_1_caixa_alta"
    )

    
    # Caso de Teste  1.2 - CAIXA BAIXA
    

    executar_pesquisa(
        texto_pesquisa="inss",
        nome_teste="cenario_1_2_caixa_baixa"
    )

    
    # Caso de Teste 1.3 - PALAVRA INCOMPLETA


    executar_pesquisa(
        texto_pesquisa="ins",
        nome_teste="cenario_1_3_palavra_incompleta"
    )

finally:

    print("\nFinalizando navegador...")

    time.sleep(3)

    driver.quit()