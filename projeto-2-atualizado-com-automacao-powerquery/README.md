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

1. Abra o arquivo `CENSO_AUTOMATIZADO_COM_POWERQUERY.xlsx` no Excel para desktop;
2. Na tabela de filtro, informe a sigla da UF (por exemplo, RO) e o município (por exemplo, Porto Velho), escrevendo o nome como aparece no Censo;
3. Clique em Dados > Atualizar Tudo;
4. Use as segmentações para explorar o painel.

O município que está no arquivo atualmente é Porto Velho (RO), com 93 escolas.

*OBS.: Há abas ocultadas na planilha

## Prints do resultado:

<img width="1916" height="772" alt="Captura de tela 2026-10-04 195339" src="https://github.com/user-attachments/assets/d3b2f887-9a5a-4dc4-a4f2-1939c743c460" />


<img width="466" height="268" alt="image" src="https://github.com/user-attachments/assets/2e9de705-7f77-489e-bb07-da9c36dbd40a" />


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
- **Maria Gabriela:** teste da atualização trocando o município e conferência dos resultados.]
