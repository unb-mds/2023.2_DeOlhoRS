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
    def test_estrair_nome_municipio_final(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        arq_path = f'{caminho_atual}/Camada_Dados/txt/testes/2030-12-30.txt'
        with open(arq_path) as file:
            texto = file.read()
        print(texto)
        self.assertEqual(self.extrator.extrair_nome_municipio(texto), "Ibirubá")
        os.remove(f'{caminho_atual}/teste_extracao.json')
    
        
    def test_extrair_dados_nomeacao(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        arq_path = f'{caminho_atual}/Camada_Dados/txt/testes/2030-12-30.txt'
        open(f'{caminho_atual}/teste_extracao.json', 'w').close()
        with open(f'{caminho_atual}/teste_extracao.json', 'w') as file:
            file.write("[\n\n]")
        self.extrator.extrair_dados(arq_path, f'{caminho_atual}/teste_extracao.json')
        
        dados_esperados = {
            "nomeMunicipio": "Ibirubá",
            "dataPost": "2030-12-30",
            "haNomeacao": True,
            "haExoneracao": False
        }
        
        with open(f'{caminho_atual}/teste_extracao.json', 'r') as arquivo:
            dados_lidos = json.load(arquivo)
        
        self.assertEqual(dados_lidos[0], dados_esperados)
        os.remove(f'{caminho_atual}/teste_extracao.json')
        
    def test_extrair_dados_exoneracao(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        arq_path = f'{caminho_atual}/Camada_Dados/txt/testes/2030-12-31.txt'
        open(f'{caminho_atual}/teste_extracao.json', 'w').close()
        with open(f'{caminho_atual}/teste_extracao.json', 'w') as file:
            file.write("[\n\n]")
        self.extrator.extrair_dados(arq_path, f'{caminho_atual}/teste_extracao.json')
        
        dados_esperados = {
            "nomeMunicipio": "Travesseiro",
            "dataPost": "2030-12-31",
            "haNomeacao": False,
            "haExoneracao": True
        }
        
        with open(f'{caminho_atual}/teste_extracao.json', 'r') as arquivo:
            dados_lidos = json.load(arquivo)
        
        self.assertEqual(dados_lidos[0], dados_esperados)
        os.remove(f'{caminho_atual}/teste_extracao.json')
        
    def test_extrair_geral(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_atual = os.path.abspath(os.path.join(diretorio_atual, '..'))
        
        open(f'{caminho_atual}/teste_extracao.json', 'w').close()
        with open(f'{caminho_atual}/teste_extracao.json', 'w') as file:
            file.write("[\n\n]")
            
        self.extrator.extrai_geral(ano_extraido="testes", arq_salvo= f'{caminho_atual}/teste_extracao.json')

        dados_esperados_nomeacao = {
                "nomeMunicipio": "Ibirubá",
                "dataPost": "2030-12-30",
                "haNomeacao": True,
                "haExoneracao": False
            }
        dados_esperados_exoneracao = {
                "nomeMunicipio": "Travesseiro",
                "dataPost": "2030-12-31",
                "haNomeacao": False,
                "haExoneracao": True
            }
        with open(f'{caminho_atual}/teste_extracao.json') as arquivo:
            dados = json.load(arquivo)
        self.assertEqual(dados_esperados_nomeacao, dados[0])
        self.assertEqual(dados_esperados_exoneracao, dados[1])
        os.remove(f'{caminho_atual}/teste_extracao.json')
if __name__ == '__main__':
    unittest.main()