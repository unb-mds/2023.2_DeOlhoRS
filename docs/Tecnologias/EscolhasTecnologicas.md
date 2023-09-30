# Escolhas Tecnológicas 
Durante nossas reuniões de equipe, discutimos constantemente as tecnologias ideais para a implementação das funcionalidades desejadas. Nesse contexto, optamos pelas seguintes tecnologias:

### 1. Python
Dada a ampla utilização da linguagem Python na área de ciência de dados, foi escolhido utilizá-la para a obtenção dos Diários Oficiais, extração de texto e análise.

Para alcançar isso, será empregado as seguintes ferramentas:

- Selenium: Será usado o framework Selenium para automatizar e simular as ações de um usuário no site que disponibiliza os Diários Oficiais, permitindo-nos fazer o download de cada um dos PDFs.
- PyPDF2: Após a extração dos PDFs, será utilizado a biblioteca PyPDF2 para extrair o texto e salvá-lo em um arquivo .txt.
- Regex: Com o arquivo .txt em mãos, será aplicado expressões regulares (Regex) para buscar palavras-chave e estruturas de texto, localizando assim as informações cruciais para o projeto.

### 2. Javascript/React
A escolha do JavaScript com React foi baseada na eficiência na criação de interfaces de usuário e na facilidade de uso. Essa combinação é ideal para implementar gráficos interativos e disposição dinâmica de dados, atendendo aos requisitos do site de forma eficaz.