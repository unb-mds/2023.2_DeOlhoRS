import regex as re
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
        # Municipio 
        padraoMunicipio = r'DE(.*?)\n'
        municipio = re.search(padraoMunicipio, bloco)
        nomeDoMunicipio = municipio.group(1).strip()
        
        if re.search(re.escape("nomeia"), bloco, re.IGNORECASE):
            entreNome = r"Sr\. (.*?),"
            nomeado = re.search(entreNome, texto)
            nomeDoNomeado = nomeado.group(1).strip()
            
            padraoCargo = r"para exercer o Cargo de (.*?)(?:\n|$)"
            cargo = re.search(padraoCargo, texto)
            cargoNomeado = cargo.group(1).strip()
            print(cargoNomeado)
            nomeacao = True
        else:
            nomeacao = False

        if re.search(re.escape("exonera"), bloco, re.IGNORECASE):
            exoneracao = True
        else:   
            exoneracao = False
            
        # Escrita no .json   
        print("Separação")      
        print(data)
        print("Municipio: ", nomeDoMunicipio)
        print("Há nomeação: ", nomeacao)
        if nomeacao == True:
            print("Nome do nomeado: ", nomeDoNomeado)
            print("Cargo do nomeado: ", cargoNomeado)
        print("Há exoneração: ", exoneracao)
        print('\n\n')
    