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
    def extrairNomeMunicipio(self, bloco):
        # Extrair nome do município com flexibilidade para padrões diferentes
        padrao_municipio = re.compile(r'(?:PREFEITURA MUNICIPAL DE\s*|MUNICÍPIO DE\s*|CÂMARA MUNICIPAL DE VEREADORES\s*\n\s*)(.*?)(?=\n)', re.IGNORECASE | re.DOTALL)
        municipio = padrao_municipio.search(bloco)

        if municipio:
            return municipio.group(1).strip()
        else:
            return "Município não encontrado"
    def escritaDatabase(self, dados):
        with open("database.json", "r", encoding="utf-8") as file:
            dados_escritos = json.load(file)

        dados_escritos.append(dados)
        with open("database.json", "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)

    def extrairDados(self, nomeDoArquivo):
        with open(nomeDoArquivo, 'r') as arquivo: 
            texto = arquivo.read()
            padrao = r"(?:\s*ESTADO DO RIO GRANDE DO SUL)?(.*?)(?:Identificador)"
            
            blocosProcessosMunicipio = re.findall(padrao, texto, re.DOTALL)

            for bloco in blocosProcessosMunicipio[0:]:
                bloco = bloco.strip() 
        
                nome_do_municipio = self.extrairNomeMunicipio(bloco)

                # Nome do Municipio 
                
                """try:
                    print(nomeDoMunicipio = municipio.group(1).strip())
                    segundaPalavra = municipio.group(2).strip()
                except:
                    pass
                if "SECRETARIA" not in segundaPalavra and "ASSESSORIA" not in segundaPalavra and "GABINETE" not in segundaPalavra and "CONSULTORIA" not in segundaPalavra:
                    nomeDoMunicipio += " " + segundaPalavra
                """
                # Verificação de existência de nomeação com base os padrões encontrados
                nomeacao = bool(re.search(re.escape("nomeia"), bloco, re.IGNORECASE))
                exoneracao = bool(re.search(re.escape("exonera "), bloco, re.IGNORECASE))
                # Escrita no .json   
                # Json só para a "Contagem" de nomeações e exonerações
                data = arquivo.name
                data = data[:-4]
                dados_novos = {
                    "nomeMunicipio": nome_do_municipio,
                    "dataPost": data[-10:],
                    "haNomeacao": nomeacao,
                    "haExoneracao": exoneracao,
                    
                }
                self.escritaDatabase(dados_novos)



