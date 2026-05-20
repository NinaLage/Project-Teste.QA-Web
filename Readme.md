Projeto Teste QA Web

-> Objetivo:

Esse projeto tem como objetivo validar a funcionalidade de pesquisa do blog https://blog.agibank.com.br/


-> Automação:

Foram Criados 03 Cenários de testes, onde foram validados:

. Busca Caixa alta

. Busca Caixa baixa

. Busca palavra incompleta


-> O script:

. Abre o navegador

. Acessa o site

. Localiza a lupa de pesquisa

. Digita o texto

. Executa a busca

. Valida resultados

. Salva os screenshots


-> Tecnologias Utilizadas:

. Python 3

. Selenium

. WebDriver Manager

. Google Chrome

. ChromeDriver

-> Bibliotecas Utilizadas (Necessário)

--> Selenium

Framework principal de automação web.

--> WebDriver Manager 

Responsável por baixar e gerenciar automaticamente o ChromeDriver.


# Instalação das Dependências

Abra o terminal ou PowerShell e execute:

```bash
pip install selenium webdriver-manager

