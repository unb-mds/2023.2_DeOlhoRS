import unittest
import os
import json

from Camada_Dados.extrair import OrganizadorDeDados



class TestOrganizadorDeDados(unittest.TestCase):

    def test_processar_dados(self):
        dados_municipios = [
            {"nomeMunicipio": "Municipio1", "dataPost": "2022-01-01", "haNomeacao": 1, "haExoneracao": 0},
            {"nomeMunicipio": "Municipio2", "dataPost": "2022-01-01", "haNomeacao": 0, "haExoneracao": 1},
            
        ]

        input_file = 'input_test.json'
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(dados_municipios, f, indent=2, ensure_ascii=False)

        output_file = 'output_test.json'

        organizador = OrganizadorDeDados()
        organizador.processar_dados(input_file, output_file)

        with open(output_file, 'r', encoding='utf-8') as f:
            dados_grafico = json.load(f)

        self.assertEqual(len(dados_grafico), len(dados_municipios))

        #Linhas para romover os arquivos criados
        os.remove(input_file)
        os.remove(output_file)

    def test_processar_anos(self):
        sua_instancia = OrganizadorDeDados()

        # Criar dados de entrada para o teste
        input_file = 'arquivo_de_entrada.json'
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump([
                {"municipio": "BOA VISTA DO CADEADO","ano": "2009","mes": "07","nomeacoes": 2,"exoneracoes": 2},
                {"municipio": "boa vista do cadeado","ano": "2009","mes": "06","nomeacoes": 10,"exoneracoes": 12},
                {"municipio": "Ibirubá","ano": "2009","mes": "07","nomeacoes": 10,"exoneracoes": 4},
                {"municipio": "Ibirubá","ano": "2009","mes": "10","nomeacoes": 11,"exoneracoes": 19},
            ], f)

        output_file = 'arquivo_de_comparacao.json'
        sua_instancia.processar_anos(input_file, output_file)

        # Carregar o arquivo de saída gerado pelo método
        
        with open(output_file, 'r', encoding='utf-8') as f:
            resultado = json.load(f)

        # Definir o resultado esperado com base nos dados de entrada
        resultado_esperado = [
                {
                    "municipio": "boa vista do cadeado",
                    "nomeacoes": 12,
                    "exoneracoes": 14
                },
                {
                    "municipio": "ibirubá",
                    "nomeacoes": 21,
                    "exoneracoes": 23
                }
        ]

        # Comparar o resultado real com o resultado esperado
        self.assertEqual(resultado, resultado_esperado)

        #Linhas para romover os arquivos criados
        os.remove(input_file)
        os.remove(output_file)



if __name__ == '__main__':
    unittest.main()

