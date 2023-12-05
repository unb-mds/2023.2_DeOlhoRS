import re

def extrair_cargos_diario_oficial(arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()

    # Padrões para exonerações e nomeações
    padrao_exoneracao = re.compile(r'exonera', re.IGNORECASE)
    padrao_nomeacao = re.compile(r'nomeia', re.IGNORECASE)
    padrao_cargo = re.compile(r'cargo de\s*(.*?)\n', re.DOTALL)

    # Encontrar todas as correspondências nos padrões
    exon = re.finditer(padrao_exoneracao, conteudo)
    nome = re.finditer(padrao_nomeacao, conteudo)

    # Inicializar listas para armazenar informações
    cargos_exoneracao = []
    cargos_nomeacao = []

    # Extrair cargos para exonerações
    for match in exon:
        match_cargo = padrao_cargo.search(conteudo, match.end())
        if match_cargo:
            cargo_exon = match_cargo.group(1).strip()
            cargos_exoneracao.append(cargo_exon)

    # Extrair cargos para nomeações
    for match in nome:
        match_cargo = padrao_cargo.search(conteudo, match.end())
        if match_cargo:
            cargo_nomeacao = match_cargo.group(1).strip()
            cargos_nomeacao.append(cargo_nomeacao)

    # Imprimir os resultados
    print(f'Número de exonerações: {len(cargos_exoneracao)}')
    print(f'Número de nomeações: {len(cargos_nomeacao)}')

    # Imprimir cargos
    print('\nCargos de Exonerações:')
    for cargo in cargos_exoneracao:
        print(cargo)

    print('\nCargos de Nomeações:')
    for cargo in cargos_nomeacao:
        print(cargo)

# Substitua 'caminho/do/seu/arquivo.txt' pelo caminho real do seu arquivo de Diário Oficial
extrair_cargos_diario_oficial("/home/bibia/Documentos/4°semestre/MDS/2023-2-Squad08/WebScraping/txt/2009/2009-07-05.txt")
