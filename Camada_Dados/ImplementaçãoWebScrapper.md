# Implementação WebScrapper

## Introdução 
Uma das etapas iniciais para o desenvolvimento desse projeto é a disposição dos Diarios Oficiais, os arquivos PDF's de cada dia são dispostos no site dos Diarios Oficiais dos Municípios do Rio Grande do Sul, no caso desse estado se tem diarios desde 2009 até o atual ano. Obter esses arquivos manualmente é possível, porém é um processo de acessar cada dia, de cada mês em cada ano e verificar a existência de um arquivo para aquele dia e se sim baixá-lo, o que é extremamente desgastante e passível de erro. Por conta disso, o processo de obtenção de cada um dos PDF's será feito por um bot.

## Metodologia

Utilizando do Python e algumas bibliotecas, no qual se destaca a biblioteca Selenium, é possível programar um bot que simule os cliques de um usuário no site. Dessa forma mapeando o caminho que o usuário deveria tomar para acessar cada um destes arquivos manualmente é passado como comandos para o computador que os realizará de forma automática. 

## Programação
Primeiramente é necessário realizar alguns imports que serão necessários para o código:

~~~python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os 
import shutil
import time
import re
~~~
Após os imports é escolhido o navegador que será usado para realizar essas operações e acoplado o link do site. 

~~~python
driver = webdriver.Chrome()
driver.get("https://www.diariomunicipal.com.br/famurs/o-que-e")
~~~

Quando analisado o site é perceptivel que é possível clicar no dia para acessar uma página com seu respectivo PDF, mas o mês e o ano devem ser selecionados numa barra acima. Conseguindo o xpath das seletoras de ano e mês é possível simular o acesso a um mês ou ano específico com o Select.

~~~python
calendar_month = driver.find_element(By.XPATH,"//*[@id='calendar_month']")
calendar_year = driver.find_element(By.XPATH,"//*[@id='calendar_year']")

month_selector = Select(calendar_month)
year_selector = Select(calendar_year)
~~~

Após isso foi realizado 3 loopings para a passagem de todos os anos, meses e dias, por isso há um contador para cada. Em cada uma das iterações de dia é acionado pela xpath de um dia correspondente ao contador e então é dado um .click() no elemento, o que abre um popup que contém o arquivo que então é selecionado e começa o download na máquina que está executando o código.
Em cada trecho é verificado a existência do bloco de download e se ele existe, se é do tipo simples ou simples2, seguindo de acordo com as inspeções feitas no código do site.
WebDriverWait é um comando para melhor experiência com possíveis delays, já que pode-se inserir um tempo que o código vai esperar para alguma tela ou ação acontecer no site e caso ela aconteca ele ignora o tempo e prossegue o código. 
~~~python 
if driver.find_element(By.XPATH, "//*[@id='materia-aviso']").get_attribute("style") == "display: block;" or driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekend ":
    print(f'Não tem matéria pra esse dia: {contador_dia}/{contador_mes}/{contador_ano}')
else:
    if driver.find_element(By.XPATH, "//*[@id='containerDownload']").get_attribute("style") == "display: block;" and driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekday ":

        element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='btDownloadSimples']"))
                                    )
        PDF = driver.find_element(By.XPATH, "//*[@id='btDownloadSimples']")
        print(f'Edição: {contador_dia}/{contador_mes}/{contador_ano}')
                        
        PDF.click()
    if driver.find_element(By.XPATH, "//*[@id='containerDownloadNova']").get_attribute("style") == "display: block;" and driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekday "    
        element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='btDownloadSimples2']"))
                                    )
        PDF = driver.find_element(By.XPATH, "//*[@id='btDownloadSimples2']")
        print(f'Edição: {contador_dia}/{contador_mes}/{contador_ano}')     
        PDF.click()
~~~

Ao final, o driver fecha e se inicia outro processo importante para essa etapa, que é a padronização desses documentos para que seja melhor sua manipulação, no código abaixo a variavél arquivos recebe uma lista com todos os documentos na pasta de download e então para cada arquivo ali contido ele usa de um processo de busca por regular expression (Regex), procurando o padrão de 4 digitos-2digitos-2digitos, que corresponde no nome do arquivo a sua data. Então é trocado o nome de cada um para sua data e então printado a data.
~~~python
padrao = r"(\d{4})-(\d{2})-(\d{2})"
arquivos = os.listdir("diretório padrão dos downloads do computador que executar")
caminho = "diretório padrão dos downloads do computador que executar"
for arq in arquivos:
        correspondencia = re.findall(padrao, os.path.basename(arq))
        for match in correspondencia:
            ano, mes, dia = match  
            caminhoArq = os.path.join(caminho, arq)
            os.rename(caminhoArq, f'{ano}-{mes}-{dia}.pdf')
            print(os.path.basename(arq))
~~~
Como já descrito acima, os documentos estavam na pasta de downloads, quando renomeados eles são trazidos para a pasta geral do projeto, para organizar isso o código abaixo pesquisa para cada arquivo na pasta geral e que terminam em .pdf para então traze-los a uma pasta específica do projeto. 
~~~python
for docs in os.listdir("Pasta geral do Projeto"):
    if docs.endswith(".pdf"):
        caminhoAtual = os.path.join("Pasta geral do Projeto", docs)
        caminhoDestino = os.path.join("Pasta específica do projeto", docs)
        shutil.move(caminhoAtual, caminhoDestino)
~~~

## Referências 
> 1. Documentação da biblioteca Selenium (Documentação não oficial): https://selenium-python.readthedocs.io/. 
> 2. Documentação Python/OS: https://docs.python.org/pt-br/3/library/os.html
> 3. Documentação Python/re: https://docs.python.org/pt-br/3/library/re.html
> 4. Documentação Python/shutil: https://docs.python.org/pt-br/3/library/shutil.html

Acessos: As documentações citadas acima foram acessadas durante maior parte dos dias da semana que compreende a Sprint 3 (25/09 a 02/10).