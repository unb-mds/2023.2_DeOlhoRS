import regex as re
import json
""""
        {
            municipio: nome do munucipio
            data: data do dia de extração
            nomeação: bool indicando se há 
            extração: bool indicando se há
            nomeado: nome/cargo/cpf ou None 
            exonerado: nome/cargo/cpf ou None 

        }
"""

with open("2011-01-04.txt", 'r') as arquivo: 
    texto = arquivo.read()
    padrao = re.escape("PREFEITURA MUNICIPAL ")
    blocos = re.split(padrao, texto)
    # Data
    padrao = r'\d{2} de [A-Z][a-z]+ de \d{4}'
    datas_encontradas = re.findall(padrao, texto)
    data = datas_encontradas.pop()

    for bloco in blocos[1:]:
        bloco = bloco.strip()
        nomeacao = None
        exoneracao = None
        # Nome do Municipio 
        padraoMunicipio = r'DE\s*([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ ]+)(?:\s+([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ ]+))?'
        municipio = re.search(padraoMunicipio, bloco)
        nomeDoMunicipio = municipio.group(1).strip()
        try:
            segundaPalavra = municipio.group(2).strip()
        except:
            pass
        if "SECRETARIA" not in segundaPalavra and "ASSESSORIA" not in segundaPalavra and "GABINETE" not in segundaPalavra and "CONSULTORIA" not in segundaPalavra:
            nomeDoMunicipio += " " + segundaPalavra
        dadosNomeacao = None
        if re.search(re.escape("nomeia"), bloco, re.IGNORECASE):
            entreNome = r"Sr\. (.*?),"
            nomeado = re.search(entreNome, texto)
            nomeDoNomeado = nomeado.group(1).strip()
            
            padraoCargo = r"para exercer o Cargo de (.*?)(?:\n|$)"
            cargo = re.search(padraoCargo, texto)
            cargoNomeado = cargo.group(1).strip()
            dadosNomeacao = f'{nomeDoNomeado} / {cargoNomeado}'
            nomeacao = True
        else:
            dadosNomeacao = None
            nomeacao = False

        if re.search(re.escape("exonera"), bloco, re.IGNORECASE):
            exoneracao = True
        else:   
            exoneracao = False
        # Escrita no .json   
        

