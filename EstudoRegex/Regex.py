import regex as re


def pega_inf(bloco):
    lista_sobre = []
    nomes = []
    for letra in blocos[1:]:
        palavra = letra
        for l in range(0, len(palavra)):
            if palavra[l] == "S" and palavra[l+1] == "r" and palavra[l+2] == ".":
                informacoes= palavra[l:70+l]
                nome = palavra[l:l+10]
                if nome in nomes:
                    print("Já coloquei")
                else:
                    nomes.append(nome)
                    lista_sobre.append(informacoes)

    print("Nomes de concursados:")          
    print(nomes)
    print("Cargo para exercer")
    print(lista_sobre)



with open("2011-01-04.txt", 'r') as arquivo: 
    texto = arquivo.read()
    padrao = re.escape("PREFEITURA MUNICIPAL DE ")
    correspondencias = re.finditer(padrao, texto, re.DOTALL | re.IGNORECASE)
    blocos = re.split(padrao, texto)
    lista_de_informacoes = []

    for bloco in blocos[1:]:
        bloco = bloco.strip()
        #print(bloco)
        if re.search(re.escape("nomeia"), bloco, re.IGNORECASE):
            print("Há nomeação! Data: ")
            pega_inf(bloco)
    
            lista_de_informacoes.append(bloco)
        else:
            print(f'Não há nomeação.')



    