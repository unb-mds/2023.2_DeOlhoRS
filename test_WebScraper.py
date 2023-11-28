import unittest
from unittest.mock import patch, MagicMock
from selenium import webdriver
from WebScraping.WebScraper import ColetorDePDF
import os 

class TestColetorDePDF(unittest.TestCase):
    def setUp(self):
        self.coletor = ColetorDePDF()

    def tearDown(self):
        self.coletor.encerrar_driver()


    def test_move_txt(self):
            # Crie uma pasta fictícia
            #os.makedirs('txt/2023', exist_ok=True)

            # Crie um arquivo fictício
            open('arquivo1.txt', 'w').close()

            self.coletor.moveTxt('testes')

            # Verifique se o arquivo foi movido para a pasta correta
            self.assertFalse(os.path.exists('arquivo.txt'))
            self.assertTrue(os.path.exists('WebScraping/txt/testes/arquivo.txt'))

    def test_apaga_pdf(self):
        # Crie um arquivo fictício
        open('arquivo.pdf', 'w').close()

        self.assertTrue(os.path.exists('arquivo.pdf'))

        self.coletor.apaga_pdf('arquivo.pdf')

        # Verifique se o arquivo foi removido
        self.assertFalse(os.path.exists('arquivo.pdf'))

'''    def test_altera_diretorio(self):
        # Crie um arquivo fictício
        open('2023-01-01.pdf', 'w').close()

        # Execute o método altera_diretorio
        ano, mes, dia = self.coletor.altera_diretorio()

        self.assertEqual(ano, '2023')
        self.assertEqual(mes, '01')
        self.assertEqual(dia, '01')
'''
    

    

if __name__ == '__main__':
    unittest.main()