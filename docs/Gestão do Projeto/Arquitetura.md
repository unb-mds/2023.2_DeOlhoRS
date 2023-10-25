# Arquitetura de Software 
### Introdução 
A arquitetura de software é o alicerce estrutural que define a organização, os componentes, as interações e os padrões de um sistema de software. Ela serve como um esqueleto lógico que molda o comportamento e a funcionalidade do sistema, proporcionando uma visão abrangente de como as partes se encaixam para atender aos requisitos do projeto. Através de decisões de design bem ponderadas, a arquitetura orienta o desenvolvimento, a escalabilidade, a manutenção e a evolução contínua do software. Este documento descreve detalhadamente a arquitetura deste sistema, oferecendo uma compreensão completa das escolhas de design, as interações entre os componentes e as diretrizes para o desenvolvimento e a manutenção bem-sucedidos do software.

### Metodologia 
A definição da arquitetura deste projeto foi moldada através de uma análise profunda do comportamento desejado para o software e uma avaliação detalhada dos requisitos que orientam sua concepção. 

### Arquitetura 

Dado o processo de criação, foram desenvolvidos alguns diagramas para a melhor compreensão de uso do software. 

A ideia inicial da arquitetura se baseia em: 

![Arquitetura](https://live.staticflickr.com/65535/53282499672_0a84d0b761_c.jpg) 

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

#### Sobre o armazenamento de dados:

Após uma reunião com um dos membros do projeto que está se usando referência (Projeto [Exoonero](https://github.com/exoonero/extrator)), um dos tópicos mais questionados foi sobre o armazenamento dessa quantia de PDFs, .txt e dados de processamento do Regex. Foi mostrado que é possível realizar esse processo em tempo de execução de código para que não se tenha que armazenar para sempre esses dados, somente usar e apagar. Porém será necessário armazenar uma coisa: um arquivo .json que contém um "resumo" das informações, de onde será retirado os dados para montagem dos displays de dados no site.

### Camada do Site

Para disposição desses dados em um site será utilizado JavaScript e React, como já mencionado no documento de Escolhas Tecnologicas. 

### Diagramas

A partir desse raciocínio e da elicitação de requisitos é possível realizar um diagrama sequencial, que mostra o caminho do usuário ou do software. Caso seja necessário os requisitos estão documentados em [Requisitos](/docs/DesignSprint/Requisitos.md)

Caminho do Usuário, pagina Home:

![home](https://live.staticflickr.com/65535/53259278760_8577f1771a_z.jpg) 

Caminho do Usuário, pagina Sobre:

![sobre](https://live.staticflickr.com/65535/53259288070_57537438b6_z.jpg) 

Caminho do Usuário, pagina Pesquisa Avançada:

![pesquisa](https://live.staticflickr.com/65535/53258792911_ff36a0f79f_z.jpg)

Caminho do Software, camada de dados:

![camada](https://live.staticflickr.com/65535/53260208205_80484f5d80_z.jpg) 


Além disso as tecnologias escolhidas para as implementações desse software estão documentadas em: [Escolhas Tecnológicas](/docs/Tecnologias/EscolhasTecnologicas.md)

## Histórico de Versões

|    Data    | Versão |       Descrição       |      Autor      |
| :--------: | :----: | :-------------------: | :-------------: |
| 8/10/2023 |  0.1   | Abertura do documento | [Bruno Henrique Duarte](https://github.com/bdebatata) e   [Bianca Patrocinio](https://github.com/BiancaPatrocinio7)|
| 9/10/2023 |  0.2   | Acréscimo do detalhamento de cada camada | [Bruno Henrique Duarte](https://github.com/bdebatata) e   [Bianca Patrocinio](https://github.com/BiancaPatrocinio7)|
|09/10/2023|0.3| Arrumando para o build do mkdocs | [Bruno Henrique](https://github.com/bdebatata) |
|10/10/2023|0.4| Atualização da Documentação, Retirada da API do Google Drive | [Bruno Henrique](https://github.com/bdebatata) |
|10/10/2023| 0.5 |Modificações propostas pela equipe | [Bruno Henrique](https://github.com/bdebatata), [Larissa Vieira](https://github.com/VieiraLaris) e [Vitor Feijó](https://github.com/vitorfleonardo) |
|15/10/2023| 0.6 | Correção das imagens no build | [Bruno Henrique](https://github.com/bdebatata) e [Bianca Patrocinio](https://github.com/BiancaPatrocinio7)|
|24/10/2023|0.7|Correção da arquitetura | [Bruno Henrique](https://github.com/bdebatata) |


