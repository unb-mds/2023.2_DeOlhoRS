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

Tal esboço de um diagrama de pacotes representa os pacotes necessários para a implementação do projeto. Uma camada de dados, onde serão extraídos e convertidos em dados utéis os textos dos Diarios Oficiais, uma camada da API do Google Drive, onde serão armazenados esses documentos, uma camada para o site, que será dividido em Frontend e Backend.

A partir desse raciocínio e da elicitação de requisitos é possível realizar um diagrama sequencial, que mostra o caminho do usuário ou do software. 

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






