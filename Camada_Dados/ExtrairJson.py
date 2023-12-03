# pylint: disable=missing-import-docstring
import json
from collections import defaultdict
# pylint: disable=missing-class-docstring
class OrganizadorDeDados:
    # pylint: disable=missing-function-docstring
    # pylint: disable=too-few-public-methods
    def processar_dados(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            dados_municipios = json.load(f)

        default_contagem = {'nomeacoes': 0, 'exoneracoes': 0}
        default_ano = defaultdict(lambda: default_contagem)
        default_mes = defaultdict(lambda: default_ano)
        contagens_municipio = defaultdict(lambda: default_mes)

        for municipio in dados_municipios:
            nome_municipio = municipio.get('nomeMunicipio', '')
            data_post = municipio.get('dataPost', '')    
            if nome_municipio and data_post:
                ano, mes, _ = data_post.split('-')
                contagens_municipio[nome_municipio][ano][mes]['nomeacoes'] += municipio['haNomeacao']
                contagens_municipio[nome_municipio][ano][mes]['exoneracoes'] += municipio['haExoneracao']

        dados_grafico = []

        for municipio, dados_ano in contagens_municipio.items():
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
