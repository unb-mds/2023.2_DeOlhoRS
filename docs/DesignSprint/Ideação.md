# Esboço/ideação e votação

## Introdução

No contexto da Design Sprint, a fase de Esboço/Ideação e Votação consiste na análise de possíveis problemas que podem surgir no projeto, além de procurar possíveis soluções para os mesmos. A ideia dessa fase é que, durante a reunião, todos os membros tirem um tempo para, individualmente, procurarem soluções. Após isso, eles compartilham o que encontraram com o resto da equipe. Sendo assim, todos podem discutir sobre a viabilidade das soluções encontradas.

## Possíveis problemas para o projeto

No início da reunião, elencamos os problemas que podemos ter no desenvolvimento do projeto, esses foram:

* **Existência de dados não estruturados** - durante nossas pesquisas, percebemos que alguns pdf's não são selecionáveis (aparentam ser uma imagem);

* **Existência de diários oficiais em formatos diferentes** - encontramos muitos sites dos diários oficiais dos municípios e os pdf's fornecidos por eles não apresentavam um padrão;

* **Armazenamento dos pdf's** - nos preocupamos com essa parte de obtenção de dados porque, se os pdf's forem baixados, muito armazenamento será gasto;

* **Dificuldade em usar bibliotecas** - no momento dessa reunião, ainda não possuimos um conhecimento consolidado sobre as bibliotecas que usaremos, então acreditamos que podemos encontrar obstáculos ao utilizá-las;

* **Tempo de obtenção/tempo gasto** - dependendo da forma que os pdf's forem baixados, muito tempo dos membros pode ser gasto. Por exemplo, não é viável os membros os baixarem manualmente.

## Possíveis soluções

Após alguns minutos pesquisando soluções, acreditamos que essas são as mais viáveis:

* **Pesquisar e filtrar os pdf's estruturados:** procurar sites em que os pdf's estão estruturados;

* **Automatizar o download dos pdf's:** devido ao problema citado anteriormente relacionado ao tempo (tempo de obtençao/tempo gasto), acreditamos que automatizar esse processo facilitará bastante o processo;

## Outras considerações

* Imaginamos que o fluxo de tecnologias que utilizaremos será o seguinte:
    
    1. Spiders -> para conseguir os links dos pdf's que utilizaremos;
    2. PyPDF2 -> para conseguir os arquivos .txt referentes aos pdf's;
    3. Regex -> para filtrar os dados que utilizaremos;

* Sabendo que teremos que usar os diários oficiais de vários municípios, precisaremos usar o site geral de diários oficiais do Rio Grande do Sul;

* Vamos usar como referência o projeto da [exoonero](https://exoonero.org/) porque podemos usar muitas coisas do repositório como base. [Repositório da exoonero](https://github.com/exoonero/exoonero.github.io).
