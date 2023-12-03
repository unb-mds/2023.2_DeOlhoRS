import unittest
from unittest.mock import patch, MagicMock
from selenium import webdriver
from Camada_Dados.WebScraper import Coletor_de_PDF
import os 
import shutil
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test_coletor_de_PDF(unittest.TestCase):
    def setUp(self):
        self.coletor = Coletor_de_PDF()

    def tearDown(self):
        self.coletor.encerrar_driver()
    
    
    def test_move_txt(self):

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Construa o caminho para um níveis acima
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        # Crie um arquivo fictício
        open(f'{caminho_atual}/arquivo1.txt', 'w').close()

        # Chame a função para mover o arquivo
        self.coletor.move_txt('testes')

        # Verifique se o arquivo foi movido para a pasta correta
        self.assertFalse(os.path.exists('arquivo1.txt'))  # Verifica se o arquivo original não existe mais
        self.assertTrue(os.path.exists(os.path.join(f'{caminho_atual}/Camada_Dados/txt/testes', 'arquivo1.txt')))  # Verifica se o arquivo foi movido para o destino esperado

    def test_apaga_pdf(self):
        # Crie um arquivo fictício
        open('arquivo.pdf', 'w').close()

        # Obtenha o diretório atual do arquivo de teste
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Construa o caminho para um níveis acima
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))

        # Mova o arquivo para o diretório acima
        shutil.move(os.path.join(diretorio_atual, 'arquivo.pdf'), os.path.join(caminho_atual, 'arquivo.pdf'))

        # Verifique se o arquivo foi movido com sucesso
        self.assertTrue(os.path.exists(os.path.join(caminho_atual, 'arquivo.pdf')))

        # Chame o método que você está testando
        self.coletor.apaga_pdf('arquivo.pdf')

        # Verifique se o arquivo foi removido
        self.assertFalse(os.path.exists(os.path.join(caminho_atual, 'arquivo.pdf')))

    def test_altera_diretorio(self):
        # Crie um arquivo fictício
        open('2023-01-01.pdf', 'w').close()
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        shutil.move(f'{diretorio_atual}/2023-01-01.pdf', caminho_downloads)
        
        # Execute o método altera_diretorio
        ano, mes, dia = self.coletor.altera_diretorio()

        self.assertEqual(ano, '2023')
        self.assertEqual(mes, '01')
        self.assertEqual(dia, '01')

    def test_roda_ano(self):
        ano_selecionado = self.coletor.roda_ano(2009, unitario=True)
        contador_ano = 2009
        self.assertEqual(ano_selecionado, str(contador_ano))

    def teste_roda_mes(self): 
        self.coletor.driver.get("https://www.diariomunicipal.com.br/famurs/o-que-e")
        self.coletor.iniciar_seletoras()
        mes_selecionado = self.coletor.roda_mes(2009, 0, self.coletor.month_selector, unitario=True)
        contador_mes = "Janeiro"
        self.assertEqual(mes_selecionado, contador_mes)
    
    def teste_roda_dia(self):
        self.coletor.driver.get("https://www.diariomunicipal.com.br/famurs/o-que-e")
        dia_selecionado = self.coletor.roda_dia(0, 1, 2009, unitario=True)
        contador_dia = 1
        self.assertEqual(dia_selecionado, contador_dia)


        
        
if __name__ == '__main__':
    unittest.main()