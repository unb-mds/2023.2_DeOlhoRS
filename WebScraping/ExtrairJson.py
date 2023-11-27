import json
from collections import defaultdict

# Função para processar os dados e criar o arquivo para o gráfico
def processar_dados(input_file, output_file):
    # Lê os dados do arquivo JSON de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        dados_municipios = json.load(f)

    # Dicionário para armazenar contagens de exonerações e nomeações por mês e município
    contagens_por_municipio_ano_mes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {'nomeacoes': 0, 'exoneracoes': 0})))

    # Processa os dados para contar nomeações e exonerações por mês e município
    for municipio in dados_municipios:
        nome_municipio = municipio.get('nomeMunicipio', '')
        data_post = municipio.get('dataPost', '')
        
        if nome_municipio and data_post:
            ano, mes, _ = data_post.split('-')
            contagens_por_municipio_ano_mes[nome_municipio][ano][mes]['nomeacoes'] += municipio['haNomeacao']
            contagens_por_municipio_ano_mes[nome_municipio][ano][mes]['exoneracoes'] += municipio['haExoneracao']

    # Cria lista de dicionários ordenada por município, ano e mês
    dados_grafico = []

    for municipio, dados_ano in contagens_por_municipio_ano_mes.items():
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


# Chama a função com os nomes dos arquivos de entrada e saída
processar_dados('2009.json', 'dados_grafico_2009.json')