# Arquitetura de Software 
### Introdução 
A arquitetura de software é o alicerce estrutural que define a organização, os componentes, as interações e os padrões de um sistema de software. Ela serve como um esqueleto lógico que molda o comportamento e a funcionalidade do sistema, proporcionando uma visão abrangente de como as partes se encaixam para atender aos requisitos do projeto. Através de decisões de design bem ponderadas, a arquitetura orienta o desenvolvimento, a escalabilidade, a manutenção e a evolução contínua do software. Este documento descreve detalhadamente a arquitetura deste sistema, oferecendo uma compreensão completa das escolhas de design, as interações entre os componentes e as diretrizes para o desenvolvimento e a manutenção bem-sucedidos do software.

### Metodologia 
A definição da arquitetura deste projeto foi moldada através de uma análise profunda do comportamento desejado para o software e uma avaliação detalhada dos requisitos que orientam sua concepção. 

### Arquitetura 

Dado o processo de criação, foram desenvolvidos alguns diagramas para a melhor compreensão de uso do software. 

A ideia inicial da arquitetura se baseia em: 

<div align="center"> 
    <img src="/site/assets/images/diagramaDePacotes.png" width="400" />
</div>

Tal esboço de um diagrama de pacotes representa os pacotes necessários para a implementação do projeto.

### Camada de Dados

Nesta camada serão realizadas 3 etapas fundamentais para o desenvolvimento: 

1. Extração dos Diarios Oficiais
Para se analizar os municipios e o estado como um todo é preciso que se tenha, primeiramente, o arquivo PDF do estado/municipio. Usando então da ferramenta Selenium é possível simular os cliques de um usuário na plataforma online e então salvar esses arquivos.

2. Extração do Texto
Para que seja possível o computador processar os dados que estão nos arquivos é necessário que eles estejam de forma estruturada. Já que usando de ferramentas como o PyPDF2 é possível extrair o texto desses arquivos em formatos .txt.

3. Regex
A busca por expressões regulares vai ser o que vai procurar de forma automatizada nos arquivos .txt dados importantes, como quantidade de nomeações, exonerações, pessoas que foram exoneradas.

4. Database
Com as informações agora desta forma, estes dados serão salvos em um arquivo .json para fácil acesso e manipulação pelas camadas a seguir.

### API do Google Drive

O ultimo tópico traz uma problemática grande quando pensado no armazenamento. Usando o Rio Grande do Sul como exemplo, são arquivos desde 2009 todos os dias menos finais de semana e sendo sempre atualizados, para armazenar esses dados enquanto são processados pela camada de dados, foi escolhido se usar uma API do Google Drive que permite salva-los na Nuvem do Google. 

### Camada do Site

Para disposição desses dados em um site será utilizado JavaScript e React, como já mencionado no documento de Escolhas Tecnologicas. 

### Diagramas

A partir desse raciocínio e da elicitação de requisitos é possível realizar um diagrama sequencial, que mostra o caminho do usuário ou do software. Caso seja necessário os requisitos estão documentados em [Requisitos](/docs/DesignSprint/Requisitos.md)

<details>
    <summary>Caminho do usuário, página Home:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/home.png" width="400" />
</div>
</details>

<details>
    <summary>Caminho do usuário, página Sobre:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/sobre.png" width="400" />
</div>
</details>

<details>
    <summary>Caminho do usuário, página de Pesquisa Avançada:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/pesquisa.png" width="400" />
</div>
</details>

<details>
    <summary>Caminho do software, webscraping:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/webscraping.png" width="400" />
</div>
</details>

<details>
    <summary>Caminho do software, PyPDF2:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/PyPDF.png" width="400" />
</div>
</details>

<details>
    <summary>Caminho do software, Regex:
    </summary>
    <div align="center"> 
    <img src="/site/assets/images/regex.png" width="400" />
</div>
</details>

Além disso as tecnologias escolhidas para as implementações desse software estão documentadas em: [Escolhas Tecnológicas](/docs/Tecnologias/EscolhasTecnologicas.md)

## Histórico de Versões

|    Data    | Versão |       Descrição       |      Autor      |
| :--------: | :----: | :-------------------: | :-------------: |
| 8/10/2023 |  0.1   | Abertura do documento | [Bruno Henrique Duarte](https://github.com/bdebatata) e   [Bianca Patrocinio](https://github.com/BiancaPatrocinio7)|
| 9/10/2023 |  0.2   | Acréscimo do detalhamento de cada camada | [Bruno Henrique Duarte](https://github.com/bdebatata) e   [Bianca Patrocinio](https://github.com/BiancaPatrocinio7)|




