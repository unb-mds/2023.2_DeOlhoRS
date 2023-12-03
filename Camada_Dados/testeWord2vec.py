from gensim.models import Word2Vec
import re
import json

# Caminho do arquivo
caminho_do_arquivo = "WebScraping/txt/2021/2021-08-16.txt"

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

        # Armazenar resultados em um arquivo JSON
        resultado_json = {
            "nomes_apos_nomeacao": nomes_apos_nomeacao,
            "nomes_apos_exoneracao": nomes_apos_exoneracao,
        }

        with open('resultados.json', 'w', encoding='utf-8') as json_file:
            json.dump(resultado_json, json_file, ensure_ascii=False, indent=2)

        print("Resultados armazenados em resultados.json")

except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_do_arquivo}")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")




