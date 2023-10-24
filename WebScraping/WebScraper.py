from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyPDF2 import PdfReader
import os 
import shutil
import time
import re



def extrair_pdf(arq):
    reader = PdfReader(arq)
    text = ""
    if arq.endswith(".pdf"):
        nova_extensao = "txt"
        nova_string = arq[:-3] + nova_extensao
        nome = nova_string

    arquivo = open(nome,'w')  

    # Itere pelas páginas do PDF
    for page in reader.pages:
        text += page.extract_text()

    #colocando no aquivo
    arquivo.write(text)
    arquivo.close()
# OBS: Tem de ser o path inteiro, não está reconhecendo o path reduzido.
def apaga_pdf(arq):
    os.remove(f'/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/{arq}')
    
def altera_diretorio():
    padrao = r"(\d{4})-(\d{2})-(\d{2})"
    # Alterar os diretórios caso seja usado por outro membro. #
    arquivos = os.listdir("/home/bdebatata/Downloads")
    caminho = "/home/bdebatata/Downloads"
    for arq in arquivos:
            correspondencia = re.findall(padrao, os.path.basename(arq))
            for match in correspondencia:
                ano, mes, dia = match  
                caminhoArq = os.path.join(caminho, arq)
                os.rename(caminhoArq, f'{ano}-{mes}-{dia}.pdf')
                print(os.path.basename(arq))
                return ano, mes, dia


driver = webdriver.Chrome()
driver.get("https://www.diariomunicipal.com.br/famurs/o-que-e")

# Acha o elemento que representa a box de seleção de ano e mês. 
calendar_month = driver.find_element(By.XPATH,"//*[@id='calendar_month']")
calendar_year = driver.find_element(By.XPATH,"//*[@id='calendar_year']")

# A seletora de ano e mês.
month_selector = Select(calendar_month)
year_selector = Select(calendar_year)

# Contador para o while
contador_ano = 2010 # Um ano antes de ter os primeiros diarios
contador_mes = 0 # um mês antes de ter os diario
contador_dia = 0 # um dia antes de ter os diarios

# Percorre o ano
while contador_ano <= 2023:
    contador_ano +=1
    if contador_ano >=2024:
        break
    calendar_year.click()
    time.sleep(2)
    contador_mes = 0
    year_selector.select_by_visible_text(str(contador_ano))
    # Percorre os Meses
    while contador_mes <= 12: 
        contador_mes+=1
        if contador_mes >= 13:
            break
        calendar_month.click()
        time.sleep(2)
        contador_dia = 0
        month_selector.select_by_value(str(contador_mes))
        calendar_month.click()
        # Percorre os dias 
        while contador_dia <= 31:
            contador_dia+=1
            if contador_dia >=32:
                break
            if (contador_mes == 4 or contador_mes == 6 or contador_mes == 9 or contador_mes == 11) and contador_dia > 30:
                break
            if contador_mes == 2 and contador_dia > 29 and (contador_ano == 2012 or contador_ano ==2016 or contador_ano ==2020):
                contador_dia = 32
            elif contador_mes == 2 and contador_dia > 28 and  (contador_ano !=2012 and contador_ano !=2016 and contador_ano !=2020):
                contador_dia = 32
            else:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.LINK_TEXT, str(contador_dia)))
                )
                
                PDF = driver.find_element(By.LINK_TEXT, str(contador_dia))
                PDF.click()
                time.sleep(2)
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
                        time.sleep(2)
                        anoPdf, mesPdf, diaPdf = altera_diretorio()
                        #extrair texto
                        extrair_pdf(f'{anoPdf}-{mesPdf}-{diaPdf}.pdf')
                        apaga_pdf(f'{anoPdf}-{mesPdf}-{diaPdf}.pdf')
                    if driver.find_element(By.XPATH, "//*[@id='containerDownloadNova']").get_attribute("style") == "display: block;" and driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekday ":
                       
                        element = WebDriverWait(driver, 20).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='btDownloadSimples2']"))
                                    )
                        PDF = driver.find_element(By.XPATH, "//*[@id='btDownloadSimples2']")
                        print(f'Edição: {contador_dia}/{contador_mes}/{contador_ano}')
    
                        PDF.click()
                        time.sleep(2)
                        anoPdf, mesPdf, diaPdf = altera_diretorio()
                        ## Extração de texto (PyPDF2)
                        extrair_pdf(f'{anoPdf}-{mesPdf}-{diaPdf}.pdf')
                        apaga_pdf(f'{anoPdf}-{mesPdf}-{diaPdf}.pdf')
                            
                element = WebDriverWait(driver, 20).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='popup']/div/article/a"))
                                    )
                driver.find_element(By.XPATH, "//*[@id='popup']/div/article/a").click()
               
driver.quit()


   