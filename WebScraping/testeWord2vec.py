from gensim.models import Word2Vec
import re

# Caminho do arquivo
caminho_do_arquivo = "WebScraping/txt/2009/2009-07-03.txt"

try:
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
        diario_oficial_text = arquivo.read()

        # Padrões de regex para nomeações e exonerações
        padroes_nomeacao = re.compile(r'\b(nomear|nomeia|nomeado|nomeada|nomear|nomeação de)\b', flags=re.IGNORECASE)
        padroes_exoneracao = re.compile(r'\b(exonera|exonera|exonerado|exonerada|exonerar|exoneração de)\b', flags=re.IGNORECASE)

        # Encontrar correspondências no texto
        matches_nomeacao = padroes_nomeacao.finditer(diario_oficial_text)
        matches_exoneracao = padroes_exoneracao.finditer(diario_oficial_text)

        # Extrair nomes após as correspondências
        nomes_apos_nomeacao = []
        nomes_apos_exoneracao = []

        for match in matches_nomeacao:
            start_index = match.end()
            end_index = diario_oficial_text.find(',', start_index)
            nome = diario_oficial_text[start_index:end_index].strip()
            nomes_apos_nomeacao.append(nome)

        for match in matches_exoneracao:
            start_index = match.end()
            end_index = diario_oficial_text.find(',', start_index)
            nome = diario_oficial_text[start_index:end_index].strip()
            nomes_apos_exoneracao.append(nome)

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

        # Exibir os resultados
        print("Nomes após nomeações:", nomes_apos_nomeacao)

        print("Nomes após exonerações:", nomes_apos_exoneracao)
    
except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_do_arquivo}")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
