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
        self.nomeDosMunicipios = [
            "ACEGUÁ",
            "ÁGUA SANTA", 
            "AGUDO", 
            "AJURICABA",
            "ALECRIM", 
            "ALEGRETE", 
            "ALMIRANTE TAMANDARÉ DO SUL", 
            "ALPESTRE", 
            "ALTO ALEGRE", 
            "ALVORADA",
            "AMETISTA DO SUL", 
            "ANDRÉ DA ROCHA", 
            "ANTA GORDA", 
            "ANTÔNIO PRADO", 
            "ARATIBA", 
            "ARROIO DO MEIO", 
            "ARROIO DO SAL", 
            "ARROIO DO TIGRE", 
            "ARROIO GRANDE", 
            "ARVOREZINHA", 
            "AUGUSTO PESTANA",
            "BAGÉ", 
            "BALNEÁRIO PINHAL", 
            "BARÃO DE COTEGIPE", 
            "BARÃO DO TRIUNFO",
            "BARRACÃO", 
            "BARRA DO QUARAÍ", 
            "BARRA DO RIBEIRO", 
            "BARRA FUNDA", 
            "BARROS CASSAL", 
            "BENTO GONÇALVES", 
            "BOA VISTA DAS MISSÕES", 
            "BOA VISTA DO BURICÁ", 
            "BOA VISTA DO CADEADO", 
            "BOA VISTA DO SUL", 
            "BOM JESUS", 
            "BOM PRINCÍPIO", 
            "BOM RETIRO DO SUL", 
            "BOQUEIRÃO DO LEÃO", 
            "BRAGA", 
            "BROCHIER", 
            "BUTIÁ", 
            "CAÇAPAVA DO SUL", 
            "CACEQUI", 
            "CACHOEIRA DO SUL", 
            "CACHOEIRINHA", 
            "CACIQUE DOBLE", 
            "CAIBATÉ", 
            "CAIÇARA", 
            "CAMAQUÃ", 
            "CAMARGO", 
            "CAMBARÁ DO SUL", 
            "CAMPESTRE DA SERRA", 
            "CAMPINAS DO SUL", 
            "CAMPO BOM", 
            "CAMPOS BORGES",
            "CANDELÁRIA", 
            "CÂNDIDO GODÓI", 
            "CANDIOTA", 
            "CANELA", 
            "CANGUÇU", 
            "CANOAS", 
            "CAPÃO BONITO DO SUL", 
            "CAPÃO DA CANOA", 
            "CAPÃO DO LEÃO", 
            "CARAZINHO", 
            "CARLOS BARBOSA", 
            "CASCA", 
            "CASEIROS", 
            "CAXIAS DO SUL", 
            "CERRO GRANDE", 
            "CERRO LARGO", 
            "CHAPADA", 
            "CHARQUEADAS", 
            "CHARRUA", 
            "CHIAPETTA", 
            "CIRÍACO", 
            "COLORADO", 
            "CONDOR", 
            "CONSTANTINA", 
            "COQUEIROS DO SUL", 
            "CORONEL BARROS", 
            "CORONEL BICACO", 
            "CORONEL PILAR", 
            "COTIPORÃ", 
            "CRISSIUMAL", 
            "CRISTAL", 
            "CRISTAL DO SUL", 
            "CRUZ ALTA", 
            "CRUZALTENSE", 
            "CRUZEIRO DO SUL", 
            "DAVID CANABARRO", 
            "DERRUBADAS", 
            "DOIS IRMÃOS", 
            "DOM FELICIANO", 
            "DOM PEDRO DE ALCÂNTARA", 
            "DOM PEDRITO", 
            "DONA FRANCISCA", 
            "ELDORADO DO SUL", 
            "ENCANTADO", 
            "ENCRUZILHADA DO SUL", 
            "ENGENHO VELHO", 
            "ENTRE-IJUÍS", 
            "ENTRE RIOS DO SUL", 
            "ERECHIM" 
            "ERNESTINA", 
            "ERVAL GRANDE", 
            "ERVAL SECO",
            "ESMERALDA", 
            "ESPUMOSO", 
            "ESTÂNCIA VELHA", 
            "ESTEIO", 
            "ESTRELA",
            "FAGUNDES VARELA", 
            "FARROUPILHA", 
            "FAXINAL DO SOTURNO", 
            "FAZENDA VILANOVA", 
            "FELIZ", 
            "FLORES DA CUNHA", 
            "FONTOURA XAVIER", 
            "FORQUETINHA",
            "FORTALEZA DOS VALOS", 
            "FREDERICO WESTPHALEN",
            "GARIBALDI", 
            "GENERAL CÂMARA"
            "GENTIL" 
            "GETÚLIO VARGAS", 
            "GIRUÁ", 
            "GRAMADO", 
            "GRAMADO XAVIER", 
            "GRAVATAÍ", 
            "GUABIJU", 
            "GUAÍBA", 
            "GUAPORÉ", 
            "GUARANI DAS MISSÕES", 
            "HORIZONTINA", 
            "HUMAITÁ", 
            "IBIAÇÁ", 
            "IBIRAIARAS", 
            "IBIRAPUITÃ", 
            "IBIRUBÁ", 
            "IGREJINHA", 
            "IJUÍ", 
            "ILÓPOLIS", 
            "IMBÉ", 
            "IMIGRANTE", 
            "INDEPENDÊNCIA",
            "IPÊ", 
            "IRAÍ", 
            "ITAPUCA", 
            "ITAQUI", 
            "ITATIBA DO SUL", 
            "IVOTI", 
            "JABOTICABA", 
            "JAGUARÃO", 
            "JAGUARI", 
            "JAQUIRANA", 
            "JÓIA" 
            "JÚLIO DE CASTILHOS", 
            "LAGOÃO", 
            "LAGOA DOS TRÊS CANTOS", 
            "LAGOA VERMELHA", 
            "LAJEADO", 
            "LAVRAS DO SUL", 
            "LIBERATO SALZANO", 
            "LINHA NOVA", 
            "MACHADINHO",  
            "MANOEL VIANA", 
            "MARATÁ", 
            "MARAU", 
            "MARCELINO RAMOS", 
            "MARQUES DE SOUZA", 
            "MATO CASTELHANO", 
            "MATO LEITÃO", 
            "MAXIMILIANO DE ALMEIDA", 
            "MINAS DO LEÃO", 
            "MIRAGUAÍ", 
            "MONTAURI", 
            "MONTE ALEGRE DOS CAMPOS", 
            "MONTE BELO DO SUL", 
            "MONTENEGRO", 
            "MORMAÇO", 
            "MUÇUM", 
            "MUITOS CAPÕES", 
            "MULITERNO", 
            "NICOLAU VERGUEIRO", 
            "NONOAI",
            "NOVA ALVORADA", 
            "NOVA ARAÇÁ", 
            "NOVA BASSANO", 
            "NOVA BOA VISTA", 
            "NOVA BRÉSCIA", 
            "NOVA CANDELÁRIA", 
            "NOVA PÁDUA", 
            "NOVA PALMA",
            "NOVA PETRÓPOLIS", 
            "NOVA PRATA", 
            "NOVA ROMA DO SUL", 
            "NOVA SANTA RITA", 
            "NOVO HAMBURGO",
            "NOVO TIRADENTES",
            "NOVO XINGU",
            "NOVO BARREIRO", 
            "OSÓRIO",
            "PAIM FILHO",
            "PALMEIRA DAS MISSÕES", 
            "PALMITINHO", 
            "PANAMBI", 
            "PANTANO GRANDE",
            "PARAÍ", 
            "PAROBÉ",
            "PASSO DO SOBRADO", 
            "PASSO FUNDO", 
            "PAVERAMA", 
            "PELOTAS", 
            "PICADA CAFÉ", 
            "PINHAL", 
            "PINHAL DA SERRA", 
            "PINHAL GRANDE", 
            "PINHEIRINHO DO VALE",
            "PINHEIRO MACHADO",
            "PIRATINI", 
            "PLANALTO", 
            "POÇO DAS ANTAS", 
            "PONTÃO", 
            "PORTO ALEGRE", 
            "PORTO XAVIER",
            "POUSO NOVO", 
            "PROGRESSO", 
            "PROTÁSIO ALVES", 
            "PUTINGA", 
            "QUARAÍ",
            "REDENTORA",
            "RELVADO",
            "RESTINGA SECA",
            "RIO DOS ÍNDIOS", 
            "RIO GRANDE", 
            "RIO PARDO",
            "ROCA SALES",
            "RODEIO BONITO",
            "ROLANTE",
            "RONDA ALTA",  
            "ROSÁRIO DO SUL", 
            "SAGRADA FAMÍLIA",
            "SALVADOR DO SUL",
            "SANANDUVA", 
            "SANTA CECÍLIA DO SUL",
            "SANTA CLARA DO SUL",
            "SANTA CRUZ DO SUL",
            "SANTA MARIA",
            "SANTANA DA BOA VISTA", 
            "SANT'ANA DO LIVRAMENTO", 
            "SANTA ROSA", 
            "SANTA TEREZA" ,
            "SANTA VITÓRIA DO PALMAR",
            "SANTIAGO", 
            "SANTO ÂNGELO", 
            "SANTO ANTÔNIO DO PALMA", 
            "SANTO ANTÔNIO DA PATRULHA", 
            "SANTO ANTÔNIO DAS MISSÕES",
            "SANTO ANTÔNIO DO PLANALTO",
            "SANTO AUGUSTO", 
            "SANTO CRISTO",
            "SANTO EXPEDITO DO SUL",
            "SÃO BORJA",
            "SÃO DOMINGOS DO SUL",
            "SÃO FRANCISCO DE ASSIS",
            "SÃO FRANCISCO DE PAULA",
            "SÃO GABRIEL",
            "SÃO JERÔNIMO",
            "SÃO JOÃO DA URTIGA",
            "SÃO JORGE",
            "SÃO JOSÉ DO HERVAL",
            "SÃO JOSÉ DO INHACORÁ",
            "SÃO JOSÉ DO NORTE",
            "SÃO JOSÉ DO OURO",
            "SÃO JOSÉ DOS AUSENTES",
            "SÃO LEOPOLDO",
            "SÃO LOURENÇO DO SUL",
            "SÃO LUIZ GONZAGA",
            "SÃO MARCOS",
            "SÃO MARTINHO",
            "SÃO NICOLAU",
            "SÃO PEDRO DA SERRA",
            "SÃO PEDRO DO SUL",
            "SÃO SEBASTIÃO DO CAÍ",
            "SÃO SEPÉ",
            "SÃO VENDELINO",
            "SÃO VICENTE DO SUL",
            "SAPIRANGA",
            "SAPUCAIA DO SUL",
            "SARANDI",
            "SEBERI", 
            "SEDE NOVA", 
            "SERAFINA CORRÊA", 
            "SÉRIO", 
            "SERTÃO",
            "SERTÃO SANTANA", 
            "SEVERIANO DE ALMEIDA",
            "SINIMBU",
            "SOLEDADE",
            "TAPEJARA", 
            "TAPERA",
            "TAPES",
            "TAQUARA",
            "TAQUARI", 
            "TAVARES", 
            "TENENTE PORTELA",
            "TERRA DE AREIA", 
            "TEUTÔNIA",
            "TIO HUGO", 
            "TIRADENTES DO SUL",
            "TORRES",
            "TRAMANDAÍ", 
            "TRÊS ARROIOS",
            "TRÊS CACHOEIRAS",
            "TRÊS COROAS",
            "TRÊS DE MAIO",
            "TRÊS PALMEIRAS",
            "TRÊS PASSOS",
            "TRINDADE DO SUL",
            "TRIUNFO",
            "TUCUNDUVA",
            "TUNAS",
            "TUPANCI DO SUL",
            "TUPANCIRETÃ",
            "TUPARENDI",
            "UNIÃO DA SERRA",
            "URUGUAIANA",
            "VACARIA",
            "VALE DO SOL",
            "VALE REAL",
            "VANINI",
            "VENÂNCIO AIRES",
            "VERA CRUZ",
            "VERANÓPOLIS",
            "VESPASIANO CORREA",
            "VIAMÃO",
            "VICENTE DUTRA",
            "VICTOR GRAEFF",
            "VILA FLORES",
            "VILA MARIA",
            "VISTA ALEGRE",
            "VISTA ALEGRE DO PRATA",
            "VITÓRIA DAS MISSÕES",
            "WESTFALIA",
            "XANGRI-LÁ"]
    def extrairNomeMunicipio(self, bloco):
        # Extrair nome do município com flexibilidade para padrões diferentes
        padrao = re.compile(r'\b(?:' + '|'.join(map(re.escape, self.nomeDosMunicipios)) + r')\b(?! \w)', re.IGNORECASE)
        textoSemDuploEspacamento = re.sub(r'\s+', ' ', bloco )
        correspondencias = padrao.findall(textoSemDuploEspacamento)
        if correspondencias:
            return correspondencias[0]
        else:
            return "Publicado por Gabinete ou afins"
    def escritaDatabase(self, dados):
        with open("2009.json", "r", encoding="utf-8") as file:
            dados_escritos = json.load(file)

        dados_escritos.append(dados)
        with open("2009.json", "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)

    def extrairDados(self, nomeDoArquivo):
        with open(nomeDoArquivo, 'r') as arquivo: 
            texto = arquivo.read()
            padrao = re.compile(r'(NOMEIA|EXONERA )', re.IGNORECASE)

            resultados = padrao.finditer(texto)
        
            for correspondencia in resultados:
                inicio_contexto = max(correspondencia.start() - 150, 0)  
                fim_contexto = min(correspondencia.end() +250, len(texto))  

                # Aqui está armazenado o texto ao redor da palavra encontrada, seja ela nomeação ou exoneração 
                contexto = texto[inicio_contexto:fim_contexto]
                # Chamada do Spacy para extração do nome do nomeado/exonerado

                """print("Correspondência:", correspondencia.group())
                print("Contexto:", contexto)
                print("-----")"""

                # Restante do seu código aqui
                nomeDoMunicipio = self.extrairNomeMunicipio(contexto)
                data = arquivo.name
                data = data[:-4]
                data = data[-10:]
                nomeacao = False
                exoneracao = False
                
                if correspondencia.group(1).lower().strip() in ["nomeia", "resolve nomear", "decide nomear"]:
                    nomeacao = True
                if correspondencia.group(1).lower().strip() in ["exonera", "resolve exonerar", "decide exonerar"]:
                    exoneracao = True 
                
                dados_novos = {
                    "nomeMunicipio": nomeDoMunicipio,
                    "dataPost": data,
                    "haNomeacao": nomeacao,
                    "haExoneracao": exoneracao,
                    #NomeDoQueSofreuAAção
                    
                }
                self.escritaDatabase(dados_novos)
    
    def extraiGeral(self):
        # Atualmente só está estraíndo 2009, que é o que se tem até o momento 
        arquivos = "/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/"
        arquivos = os.listdir("/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/")
        for arq in arquivos:
            arqPath = f'/home/bdebatata/MétodosDeDesenvolvimentoDeSoftware/2023-2-Squad08/WebScraping/txt/2009/{arq}'
            self.extrairDados(arqPath)

"""
regex = ExtratorDeDados()
regex.extraiGeral()"""



