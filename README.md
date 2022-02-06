# Desafio RPA BWA 🚀 

## Começando

Essas instruções permitirão baixar e rodar a solução para o rpa challenge em um ambiente virutal em sua máquina. 

### 📋 Pré-requisitos

Os testes foram executados com as seguintes ferramentas nas seguintes versões:

* Google Chrome 98.0.4758.82 (Versão oficial) 64 bits
* Python 3.9.5

### 🔧 Instalação e criação de um ambiente virtual
Instalando o ambiente virtual(virtualenv):

1. Abrir o prompt de comando do windows
2. colar o comando: pip install virtualenv
   * se o pip não for localizado mesmo com python instalado verifique a possível solução [aqui](https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/)

3. Digitar o comando: cd caminho_onde_se_encontra_os_arquivos_baixados_aqui_no_git
   * Exemplo de comando anterior: cd C:\Users\jeffe\Desktop\rpachallenge\challenge
4. colar o seguinte comando: virtualenv criar_nome_para_o_ambiente
   * exemplo do comando anterior: virtualenv ambiente_bwa1

### ⌨️ Iniciando o ambiente virtual e iniciando o programa
1. Abrir o prompt de comando do windows
2. Digitar o comando: cd caminho_onde_se_encontra_os_arquivos_baixados_aqui_no_git
   * Exemplo de comando anterior: cd C:\Users\jeffe\Desktop\rpachallenge\challenge
3. Colar o seguinte comando: nome_do_seu_ambiente\Scripts\activate.bat
   * Exemplo de comando anterior: ambiente_bwa1\Scripts\activate.bat
5. Colar os seguintes comandos um por vez:
    * pip install selenium
    * pip install pandas
    * pip install webdriver_manager
    * pip install openpyxl
5. colar o comando: teste.py
* Após essa sequencia o navegador será iniciado automaticamente e os formulários serão preenchidos 

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação usada
* [Pandas](https://pypi.org/project/pandas/) - Biblioteca que gerencia as planilhas
* [Selenium](https://selenium-python.readthedocs.io/index.html) - ferramenta para automatizar o preenchimento dos forms
