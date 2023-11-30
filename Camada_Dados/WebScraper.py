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



class Coletor_de_PDF:

    def __init__(self):
        self.driver = None
        self.iniciar_driver()
    
        
    def iniciar_driver(self):
        self.driver = webdriver.Chrome()
        
        
    def iniciar_seletoras(self):
        self.calendar_month = self.driver.find_element(By.XPATH,"//*[@id='calendar_month']")
        self.calendar_year = self.driver.find_element(By.XPATH,"//*[@id='calendar_year']")
        self.month_selector = Select(self.calendar_month)
        self.year_selector = Select(self.calendar_year)

    def encerrar_driver(self):
        if self.driver:
            self.driver.quit()

    def extrair_pdf(self, arq):
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

    def apaga_pdf(self, arq):
    # diretorio atual = /squad08/camada_dados
       diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    # caminho atual = /squad08/
       caminho_atual = os.path.dirname(diretorio_atual)
       os.remove(f'{caminho_atual}/{arq}')
        
    def altera_diretorio(self):
        padrao = r"(\d{4})-(\d{2})-(\d{2})"
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        arquivos = os.listdir(f"{caminho_downloads}")
        for arq in arquivos:
                correspondencia = re.findall(padrao, os.path.basename(arq))
                for match in correspondencia:
                    ano, mes, dia = match  
                    caminhoArq = os.path.join(caminho_downloads, arq)
                    os.rename(caminhoArq, f'{ano}-{mes}-{dia}.pdf')
                    print(os.path.basename(arq))
                    return ano, mes, dia
                
    def move_txt(self, ano):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_origem = os.path.dirname(diretorio_atual)
        pasta_destino = f'{diretorio_atual}/txt/{ano}/'
        arquivos_txt = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.endswith('.txt')]
        for arq in arquivos_txt:
            origem_arquivo = os.path.join(pasta_origem, arq)
            destino_arquivo = os.path.join(pasta_destino, arq)
            shutil.move(origem_arquivo, destino_arquivo)
            
    def coleta_pdf(self, ano_inicial, ano_final=2023):
        self.roda_ano(ano_inicial, ano_final)

    def roda_ano(self, ano_inicial, ano_final=2023, unitario=False):
        contador_ano = ano_inicial-1
        contador_mes = 0
        self.driver.get("https://www.diariomunicipal.com.br/famurs/o-que-e")
        
        self.iniciar_seletoras()
    
        # Percorre o ano
        while contador_ano <= ano_final:
            contador_ano +=1
            if contador_ano >=ano_final:
                break
            self.calendar_year.click()
            time.sleep(2)
            self.year_selector.select_by_visible_text(str(contador_ano))

            # Usado para os testes
            ano_selecionado = self.year_selector.first_selected_option.text

            if unitario == True:
                print(ano_selecionado)
                self.encerrar_driver()
                return ano_selecionado
                
            else:
                self.roda_mes(contador_ano, contador_mes, self.month_selector)
        # Fecha o Driver após todas as iterações
        self.driver.quit()
   
    def roda_mes(self, contador_ano, contador_mes, month_selector, unitario = False):
    
        while contador_mes <= 12: 
            contador_mes+=1
            if contador_mes >= 13:
                break
            self.calendar_month.click()
            time.sleep(2)
            contador_dia = 0
            month_selector.select_by_value(str(contador_mes))
            self.calendar_month.click()
            
            mes_selecionado = self.month_selector.first_selected_option.text
            # Percorre os dias 
            if unitario == True:
                print(mes_selecionado)
                self.encerrar_driver()
                return mes_selecionado
            self.roda_dia(contador_dia, contador_mes, contador_ano)
            
    def roda_dia(self, contador_dia, contador_mes, contador_ano, unitario = False):
        while contador_dia <= 31:
            contador_dia+=1
            if contador_dia >=32:
                break
            if (contador_mes in [4, 6, 9, 11] and contador_dia > 30) or (contador_mes == 2 and contador_dia > 29 and (contador_ano % 4 == 0 and (contador_ano % 100 != 0 or contador_ano % 400 == 0))) or (contador_mes == 2 and contador_dia > 28 and not (contador_ano % 4 == 0 and (contador_ano % 100 != 0 or contador_ano % 400 == 0))):
                contador_dia = 32
            else:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.LINK_TEXT, str(contador_dia)))
                )
                
                PDF = self.driver.find_element(By.LINK_TEXT, str(contador_dia))
                PDF.click()
                time.sleep(2)
                if self.driver.find_element(By.XPATH, "//*[@id='materia-aviso']").get_attribute("style") == "display: block;" or self.driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekend ":
                    print(f'Não tem matéria pra esse dia: {contador_dia}/{contador_mes}/{contador_ano}')
                else:
                    if self.driver.find_element(By.XPATH, "//*[@id='containerDownload']").get_attribute("style") == "display: block;" and self.driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekday ":

                        WebDriverWait(self.driver, 20).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='btDownloadSimples']"))
                                    )
                        PDF = self.driver.find_element(By.XPATH, "//*[@id='btDownloadSimples']")
                        print(f'Edição: {contador_dia}/{contador_mes}/{contador_ano}')
                        if unitario == True:
                            return f'{contador_dia}/{contador_mes}/{contador_ano}'
                        else:
                            PDF.click()
                            time.sleep(2)
                            ano_pdf, mes_pdf, dia_pdf = self.altera_diretorio()
                            #extrair texto
                            self.extrair_pdf(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.pdf')
                            self.apaga_pdf(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.pdf')
                            self.move_txt(ano_pdf)
                        #regex.extrairDados(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.txt')

                    if self.driver.find_element(By.XPATH, "//*[@id='containerDownloadNova']").get_attribute("style") == "display: block;" and self.driver.find_element(By.LINK_TEXT, str(contador_dia)).find_element(By.XPATH, './ancestor::td').get_attribute("class") == "weekday ":
                    
                        WebDriverWait(self.driver, 20).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='btDownloadSimples2']"))
                                    )
                        PDF = self.driver.find_element(By.XPATH, "//*[@id='btDownloadSimples2']")
                        print(f'Edição: {contador_dia}/{contador_mes}/{contador_ano}')
                        if unitario == True:
                            return f'{contador_dia}/{contador_mes}/{contador_ano}'
                        else:
                            PDF.click()
                            time.sleep(2)
                            ano_pdf, mes_pdf, dia_pdf = self.altera_diretorio()
                            ## Extração de texto (PyPDF2)
                            self.extrair_pdf(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.pdf')
                            self.apaga_pdf(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.pdf')
                            self.move_txt(ano_pdf)
                        #regex.extrairDados(f'{ano_pdf}-{mes_pdf}-{dia_pdf}.txt')
                        
                WebDriverWait(self.driver, 40).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@id='popup']/div/article/a"))
                                    )
                self.driver.find_element(By.XPATH, "//*[@id='popup']/div/article/a").click()
 
