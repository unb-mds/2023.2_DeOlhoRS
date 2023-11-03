# Junção Obtenção dos pdfs e Extração de texto


## Metodologia 

Como forma de integrar as etapas do projeto e torná-lo mais eficiente, foi criado um bot com Selenium que consegue baixar de forma automatizada os pdfs do site dos diários oficiais do Rio Grande do Sul. Após isso, ele coloca os pdfs em um diretório dentro da própria máquina do usuário. Em seguida, ele extrai as informações com PyPdf2 e as transforma em um arquivo .txt para melhor análise dos dados. Por fim, o programa exclui os pdfs por não precisar armazenar uma quantidade tão extensa de dados.

Após muitos testes, o programa está funcionando bem. O PyPdf2 cria um novo arquivo .txt, junta as informações de cada página do pdf com um append e para com o final do arquivo.

A próxima etapa será incluir no programa o Regex, que fará a mineração dos dados necessários e salvará em um arquivo compacto para análise. O Regex deverá buscar por nomes, CPFs e datas relacionados a exonerações e nomeações em diferentes municípios do RS ao longo dos anos.

## Desafios

Alguns obstáculos para a junção dos dois métodos foi o formato das datas. Exemplo: 2011-01-20, foi preciso buscar um método para formatar cada dia e mês com 2 dígitos, para o programa poder reconhecer o path do arquivo. Em seguida, percebemos que o diário oficial é lançado em um dia, porém seus carimbos oficiais são do dia anterior e ficou decidido que o diário baixado possui a data anterior. Esses problemas foram solucionados com alguns ajustes no algoritmo em Python.

Outro desafio foi a leitura do pdf até o final. De início ficou implementado um método com while, mas os pdfs possuíam tamanhos variados e esse método não funcionava bem para o programa.


