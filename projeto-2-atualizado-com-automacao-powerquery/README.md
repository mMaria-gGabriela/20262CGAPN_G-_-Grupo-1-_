# 2° Projeto - PAINEL DO CENSO ESCOLAR 2024

## Objetivo

Construir um painel de infraestrutura e matrículas das escolas de **um município**, a partir dos microdados do Censo Escolar 2024. O painel permite responder, por exemplo:

- Quantas escolas e quantas matrículas existem por dependência administrativa (federal, estadual, municipal, privada)?
- Como as escolas se distribuem por tamanho (Micro, Pequena, Média, Grande)?
- Quais são as condições de água, energia e destinação do lixo nas escolas do município?

A análise do município é refeita automaticamente ao trocar o filtro, sem refazer tabelas dinâmicas ou gráficos.

## Automação em Power Query

O painel foi desenvolvido a partir do padrão apresentado nas Aulas 9 e 10 e utiliza o Power Query para importar a base do Censo Escolar 2024, filtrar o município escolhido pelo grupo e atualizar todo o painel com um único clique em **Atualizar Tudo**.

O que mudou em relação à versão anterior:

● A base deixou de ser o recorte de São Paulo e passou a ser a base nacional do Censo Escolar 2024, com todos os municípios do Brasil;

● O município passou a ser informado em uma tabela de filtro (UF e município);

● O filtro passou a ser feito dentro do Power Query, por Merge com Junção Interna (Inner Join) entre a consulta principal e a tabela de filtro, pelos campos UF e Município ao mesmo tempo. Assim, o painel trabalha apenas com os dados do município escolhido.

O Power Query realiza as seguintes etapas:

● Importa a base e as tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação);

● Define os tipos de cada coluna;

● Faz Merges com Junção Esquerda Externa (Left Join) para trazer a descrição da Dependência e da Localização;

● Cria a coluna condicional Tamanho da Escola (Micro até 50 matrículas, Pequena até 200, Média até 500 e Grande acima de 500);

● Cria os indicadores de infraestrutura Água, Energia, Esgoto e Lixo, usando a primeira coluna binária marcada com 1, na ordem de prioridade definida;

● Filtra a base pelo município escolhido (Inner Join).

O painel contém tabelas dinâmicas, gráficos dinâmicos (Escolas por Dependência, Matrículas por Dependência, Escolas por Tamanho, Escolas por Energia, Escolas por Água e Escolas por Lixo) e segmentações de dados (Dependência, Tamanho da Escola, Água, Energia e Lixo).

### Como usar

O painel foi construído a partir de uma planilha-base com os dados do Censo Escolar 2024, utilizada pelo Power Query para gerar e atualizar os dados apresentados no painel. Por isso, para trocar o estado ou município analisado, é necessário ter acesso à planilha-base utilizada pelo projeto, pois é dela que o Power Query busca os dados.

Para utilizar o painel:

1. Abra o arquivo CENSO_AUTOMATIZADO_COM_POWERQUERY.xlsx no Excel para desktop;

2. Certifique-se de que a planilha-base do Censo Escolar 2024 utilizada pelo projeto está disponível no local indicado nas consultas do Power Query;

3. Na tabela de filtro, informe a sigla da UF (por exemplo, RO) e o município (por exemplo, Porto Velho), escrevendo o nome exatamente como aparece na base do Censo;

4. Clique em Dados > Atualizar Tudo;

5. O Power Query irá buscar os dados correspondentes na planilha-base, filtrar o estado e o município selecionados e atualizar automaticamente as tabelas, gráficos e indicadores do painel;

6. Use as segmentações para explorar os resultados.

Importante: a alteração da UF e do município só funcionará corretamente se a planilha-base estiver disponível, pois o painel não possui todos os dados do Censo armazenados diretamente nele. A planilha-base é a fonte utilizada pelo Power Query para realizar a atualização dos dados. Portanto, caso a pessoa queira analisar outro estado ou município, deverá manter essa base disponível e, se necessário, ajustar o caminho da fonte de dados nas consultas do Power Query.

O município que está no arquivo atualmente é Porto Velho (RO), com 93 escolas.

OBS.: Há abas ocultadas na planilha.

## Prints do resultado:

<img width="1278" height="659" alt="image" src="https://github.com/user-attachments/assets/fedda90a-9935-4f85-b1a5-965441af74b1" />



## Uso de Inteligência Artificial

A Inteligência Artificial (Claude) foi utilizada como apoio na redação deste README, a partir do arquivo da planilha e das instruções do Projeto 2.

## Fonte de Dados
Fonte: Censo Escolar 2024, do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), disponível no seguinte link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar.  Os dados apresentam nformações de cada escola do Brasil, como dependência administrativa, localização, situação de funcionamento, condições de infraestrutura (água, energia, esgoto e lixo) e número de matrículas. Os dados não foram alterados, apenas tratados no Power Query (tipos, classificações e filtro por município). As faixas de tamanho da escola (Micro/Pequena/Média/Grande) foram definidas para fins didáticos deste curso.
Estrutura:
Dependência: Federal, Estadual, Municipal ou Privada;
Localização: Urbana ou Rural;
Matrículas (QT_MAT_BAS): número de matrículas da educação básica;
Tamanho da escola: classificação de acordo com a faixa de matrículas;
Água, Energia, Esgoto e Lixo: tipo de infraestrutura da escola, conforme a ordem de prioridade das colunas binárias.

## Participação do Grupo

O que aprendemos com este projeto: Aprendemos a importar uma base grande no Power Query e a filtrá-la antes de montar o painel, de modo que apenas os dados do município escolhido sejam processados. Na prática, aprofundamos o uso de Merges com Junção Interna e Junção Esquerda Externa, de colunas condicionais, de tabelas dinâmicas, gráficos dinâmicos e segmentações de dados. Também aprendemos a atualizar o painel inteiro com um clique, trocando o município na tabela de filtro.

### Papel de cada integrante: 


- **Camile:** importação da base e consultas do Power Query.
- **Danielle e Manuela:** colunas condicionais e *merges*.
- **Manuela:** tabelas dinâmicas, gráficos e segmentações.
- **Maria Gabriela:** teste da atualização trocando o município e conferência dos resultados.
