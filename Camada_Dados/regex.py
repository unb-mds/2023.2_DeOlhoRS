# pylint: disable=missing-module-docstring
import re
import json
import os
# pylint: disable=trailing-whitespace
class ExtratorDeDados:
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=W1514
    # pylint: disable=R0914
    def __init__(self):
        self.nome_dos_municipios = [
                "Aceguá", "Água Santa", "Agudo", "Ajuricaba", "Alecrim", "Alegrete", 
                "Alegria","Almirante Tamandaré do Sul", 
                "Alpestre", "Alto Alegre", "Alto Feliz", "Alvorada", "Amaral Ferrador",
                "Ametista do Sul", "André da Rocha", "Anta Gorda", "Antônio Prado", 
                "Arambaré", "Araricá","Aratiba", "Arroio do Meio", "Arroio do Padre",
                "Arroio do Sal", "Arroio do Tigre","Arroio dos Ratos", "Arroio Grande", 
                "Arvorezinha", "Augusto Pestana", "Áurea", "Bagé",
                    "Balneário Pinhal", "Barão", "Barão de Cotegipe", 
                    "Barão do Triunfo", "Barra do Guarita",
                    "Barra do Quaraí", "Barra do Ribeiro", "Barra do Rio Azul", 
                    "Barra Funda", "Barracão","Barros Cassal", "Benjamin Constan do Sul",
                    "Bento Gonçalves", "Boa Vista das Missões",
                    "Boa Vista do Buricá", "Boa Vista do Cadeado", "Boa Vista do Incra", 
                    "Boa Vista do Sul",
                    "Bom Jesus", "Bom Princípio", "Bom Progresso", 
                    "Bom Retiro do Sul", "Boqueirão do Leão",
                    "Bossoroca", "Bozano", "Braga", "Brochier", "Butiá",
                    "Caçapava do Sul", "Cacequi","Cachoeira do Sul", 
                    "Cachoeirinha", "Cacique Doble", "Caibaté", "Caiçara", "Camaquã",
                    "Camargo", "Cambará do Sul", "Campestre da Serra",
                    "Campina das Missões", "Campinas do Sul", "Campo Bom", 
                    "Campo Novo", "Campos Borges", "Candelária", "Cândido Godói",
                    "Candiota", "Canela", "Canguçu", "Canoas", "Canudos do Vale", 
                    "Capão Bonito do Sul",
                    "Capão da Canoa","Capão do Cipó","Capão do Leão", "Capela de Santana",
                    "Capitão","Capivari do Sul", "Caraá","Carazinho",
                    "Carlos Barbosa","Carlos Gomes","Casca",
                    "Caseiros","Catuípe","Caxias do Sul","Centenário","Cerrito",
                    "Cerro Branco",
                    "Cerro Grande","Cerro Grande do Sul","Cerro Largo","Chapada","Charqueadas",
                    "Charrua","Chiapeta","Chuí","Chuvisca","Cidreira","Ciríaco", "Colinas",
                    "Colorado","Condor","Constantina","Coqueiro Baixo","Coqueiros do Sul",
                    "Coronel Barros","Coronel Bicaco", "Coronel Pilar", "Cotiporã","Coxilha",
                    "Crissiumal",  "Cristal","Cristal do Sul","Cruz Alta","Cruzaltense",
                    "Cruzeiro do Sul","David Canabarro","Derrubadas","Dezesseis de Novembro",
                    "Dilermando de Aguiar","Dois Irmãos","Dois Irmãos das Missões",
                    "Dois Lajeados","Dom Feliciano","Dom Pedrito","Dom Pedro de Alcântara",
                    "Dona Francisca","Doutor Maurício Cardoso","Doutor Ricardo","Eldorado do Sul",
                    "Encantado","Encruzilhada do Sul", "Engenho Velho","Entre Rios do Sul",
                    "Entre-Ijuís", "Erebango", "Erechim", "Ernestina","Erval Grande",
                    "Erval Seco","Esmeralda", "Esperança do Sul", "Espumoso", "Estação",
                    "Estância Velha", "Esteio","Estrela","Estrela Velha","Eugênio de Castro",
                    "Fagundes Varela", "Farroupilha","Faxinal do Soturno",
                    "Faxinalzinho","Fazenda Vilanova","Feliz","Flores da Cunha",
                    "Floriano Peixoto", "Fontoura Xavier",
                    "Formigueiro","Forquetinha", "Fortaleza dos Valos","Frederico Westphalen",
                    "Garibaldi","Garruchos","Gaurama","General Câmara","Gentil","Getúlio Vargas",
                    "Giruá","Glorinha","Gramado","Gramado dos Loureiros",
                    "Gramado Xavier","Gravataí",
                    "Guabiju","Guaíba","Guaporé","Guarani das Missões","Harmonia","Herval",
                    "Herveiras","Horizontina","Hulha Negra","Humaitá","Ibarama","Ibiaçá",
                    "Ibiraiaras","Ibirapuitã","Ibirubá","Igrejinha","Ijuí","Ilópolis","Imbé",
                    "Imigrante","Independência","Inhacorá","Ipê","Ipiranga do Sul","Iraí","Itaara",
                    "Itacurubi","Itapuca","Itaqui","Itati","Itatiba do Sul","Ivorá","Ivoti",
                    "Jaboticaba","Jacuizinho","Jacutinga", "Jaguarão","Jaguari","Jaquirana",
                    "Jari","Jóia","Júlio de Castilhos",
                    "Lagoa Bonita do Sul","Lagoa dos Três Cantos",
                    "Lagoa Vermelha","Lagoão","Lajeado","Lajeado do Bugre",
                    "Lavras do Sul","Liberato Salzano", "Lindolfo Collor","Linha Nova",
                    "Maçambara","Machadinho","Mampituba","Manoel Viana","Maquiné","Maratá", 
                    "Marau","Marcelino Ramos","Mariana Pimentel","Mariano Moro", 
                    "Marques de Souza", "Mata", "Mato Castelhano", "Mato Leitão", "Mato Queimado",
                    "Maximiliano de Almeida", "Minas do Leão", "Miraguaí","Montauri", 
                    "Monte Alegre dos Campos", "Monte Belo do Sul","Montenegro","Mormaço",
                    "Morrinhos do Sul","Morro Redondo", "Morro Reuter", "Mostardas","Muçum",
                    "Muitos Capões", "Muliterno", "Não-Me-Toque", 
                    "Nicolau Vergueiro", "Nonoai", "Nova Alvorada", "Nova Araçá",
                    "Nova Bassano",  "Nova Boa Vista", "Nova Bréscia",  
                    "Nova Candelária", 
                    "Nova Esperança do Sul", "Nova Hartz","Nova Pádua",
                    "Nova Palma","Nova Petrópolis",
                    "Nova Prata", "Nova Ramada", "Nova Roma do Sul", 
                    "Nova Santa Rita", "Novo Barreiro",
                    "Novo Cabrais","Novo Hamburgo", "Novo Machado","Novo Tiradentes","Novo Xingu",
                    "Osório","Paim Filho", "Palmares do Sul","Palmeira das Missões","Palmitinho",
                    "Panambi","Pântano Grande", "Paraí","Paraíso do Sul","Pareci Novo", "Parobé",
                    "Passa Sete","Passo do Sobrado", "Passo Fundo", "Paulo Bento","Paverama",
                    "Pedras Altas","Pedro Osório","Pejuçara", "Pelotas", "Picada Café",
                    "Pinhal", "Pinhal da Serra","Pinhal Grande",
                    "Pinheirinho do Vale","Pinheiro Machado",
                    "Pirapó", "Piratini","Planalto", "Poço das Antas",
                    "Pontão","Ponte Preta", "Portão",
                    "Porto Alegre","Porto Lucena", "Porto Mauá",
                    "Porto Vera Cruz", "Porto Xavier",
                    "Pouso Novo","Presidente Lucena", "Progresso",
                    "Protásio Alves", "Putinga", "Quaraí",
                    "Quatro Irmãos", "Quevedos", "Quinze de Novembro",
                    "Redentora", "Relvado", "Restinga Seca",
                    "Rio dos Índios", "Rio Grande", "Rio Pardo", 
                    "Riozinho", "Roca Sales", "Rodeio Bonito",
                    "Rolador", "Rolante", "Ronda Alta", "Rondinha", 
                    "Roque Gonzales", "Rosário do Sul",
                    "Sagrada Família", "Saldanha Marinho", "Salto do Jacuí", 
                    "Salvador das Missões", "Salvador do Sul",
                    "Sananduva", "Santa Bárbara do Sul", 
                    "Santa Cecília do Sul", "Santa Clara do Sul",
                    "Santa Cruz do Sul", "Santa Margarida do Sul", 
                    "Santa Maria", "Santa Maria do Herval",
                    "Santa Rosa", "Santa Tereza", "Santa Vitória do Palmar",  
                    "Santana da Boa Vista", "Santana do Livramento",
                    "Santiago","Santo Ângelo","Santo Antônio da Patrulha",
                    "Santo Antônio das Missões","Santo Antônio do Palma", 
                    "Santo Antônio do Planalto",
                    "Santo Augusto","Santo Cristo",
                    "Santo Expedito do Sul", "São Borja", 
                    "São Domingos do Sul", "São Francisco de Assis",
                    "São Francisco de Paula", "São Gabriel", 
                    "São Jerônimo", "São João da Urtiga",
                    "São João do Polêsine", "São Jorge", 
                    "São José das Missões", "São José do Herval",
                    "São José do Hortêncio", "São José do Inhacorá", "São José do Norte", 
                    "São José do Ouro", "São José do Sul", "São José dos Ausentes",
                    "São Leopoldo", "São Lourenço do Sul", "São Luiz Gonzaga", "São Marcos",
                    "São Martinho", "São Martinho da Serra", "São Miguel das Missões", 
                    "São Nicolau", "São Paulo das Missões", "São Pedro da Serra", 
                    "São Pedro das Missões", "São Pedro do Butiá", 
                    "São Pedro do Sul", "São Sebastião do Caí", "São Sepé", 
                    "São Valentim", "São Valentim do Sul", "São Valério do Sul",
                    "São Vendelino", "São Vicente do Sul", "Sapiranga", "Sapucaia do Sul",
                    "Sarandi", "Seberi", "Sede Nova", "Segredo", "Selbach", 
                    "Senador Salgado Filho",
                    "Sentinela do Sul", "Serafina Corrêa", "Sério",
                    "Sertão", "Sertão Santana", "Sete de Setembro",
                    "Severiano de Almeida", "Silveira Martins", "Sinimbu",
                    "Sobradinho", "Soledade",
                    "Tabaí", "Tapejara", "Tapera", "Tapes", 
                    "Taquara", "Taquari", "Taquaruçu do Sul",
                    "Tavares", "Tenente Portela", "Terra de Areia", "Teutônia", "Tio Hugo",
                    "Tiradentes do Sul", "Toropi", "Torres", 
                    "Tramandaí", "Travesseiro", "Três Arroios",
                    "Três Cachoeiras", "Três Coroas", "Três de Maio",
                    "Três Forquilhas", "Três Palmeiras",
                    "Três Passos", "Trindade do Sul", "Triunfo", 
                    "Tucunduva", "Tunas", "Tupanci do Sul",
                    "Tupanciretã", "Tupandi", "Tuparendi",
                    "Turuçu", "Ubiretama", "União da Serra",
                    "Unistalda", "Uruguaiana", "Vacaria",
                    "Vale do Sol", "Vale Real", "Vale Verde",
                    "Vanini", "Venâncio Aires", "Vera Cruz", 
                    "Veranópolis", "Vespasiano Correa",
                    "Viadutos", "Viamão", "Vicente Dutra", 
                    "Victor Graeff", "Vila Flores", "Vila Lângaro",
                    "Vila Maria", "Vila Nova do Sul", 
                    "Vista Alegre", "Vista Alegre do Prata",
                    "Vista Gaúcha", "Vitória das Missões", "Westfália", "Xangri-lá"
            ]
    def extrair_nome_municipio(self, bloco):
        # Extrair nome do município com flexibilidade para padrões diferentes
        padrao = re.compile(
            r'\b(?:' + '|'.join(map(re.escape, self.nome_dos_municipios)) + r')\b', re.IGNORECASE)
        correspondencias = padrao.findall(bloco)
        if 'Rio Grande' in correspondencias:
            # Encontrar a posição da palavra "Rio Grande" no texto
            posicao_rio_grande = bloco.find('Rio Grande')
            # Verificar se a palavra "do Sul" segue "Rio Grande"
            if posicao_rio_grande != -1 and bloco[posicao_rio_grande +
                                                  len('Rio Grande'):].strip().startswith('do Sul'):
                return correspondencias[1]
            return "Rio Grande"
        return "Publicado por Gabinete ou afins"
    def escrita_data_base(self, dados, arquivo):
        print(arquivo)
        with open(arquivo, "r", encoding="utf-8") as file:
            dados_escritos = json.load(file)
        dados_escritos.append(dados)
        with open(arquivo, "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)
    def extrair_dados(self, nome_do_arquivo, arq_salvo):
        with open(nome_do_arquivo, 'r') as arquivo: 
            texto = arquivo.read()
            padrao = re.compile(r'(NOMEIA|EXONERA )', re.IGNORECASE)
            resultados = padrao.finditer(texto)
            for correspondencia in resultados:
                inicio_contexto = max(correspondencia.start() - 400, 0)  
                fim_contexto = min(correspondencia.end() + 400, len(texto))  
                contexto = texto[inicio_contexto:fim_contexto]
                print("Contexto:", contexto)
                nome_do_municipio = self.extrair_nome_municipio(contexto)
                data = arquivo.name
                data = data[:-4]
                data = data[-10:]
                nomeacao = False
                exoneracao = False
                if correspondencia.group(1).lower().strip() in ["nomeia",
                                                                "resolve nomear", 
                                                                "decide nomear"]:
                    nomeacao = True
                if correspondencia.group(1).lower().strip() in ["exonera", 
                                                                "resolve exonerar", 
                                                                "decide exonerar"]:
                    exoneracao = True 
                dados_novos = {
                    "nomeMunicipio": nome_do_municipio,
                    "dataPost": data,
                    "haNomeacao": nomeacao,
                    "haExoneracao": exoneracao,   
                }
                self.escrita_data_base(dados_novos, arq_salvo)
    def extrai_geral(self, ano_extraido, arq_salvo):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        arquivos = os.listdir(f'{diretorio_atual}/txt/{ano_extraido}/')
        for arq in arquivos:
            arq_path = f'{diretorio_atual}/txt/{ano_extraido}/{arq}'
            self.extrair_dados(arq_path, arq_salvo)
