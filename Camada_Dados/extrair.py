# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
import json
import os
from collections import defaultdict
# pylint: disable=trailing-whitespace
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods

class OrganizadorDeDados:
   
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    
    def processar_dados(self, input_file, output_file):
        
        with open(input_file, 'r', encoding='utf-8') as f:
            dados_municipios = json.load(f)

        default_contagem = {'nomeacoes': 0, 'exoneracoes': 0}
        default_ano = defaultdict(lambda: default_contagem)
        default_mes = defaultdict(lambda: default_ano)
        contagens = defaultdict(lambda: default_mes)

        for municipio in dados_municipios:
            nome_municipio = municipio.get('nomeMunicipio', '')
            data_post = municipio.get('dataPost', '')    
            if nome_municipio and data_post:
                ano, mes, _ = data_post.split('-')
                contagens[nome_municipio][ano][mes]['nomeacoes'] += municipio['haNomeacao']
                contagens[nome_municipio][ano][mes]['exoneracoes'] += municipio['haExoneracao']

        dados_grafico = []

        for municipio, dados_ano in contagens.items():
            for ano, dados_mes in dados_ano.items():
                for mes, contagem in dados_mes.items():
                    dados_grafico.append({
                        'municipio': municipio,
                        'ano': ano,
                        'mes': mes,
                        'nomeacoes': contagem['nomeacoes'],
                        'exoneracoes': contagem['exoneracoes']
                    })

        dados_grafico = sorted(
            dados_grafico,
            key=lambda x: (x['municipio'], x['ano'], x['mes'])
        )

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dados_grafico, f, indent=2, ensure_ascii=False)
    
    def processar_pasta(self, pasta):
        resumo_por_ano = {}
        # Iterar sobre os arquivos na pasta
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith('.json'):
                caminho_arquivo = os.path.join(pasta, nome_arquivo)
                # Processar cada arquivo JSON
                with open(caminho_arquivo, 'r') as arquivo_json:
                    dados_lista = json.load(arquivo_json)
                    # Iterar sobre os objetos na lista
                    for dados in dados_lista:
                        ano = dados.get("ano", "")
                        nomeacoes = dados.get("nomeacoes", 0)
                        exoneracoes = dados.get("exoneracoes", 0)
                        # Atualizar o resumo para o ano correspondente
                        if ano not in resumo_por_ano:
                            resumo_por_ano[ano] = {"nomeacoes": 0, "exoneracoes": 0}
                        resumo_por_ano[ano]["nomeacoes"] += nomeacoes
                        resumo_por_ano[ano]["exoneracoes"] += exoneracoes
        # Salvar o resumo por ano em um novo arquivo JSON
        with open('resumo_por_ano.json', 'w') as arquivo_resumo:
            json.dump(resumo_por_ano, arquivo_resumo, indent=2)   
    if __name__ == "__main__":
        # diretorio atual = /squad08/camada_dados
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        pasta_json = f'{diretorio_atual}/dados_para_os_Graficos'
        processar_pasta(pasta_json)
        