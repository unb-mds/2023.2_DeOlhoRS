import unittest
import os
import json
from Camada_Dados.Regex import Extrator_de_dados

class Test_extrator_de_dados(unittest.TestCase):
    def setUp(self):
        self.extrator = Extrator_de_dados()
        
    def test_escrita_database(self):
        # Criação do arquivo temporario na pasta geral do projeto
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        open(f'{caminho_atual}/testeRegex.json', 'w').close()
        with open(f'{caminho_atual}/testeRegex.json', 'w') as file:
            file.write("[\n\n]")
            
        dados_ficticios = {
            "nomeMunicipio": "nome_ficticio",
            "dataPost": "data_ficticia",
            "haNomeacao": "nomeacao_ficticia",
            "haExoneracao": "exoneracao_ficticia",      
        }
        self.extrator.escrita_data_base(dados_ficticios, f'{caminho_atual}/testeRegex.json')
        
        
        with open(f'{caminho_atual}/testeRegex.json', 'r') as arquivo:
            dados_lidos = json.load(arquivo)

        self.assertEqual(dados_lidos[0], dados_ficticios)
        os.remove(f'{caminho_atual}/testeRegex.json')
if __name__ == '__main__':
    unittest.main()