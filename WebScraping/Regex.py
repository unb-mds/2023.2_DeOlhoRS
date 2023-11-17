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
        padrao_municipio = re.compile(r'(?:PREFEITURA MUNICIPAL DE\s*|MUNICÍPIO DE\s*|CÂMARA MUNICIPAL DE VEREADORES\s*\n\s*)(.*?)(?=\n)', re.IGNORECASE )
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
            padrao = re.compile(r'(NOMEIA|EXONERA|resolve nomear|decide nomear|decide exonerar|resolve exonerar)', re.IGNORECASE)

            resultados = padrao.finditer(texto)
        
            for correspondencia in resultados:
                inicio_contexto = max(correspondencia.start() - 250, 0)  
                fim_contexto = min(correspondencia.end() +250, len(texto))  

                contexto = texto[inicio_contexto:fim_contexto]

                print("Correspondência:", correspondencia.group())
                print("Contexto:", contexto)
                print("-----")

                # Restante do seu código aqui
                nomeDoMunicipio = self.extrairNomeMunicipio(contexto)
                data = arquivo.name
                data = data[:-4]
                data = data[-10:]
                nomeacao = False
                exoneracao = False

                if correspondencia.group(1).lower() in ["nomeia", "resolve nomear", "decide nomear"]:
                    nomeacao = True
                elif correspondencia.group(1).lower() in ["exonera", "resolve exonerar", "decide exonerar"]:
                    exoneracao = True 

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



