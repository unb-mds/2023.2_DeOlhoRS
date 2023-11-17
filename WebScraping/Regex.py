import re
import json
import os
""""
        {
            municipio: nome do munucipio
            data: data do dia de extração
            nomeação: bool indicando se há 
            extração: bool indicando se há
        }
"""
class ExtratorDeDados:
    def __init__(self):
        pass
    def extrairNomeMunicipio(self, bloco):
        # Extrair nome do município com flexibilidade para padrões diferentes
        padrao_municipio = re.compile(r'(?:PREFEITURA MUNICIPAL DE\s*|MUNICÍPIO DE\s*|CÂMARA MUNICIPAL DE VEREADORES\s*\n\s*)(.*?)(?=\n)' )
        municipio = padrao_municipio.search(bloco)
        if municipio:
            return municipio.group(1).strip()
        else:
            
            return "Publicado por Secretaria/Gabinete ou afins"
    def escritaDatabase(self, dados):
        with open("database.json", "r", encoding="utf-8") as file:
            dados_escritos = json.load(file)

        dados_escritos.append(dados)
        with open("database.json", "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)

    def extrairDados(self, nomeDoArquivo):
        with open(nomeDoArquivo, 'r') as arquivo: 
            texto = arquivo.read()
            padrao = re.compile(r'(ESTADO DO RIO GRANDE DO SUL|PREFEITURA MUNICIPAL DE|MUNICIPIO DE)\W*([^C]*(?:C(?!ódigo Identificador)[^C]*)*)\W*(NOMEIA|resolve nomear|decide nomear|EXONERA |decide exonerar|resolve exonerar)\W*([^C]*(?:C(?!ódigo Identificador)[^C]*)*)\W*(Código Identificador|Identificador|Publicado por)', re.IGNORECASE)

            resultados = padrao.findall(texto)
        
        for resultado in resultados:
            # Resultado armazena o bloco de texto que compõem uma nomeação e/ou exoneração 
            #Caso queira saber como está sendo quebrado o texto para um debbug, tire as aspas
            """print("Bloco de Texto:")
            print(resultado[0])
            print("\n")
            print(resultado[1])
            print("\n")
            print(resultado[2])
            print("\n")
            print("Fim do bloco\n--------------------------\n")"""
            # Resultado em 0 possui Estado Do Rio Grande do Sul ou Prefeitura Municipal de ou Municipio de
            # Resultado em 1 possui todo o bloco de texto pós resultado em 0 e antes da ação (nomeação ou exoneração)
            # Resultado em 2 possui a ação
            # Resultado em 3 possui todo o texto antes do código identificador e depois da ação

            # O bloco completo, não está sendo usado. Mas para que fique exemplificado, ele é a contacatenaçao de todas as outras string, ou seja o bloco todo
            bloco_completo = resultado[0]+resultado[1]+resultado[2]+resultado[3]
            
            nomeDoMunicipio = self.extrairNomeMunicipio(resultado[1])
            data = arquivo.name
            # Tira os 4 ultimos char do nome do arquivo (YYYY-MM-DD.txt), ou seja, ".txt"
            data = data[:-4]
            data = data[-10:]
            nomeacao = False
            exoneracao = False
            # descobre qual o tipo de ação, usando do resultado em 2
            if resultado[2] == "Nomeia" or resultado[2] =="NOMEIA" or resultado[2] =="resolve nomear" or resultado[2] =="decide nomear":
                nomeacao = True
            else:
                exoneracao = True 
            # Criação de um dicionário para a futura escrita dele no json       
            dados_novos = {
                "nomeMunicipio": nomeDoMunicipio,
                "dataPost": data,
                "haNomeacao": nomeacao,
                "haExoneracao": exoneracao,
                
            }
            self.escritaDatabase(dados_novos)
    
    def extraiGeral(self):
        # Atualmente só está estraíndo 2009, que é o que se tem até o momento 
        arquivos = "/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/"
        arquivos = os.listdir("/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/")
        for arq in arquivos:
            arqPath = f'/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/{arq}'
            self.extrairDados(arqPath)
regex = ExtratorDeDados()
regex.extraiGeral()



