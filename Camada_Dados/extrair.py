# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=line-too-long
import json
from operator import itemgetter
import os
from collections import defaultdict
# pylint: disable=trailing-whitespace
# pylint: disable=too-many-locals

class OrganizadorDeDados:
   
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=E1120
    # pylint: disable=W1514
    def processar_dados(self, input_file, output_file):
        # Lê os dados do arquivo JSON de entrada
        with open(input_file, 'r', encoding='utf-8') as f:
            dados_municipios = json.load(f)

        # Dicionário para armazenar contagens de exonerações e nomeações por mês e município
        cont_municipoios = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'nomeacoes': 0, 'exoneracoes': 0})))

        # Processa os dados para contar nomeações e exonerações por mês e município
        for municipio in dados_municipios:
            nome_municipio = municipio.get('nomeMunicipio', '')
            data_post = municipio.get('dataPost', '')
            
            if nome_municipio and data_post:
                ano, mes, _ = data_post.split('-')
                # Normaliza o nome do município para caixa alta
                nome_municipio = nome_municipio.upper()
                cont_municipoios[nome_municipio][ano][mes]['nomeacoes'] += municipio['haNomeacao']
                cont_municipoios[nome_municipio][ano][mes]['exoneracoes'] += municipio['haExoneracao']

        # Cria lista de dicionários ordenada por município, ano e mês
        dados_grafico = []

        for municipio, dados_ano in cont_municipoios.items():
            for ano, dados_mes in dados_ano.items():
                for mes, contagem in dados_mes.items():
                    dados_grafico.append({
                        'municipio': municipio,
                        'ano': ano,
                        'mes': mes,
                        'nomeacoes': contagem['nomeacoes'],
                        'exoneracoes': contagem['exoneracoes']
                    })

        # Ordena a lista por município, ano e mês
        dados_grafico = sorted(
            dados_grafico,
            key=lambda x: (x['municipio'], x['ano'], x['mes'])
        )

        # Escreve os dados no arquivo JSON de saída com codificação UTF-8
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

    def processar_anos(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            dados_municipios = json.load(f)

        contagens = defaultdict(lambda: {'nomeacoes': 0, 'exoneracoes': 0})

        for registro in dados_municipios:
            nome_municipio = registro.get('municipio', '')
            nomeacoes = registro.get('nomeacoes', 0)
            exoneracoes = registro.get('exoneracoes', 0)

            # Tratar variações de caixa alta ou normal do município
            nome_municipio_lower = nome_municipio.lower()
            if nome_municipio_lower not in contagens:
                contagens[nome_municipio_lower] = {'nomeacoes': 0, 'exoneracoes': 0}
            contagens[nome_municipio_lower]['nomeacoes'] += nomeacoes
            contagens[nome_municipio_lower]['exoneracoes'] += exoneracoes

        dados_grafico = []

        for municipio, contagem in contagens.items():
            dados_grafico.append({
                'municipio': municipio,
                'nomeacoes': contagem['nomeacoes'],
                'exoneracoes': contagem['exoneracoes']
            })

        dados_grafico = sorted(
            dados_grafico,
            key=lambda x: x['municipio']
        )


        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dados_grafico, f, indent=2, ensure_ascii=False)
    
    def processar_arquivos_json(self, nomes_arquivos, output_file):

        def agrupar_por_nome(municipios):
            grupos = defaultdict(lambda: {"nomeacoes": 0, "exoneracoes": 0})
            for municipio in municipios:
                nome = municipio["municipio"].lower()
                grupos[nome]["nomeacoes"] += municipio["nomeacoes"]
                grupos[nome]["exoneracoes"] += municipio["exoneracoes"]
            return [{"municipio": nome, **valores} for nome, valores in grupos.items()]


        def remover_invalidos(municipios):
            return [municipio for municipio in municipios if "publicado por gabinete ou afins" not in municipio["municipio"].lower()]
        
        def ordenar_municipios(municipios, chave):
            return sorted(municipios, key=itemgetter(chave), reverse=True)[:5]

        todos_os_municipios = []

        for nome_arquivo in nomes_arquivos:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                todos_os_municipios.extend(dados)

        municipios_validos = remover_invalidos(todos_os_municipios)
        municipios_agrupados = agrupar_por_nome(municipios_validos)

        municipios_com_mais_nomeacoes = ordenar_municipios(municipios_agrupados, 'nomeacoes')
        municipios_com_mais_exoneracoes = ordenar_municipios(municipios_agrupados, 'exoneracoes')

        resultado = {
            'municipios_com_mais_nomeacoes': municipios_com_mais_nomeacoes,
            'municipios_com_mais_exoneracoes': municipios_com_mais_exoneracoes
        }

        with open(output_file, 'w', encoding='utf-8') as arquivo_resultado:
            json.dump(resultado, arquivo_resultado, ensure_ascii=False, indent=2)


if __name__ == "__main__":

    organizador = OrganizadorDeDados()
    organizador.processar_dados("2021.json", "dados_grafico_2021.json")
    # diretorio atual = /squad08/camada_dados
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    #Função para agrupar os meses
    pasta_json = f'{diretorio_atual}/dados_para_os_Graficos'
    #processar_pasta(pasta_json)
    organizador = OrganizadorDeDados()
    organizador.processar_dados("2009.json", "dados_grafico_2009.json")
    #Chamar a função processar_anos
    organizador.processar_anos("dados_grafico_2021.json", "resultado_grafico_2021.json")
    #Chamar a função para calcular o rank das nomeacoes e exoneracoes
    lista = ["resultado_dados_grafico_2009.json", "resultado_dados_grafico_2013.json", "resultado_dados_grafico_2017.json", "resultado_dados_grafico_2020.json", "resultado_dados_grafico_2021.json"]
    organizador.calcula_ano(lista, "Rank.json")
    