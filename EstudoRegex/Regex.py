import regex as re
with open("2011-01-04.txt", 'r') as arquivo: 
    texto = arquivo.read()
    padrao = re.escape("PREFEITURA MUNICIPAL DE ")
    correspondencias = re.finditer(padrao, texto, re.DOTALL | re.IGNORECASE)
    blocos = re.split(padrao, texto)

    for bloco in blocos[1:]:
        bloco = bloco.strip()
        if re.search(re.escape("nomeia"), bloco, re.IGNORECASE):
            print("Há nomeação! Data: ")
        else:
            print(f'Não há nomeação.')

                    