import unittest
import os
import json
from Camada_Dados.Extrair import OrganizadorDeDados


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

if __name__ == '__main__':
    unittest.main()

