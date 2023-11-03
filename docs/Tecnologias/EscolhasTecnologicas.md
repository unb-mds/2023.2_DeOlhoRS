# Escolhas Tecnológicas 

## Introdução

Para este artefato, o objetivo foi fornecer uma visão abrangente das escolhas tecnológicas feitas para o nosso projeto. As decisões relacionadas à tecnologia desempenham um papel crucial no desenvolvimento bem-sucedido de qualquer iniciativa. Portanto, é essencial entender as razões por trás das seleções feitas, bem como os benefícios e desafios associados a cada escolha.

## Metodologia 

Durante as reuniões de equipe, foi discutido constantemente as tecnologias ideais para a implementação das funcionalidades desejadas. Então foi identificada as necessidades tecnológicas e feitas pesquisas para solucionar essas necessidades. Nesse contexto, optamos pelas seguintes tecnologias:

### 1. [Python](https://docs.python.org/pt-br/3.10/index.html) <img src='https://skillicons.dev/icons?i=python' alt="Python" width="20"></img> 
  
Dada a ampla utilização da linguagem Python na área de ciência de dados, foi escolhido utilizá-la para a obtenção dos Diários Oficiais, extração de texto e análise.

Para alcançar isso, será empregado as seguintes ferramentas:

- [Selenium](https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/): Será usado o framework Selenium para automatizar e simular as ações de um usuário no site que disponibiliza os Diários Oficiais, permitindo-nos fazer o download de cada um dos PDFs.
- [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/): Após a extração dos PDFs, será utilizado a biblioteca PyPDF2 para extrair o texto e salvá-lo em um arquivo .txt.
- [Regex](https://docs.python.org/3/library/re.html): Com o arquivo .txt em mãos, será aplicado expressões regulares (Regex) para buscar palavras-chave e estruturas de texto, localizando assim as informações cruciais para o projeto.

### 2. [TypeScript](https://devdocs.io/typescript/) <img src='https://skillicons.dev/icons?i=typescript' alt="JavaScript" width="20"></img> / [React](https://react.dev/reference/react) <img src='https://skillicons.dev/icons?i=react' alt="React" width="20"></img> 

A escolha do TypeScript com React foi baseada na eficiência na criação de interfaces de usuário e na facilidade de uso. Essa combinação é ideal para implementar gráficos interativos e disposição dinâmica de dados, atendendo aos requisitos do site de forma eficaz. Ademais, o TypeScript é uma extensão do JavaScript que adiciona tipagem estática e aprimora a eficiência do desenvolvedor, além de seguir o paradigma de programação orientada a objetos e ser compatível com diversos ambientes de desenvolvimento, trazendo diversas vantagens para o desenvolvimento do projeto.