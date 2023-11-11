import re
import json
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
    def escritaDatabase(self, dados):
        with open("database.json", "r", encoding="utf-8") as file:
            dados_escritos = json.load(file)

        dados_escritos.append(dados)
        with open("database.json", "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)

    def extrairDados(self, nomeDoArquivo):
        with open(nomeDoArquivo, 'r') as arquivo: 
            texto = arquivo.read()
            padrao = r"(?:\s*ESTADO DO RIO GRANDE DO SUL)?(.*?)(?:ESTADO DO RIO GRANDE DO SUL)"
            
            blocosProcessosMunicipio = re.findall(padrao, texto, re.DOTALL)

            # Data
            padrao = r'\d{2} de [A-Z][a-z]+ de \d{4}'
            datas_encontradas = re.findall(padrao, texto)
            data = datas_encontradas.pop()

            for bloco in blocosProcessosMunicipio[1:]:
                bloco = bloco.strip() 
                nomeacao = None
                exoneracao = None
                
                # Nome do Municipio 
                padraoMunicipio = r'PREFEITURA MUNICIPAL DE\s*([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ\'-]+)(?:\s+([A-ZÁÀÃÉÈÍÏÓÒÕÚÇ\'-]+))?'
                municipio = re.search(padraoMunicipio, bloco)

                nomeDoMunicipio = municipio.group(1).strip()
                try:
                    segundaPalavra = municipio.group(2).strip()
                except:
                    pass
                if "SECRETARIA" not in segundaPalavra and "ASSESSORIA" not in segundaPalavra and "GABINETE" not in segundaPalavra and "CONSULTORIA" not in segundaPalavra:
                    nomeDoMunicipio += " " + segundaPalavra

                # Verificação de existência de nomeação com base os padrões encontrados
                if re.search(re.escape("nomeia"), bloco, re.IGNORECASE):
                    nomeacao = True
                else:
                    nomeacao = False
                # Verificação de existência de exoneração com base os padrões encontrados
                if re.search(re.escape("exonera"), bloco, re.IGNORECASE):
                    exoneracao = True
                else:   
                    exoneracao = False
                # Escrita no .json   
                # Json só para a "Contagem" de nomeações e exonerações
                dados_novos = {
                    "nomeMunicipio": nomeDoMunicipio,
                    "dataPost": data,
                    "haNomeacao": nomeacao,
                    "haExoneracao": exoneracao,
                }
                self.escritaDatabase(dados_novos)



