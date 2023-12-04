from gensim.models import Word2Vec
import re
import json
from datetime import datetime, timedelta

resultados_acumulados_por_data = {}

# Data inicial e final
data_inicial = datetime(2017, 1, 1)
data_final = datetime(2017, 12, 31)

# Lista de datas no formato 'YYYY-MM-DD'
datas = [(data_inicial + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((data_final - data_inicial).days + 1)]

for data in datas:
    caminho_do_arquivo = f"Camada_Dados/txt/2017/{data}.txt"
    resultados_do_dia = {
        "nomes_nomeados": [],
        "nomes_exonerados": [],
    }

    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            diario_oficial_text = arquivo.read()

            # Padrões de regex para nomeações e exonerações
            padroes_nomeacao = re.compile(r'\b(nomear|nomeia|nomeado|nomeada|nomear|nomeação de|fica nomeada|fica nomeado)\b', flags=re.IGNORECASE)
            padroes_exoneracao = re.compile(r'\b(exonera|exonera|exonerado|exonerada|exonerar|exoneração de|fica exonerada|fica exonerado)\b', flags=re.IGNORECASE)

            # Encontrar correspondências no texto
            matches_nomeacao = padroes_nomeacao.finditer(diario_oficial_text)
            matches_exoneracao = padroes_exoneracao.finditer(diario_oficial_text)

            # Extrair nomes após as correspondências, ignorando "o sr" e "a sra"
            nomes_apos_nomeacao = []
            nomes_apos_exoneracao = []

            for match in matches_nomeacao:
                start_index = match.end()
                end_index = diario_oficial_text.find(',', start_index)
                nome_chunk = diario_oficial_text[start_index:end_index].strip()

                # Ignorar "o sr" e "a sra" ao extrair nomes
                if not re.match(r'\bo\s*sr\b|\ba\s*sra\b', nome_chunk, flags=re.IGNORECASE):
                    nomes_apos_nomeacao.append(nome_chunk)

            for match in matches_exoneracao:
                start_index = match.end()
                end_index = diario_oficial_text.find(',', start_index)
                nome_chunk = diario_oficial_text[start_index:end_index].strip()

                # Ignorar "o sr" e "a sra" ao extrair nomes
                if not re.match(r'\bo\s*sr\b|\ba\s*sra\b', nome_chunk, flags=re.IGNORECASE):
                    nomes_apos_exoneracao.append(nome_chunk)

            # Treinar o modelo Word2Vec
            tokenized_text = [re.findall(r'\b\w+\b', sentence.lower()) for sentence in diario_oficial_text.split('.')]
            model = Word2Vec(sentences=tokenized_text, vector_size=100, window=5, min_count=1, workers=4)

            # Encontrar palavras similares para cada nome
            resultados_similares_nomeacao = {}
            resultados_similares_exoneracao = {}

            for nome in nomes_apos_nomeacao:
                if nome in model.wv:
                    similares = model.wv.most_similar(nome, topn=1)
                    resultados_similares_nomeacao[nome] = similares[0][0]

            for nome in nomes_apos_exoneracao:
                if nome in model.wv:
                    similares = model.wv.most_similar(nome, topn=1)
                    resultados_similares_exoneracao[nome] = similares[0][0]

            resultado_json = {
                "nomes_nomeados": nomes_apos_nomeacao,
                "nomes_exonerados": nomes_apos_exoneracao,
            }

            resultados_do_dia["nomes_nomeados"].extend(nomes_apos_nomeacao)
            resultados_do_dia["nomes_exonerados"].extend(nomes_apos_exoneracao)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_do_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

    # Converte a string de data para o formato datetime
    data_formatada = datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

    # Adiciona os resultados do dia ao dicionário acumulado por data
    resultados_acumulados_por_data[data_formatada] = resultados_do_dia

# Salva resultados acumulados por data em um único arquivo JSON
with open('nomes_2017.json', 'w', encoding='utf-8') as json_file:
    json.dump(resultados_acumulados_por_data, json_file, ensure_ascii=False, indent=2)

print("Resultados acumulados por data armazenados em resultados_acumulados_por_data.json")




