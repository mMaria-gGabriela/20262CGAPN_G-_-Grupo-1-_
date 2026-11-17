# Projeto 3 – Simulador do Programa Nacional de Alimentação Escolar (PNAE)

## Objetivo

Desenvolver um simulador em Python capaz de calcular uma estimativa dos recursos financeiros repassados pelo Governo Federal às escolas públicas por meio do Programa Nacional de Alimentação Escolar (PNAE). O programa considera a quantidade de matrículas por etapa de ensino, os valores per capita do PNAE e os dias letivos para calcular o repasse anual.

Além disso, o simulador estima o custo anual dos gêneros alimentícios utilizados nas refeições escolares e compara esse valor com o repasse federal, apresentando o percentual de cobertura e a diferença que precisaria ser complementada por outras fontes de recursos.

## Como usar

Para utilizar o simulador, é necessário ter o Python instalado no computador e salvar o código em um arquivo chamado `simulador_pnae.py`.

A execução pode ser feita pelo terminal, utilizando o comando:

```bash
python simulador_pnae.py
```

Ao iniciar, o programa solicitará algumas informações ao usuário:

1. Nome do usuário;
2. Nome da escola;
3. Quantidade de dias letivos do ano;
4. Quantidade de matrículas na creche;
5. Quantidade de matrículas na pré-escola;
6. Quantidade de matrículas no Ensino Fundamental;
7. Quantidade de matrículas no Ensino Médio;
8. Quantidade de matrículas na Educação de Jovens e Adultos (EJA).

As respostas referentes às quantidades devem ser números inteiros, sem letras ou caracteres especiais. Caso seja digitada uma informação inválida, o programa solicitará novamente a entrada.

Depois de preencher os dados, o simulador realizará os cálculos e apresentará o porte da escola, os valores de repasse por etapa de ensino, o repasse total, o custo anual estimado dos alimentos, o percentual de cobertura e a diferença entre o custo e o repasse federal.

## Prints do resultado

<img width="1279" height="822" alt="Captura de tela 2026-11-17 151151" src="https://github.com/user-attachments/assets/e2dfbcd5-79cc-480b-bba0-04bb0e2a1c39" />


<img width="1279" height="858" alt="image" src="https://github.com/user-attachments/assets/0617004a-0b3d-4818-8d7e-f18b4d6a0b3d" />



## Escola simulada

Para a realização da simulação, foi escolhida a **EMEF Celso Leite Ribeiro Filho**, uma escola pública municipal localizada no município de São Paulo, no estado de São Paulo.

| Informação                 | Dados                          |
| -------------------------- | ------------------------------ |
| Nome                       | EMEF Celso Leite Ribeiro Filho |
| Código INEP                | 35053041                       |
| Município                  | São Paulo                      |
| UF                         | SP                             |
| Dependência administrativa | Municipal                      |
| Situação de funcionamento  | Em funcionamento               |
| Ano dos dados              | 2024                           |

### Matrículas por etapa de ensino

| Etapa de ensino    | Quantidade de matrículas |
| ------------------ | -----------------------: |
| Creche             |                        0 |
| Pré-escola         |                        0 |
| Ensino Fundamental |                      805 |
| Ensino Médio       |                        0 |
| EJA                |                       77 |
| **Total**          |                  **882** |

### Fonte e coleta dos dados

As informações foram obtidas diretamente da planilha Excel dos microdados do **Censo Escolar de 2024**, disponibilizada pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

Para localizar a escola, foi realizada uma busca na base de dados utilizando seu nome e código INEP. Após sua identificação, foram consultadas as informações referentes à dependência administrativa, à situação de funcionamento e à quantidade de matrículas por etapa de ensino.

Os dados utilizados correspondem às matrículas registradas no Censo Escolar de 2024. As etapas não oferecidas pela instituição foram consideradas com quantidade igual a zero.

**Fonte oficial:** [INEP – Microdados do Censo Escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar).

## Custo dos alimentos

Para estimar o custo dos alimentos utilizados em uma refeição escolar, foi consultada uma proposta de preços publicada no Diário Oficial da Cidade de São Paulo, referente ao Pregão Eletrônico nº 31/SME/2023, Lote 13 – Santo Amaro, com proposta datada de 7 de agosto de 2025.

O documento apresenta a separação entre os valores destinados aos gêneros alimentícios e os custos relacionados à mão de obra e a outros serviços.

Para uma refeição porcionada destinada às EMEFs, sem sobremesa, foram identificados os seguintes valores:

| Componente                  | Valor por refeição |
| --------------------------- | -----------------: |
| Gêneros alimentícios        |            R$ 2,67 |
| Mão de obra e outros custos |            R$ 0,78 |
| **Valor total**             |        **R$ 3,45** |

Para o simulador, foi adotado o valor de **R$ 2,67 por refeição**, correspondente exclusivamente aos gêneros alimentícios.

A escolha desse valor foi feita porque o objetivo do projeto é comparar o repasse do PNAE com o custo dos alimentos, e não com o custo total da prestação do serviço de alimentação escolar. Por isso, não foram incluídos os gastos com mão de obra, logística, equipamentos, infraestrutura e outros serviços.

**Fonte:** [Diário Oficial da Cidade de São Paulo – Proposta de preços, Pregão Eletrônico nº 31/SME/2023](https://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?hxgCDmL4t6jFh0JZRMIxGUVP2t3pAmubyY5cgLWodEdxcqz-6QwNaxhah8zowbrIoHNydE5hOlrovIzv3UGyIYxsypn9LFeKiiPm3mKKQ119PHv6vtFZIKCx7_zOVWmu).

**Data da proposta consultada:** 7 de agosto de 2025.

### Ressalvas sobre a fonte

O valor utilizado é uma referência de preço, não o custo efetivamente pago pela escola escolhida. A proposta foi elaborada para o Lote 13 – Santo Amaro, e não especificamente para a EMEF Celso Leite Ribeiro Filho.

Além disso, o documento apresenta um valor de R$ 2,62 para os gêneros alimentícios de uma refeição porcionada da EJA, diferente dos R$ 2,67 identificados para a refeição de EMEF. Para manter um único parâmetro no simulador, foi utilizado R$ 2,67 para todas as matrículas.

Dessa forma, o custo calculado representa uma estimativa baseada em uma referência pública de preços, podendo apresentar diferenças em relação aos valores efetivamente praticados pela escola.

## Resultados e reflexão

### Resultados da simulação

Para realizar a simulação, foram considerados os dados de matrícula da EMEF Celso Leite Ribeiro Filho, 200 dias letivos e o custo de R$ 2,67 por refeição.

Os valores per capita utilizados para o cálculo do repasse foram os estabelecidos para 2026 pelo FNDE:

| Etapa de ensino    | Valor por aluno/dia |
| ------------------ | ------------------: |
| Creche             |             R$ 1,57 |
| Pré-escola         |             R$ 0,82 |
| Ensino Fundamental |             R$ 0,57 |
| Ensino Médio       |             R$ 0,57 |
| EJA                |             R$ 0,57 |

O cálculo do repasse considera a quantidade de matrículas multiplicada pelo valor per capita correspondente à etapa de ensino e pelos dias letivos.

**Repasse do Ensino Fundamental:**

805 × R$ 0,57 × 200 = R$ 91.770,00.

**Repasse da EJA:**

77 × R$ 0,57 × 200 = R$ 8.778,00.

**Repasse total estimado: R$ 100.548,00.**

Para o custo anual dos alimentos, foi utilizada a quantidade total de matrículas, multiplicada pelos dias letivos e pelo custo de R$ 2,67 por refeição:

882 × 200 × R$ 2,67 = R$ 470.988,00.

O percentual de cobertura é calculado dividindo o repasse total pelo custo anual estimado dos alimentos e multiplicando o resultado por 100.

| Indicador                          |     Resultado |
| ---------------------------------- | ------------: |
| Total de matrículas                |           882 |
| Porte da escola                    |        Grande |
| Repasse total do PNAE              | R$ 100.548,00 |
| Custo dos alimentos por refeição   |       R$ 2,67 |
| Custo anual estimado dos alimentos | R$ 470.988,00 |
| Cobertura do repasse federal       |        21,35% |
| Diferença estimada                 | R$ 370.440,00 |

Os resultados indicam que o repasse federal representa aproximadamente 21,35% do custo anual estimado dos gêneros alimentícios. A diferença de R$ 370.440,00 corresponde à parcela do custo que não é coberta pelo repasse federal, considerando os parâmetros adotados.

### Reflexão

A realização da simulação permite compreender que o financiamento da alimentação escolar não depende exclusivamente dos recursos transferidos pelo Governo Federal. O PNAE possui caráter suplementar, ou seja, os valores federais devem ser complementados pelos estados e municípios para garantir a oferta de alimentação adequada aos estudantes.

A Nota Técnica do Todos Pela Educação, publicada em março de 2023, destaca a importância do financiamento do programa e a necessidade de atualização dos valores per capita, considerando as diferenças econômicas e sociais entre os municípios. Essa questão é relevante porque os custos dos alimentos variam entre as regiões, e municípios com menor capacidade financeira podem enfrentar maiores dificuldades para complementar os recursos federais.

O artigo publicado pelo Observatório da Alimentação Escolar em 21 de outubro de 2025 também chama atenção para os desafios do financiamento da alimentação escolar. A discussão evidencia que a falta de recursos suficientes pode comprometer a qualidade e a variedade dos alimentos oferecidos, além de dificultar a implementação das diretrizes do programa, como a valorização da agricultura familiar e a oferta de refeições saudáveis.

Já o material publicado pelo Brasil de Fato em 16 de outubro de 2025 aborda as dificuldades relacionadas ao financiamento da alimentação escolar e as desigualdades existentes entre os municípios. Essa discussão reforça que a capacidade de complementar os recursos federais não é igual em todas as localidades, o que pode gerar diferenças nas condições de oferta das refeições aos estudantes.

No caso da escola analisada, a simulação mostra que o repasse federal cobre aproximadamente 21,35% do custo estimado dos alimentos. Caso a diferença não seja complementada pelo município ou por outras fontes de financiamento, pode haver dificuldades para manter a quantidade, a variedade e a qualidade das refeições oferecidas aos alunos. Isso pode comprometer o direito à alimentação adequada e afetar as condições de aprendizagem e permanência dos estudantes na escola.

É importante destacar que o simulador apresenta algumas simplificações. Primeiramente, são utilizadas matrículas referentes ao Censo Escolar de 2024, enquanto os valores per capita do repasse correspondem a 2026. Essa escolha foi feita com a intenção de manter o simulador o mais atualizado possível. Dessa forma, uma pessoa que utilize os dados do Censo de 2024 poderá obter uma estimativa com os valores mais recentes disponíveis, enquanto alguém que utilize dados de 2025 em diante também poderá utilizar o programa sem precisar alterar os parâmetros do repasse, desde que mantenha os valores vigentes.

Além disso, o cálculo considera as etapas de ensino cadastradas no programa, sem contemplar todas as modalidades e condições especiais de atendimento previstas nas regras do PNAE. Por fim, a estimativa considera apenas uma refeição por aluno por dia letivo, utilizando um único custo de referência para todas as etapas. Na prática, a quantidade de refeições e os custos podem variar conforme a etapa de ensino, a jornada escolar e as características da unidade.

Portanto, os resultados devem ser interpretados como uma estimativa simplificada, e não como o custo exato da alimentação escolar ou o valor efetivamente recebido pela instituição.

## Organização do programa

O programa foi organizado em parâmetros, funções e programa principal, mantendo a estrutura utilizada no simulador desenvolvido no Projeto 1 e acrescentando uma nova função para estimar o custo dos alimentos e a cobertura do repasse.

| Função / parte do programa                                              | O que faz                                                                                                                   | Correspondência com o Projeto 1                                                |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `validaNumero(mensagem)`                                                | Verifica se o usuário digitou um número inteiro válido, solicitando novamente a informação caso a entrada esteja incorreta. | Função de validação de entrada de dados.                                       |
| `classifica_porte(numeroMatriculas)`                                    | Classifica o porte da escola de acordo com a quantidade total de matrículas.                                                | Função de classificação do porte da escola.                                    |
| `calculo_repasse(qtdmatriculas, valorUnitario, dias)`                   | Calcula o repasse anual de cada etapa de ensino, utilizando matrículas, valor per capita e dias letivos.                    | Função de cálculo do repasse do PNAE.                                          |
| `calcula_cobertura(totalMatriculas, dias, repasseTotal, custoRefeicao)` | Calcula o custo anual estimado dos alimentos, o percentual de cobertura do repasse e a diferença entre os valores.          | Nova função acrescentada no Projeto 3.                                         |
| Programa principal                                                      | Solicita os dados da escola, chama as funções, reúne os resultados e apresenta as informações ao usuário.                   | Programa principal do simulador do Projeto 1, com novos cálculos e resultados. |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** ChatGPT (OpenAI).

**Para que foi usada:** A ferramenta foi utilizada como apoio durante o desenvolvimento do projeto, principalmente para o ensinamento da ferramenta "round" no código em Python, identificar possíveis erros e em auxilio para fazer tabelas aqui no _readme_.

**Exemplo de prompt utilizado:**

"chat me ensine a usar o round no python e veja se da forma que eu usei está certinho. Caso esteja errado me ensine a concertar e o que essa ferramenta faz",
"chat como que faz tabelas no sistema markdown do github", "chat me ajude a arrumar esse readme as tabelas ficaram erradas e organize ele para que fique mais facil de entender"

**O que foi ajustado manualmente:** O grupo conferiu as informações apresentadas do round, revisou o código.

## Fonte de Dados

**Fontes oficiais:**

- Censo Escolar 2024 – Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).
- Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026 – Fundo Nacional de Desenvolvimento da Educação (FNDE).

**Links oficiais:**

- [INEP – Microdados do Censo Escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar).
- [FNDE – Resolução CD/FNDE nº 1/2026](https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf).

**O que os dados representam:** Os dados do Censo Escolar representam informações sobre as escolas de educação básica do Brasil, incluindo identificação, dependência administrativa, situação de funcionamento e quantidade de matrículas por etapa de ensino. Para este projeto, foram utilizados os registros da EMEF Celso Leite Ribeiro Filho referentes ao ano de 2024.

**Estrutura – informações utilizadas:**

| Informação                 | Significado                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------- |
| Código INEP                | Identificador único da escola na base do Censo Escolar.                                 |
| Nome da escola             | Nome oficial da instituição de ensino.                                                  |
| Município e UF             | Localização da escola.                                                                  |
| Dependência administrativa | Indica se a escola é federal, estadual, municipal ou privada.                           |
| Situação de funcionamento  | Indica se a escola está em funcionamento.                                               |
| Matrículas por etapa       | Quantidade de estudantes matriculados em cada etapa de ensino considerada no simulador. |

**Valores de repasse:** Foram utilizados os valores per capita estabelecidos pelo FNDE para 2026, com a intenção de manter o simulador atualizado e permitir sua utilização com diferentes anos de referência do Censo Escolar.

**Custo dos alimentos:** Foi adotado o valor de R$ 2,67 por refeição, com base na proposta de preços publicada no Diário Oficial da Cidade de São Paulo em 7 de agosto de 2025, referente aos gêneros alimentícios de uma refeição porcionada de EMEF.

## Participação do Grupo

### O que aprendemos com este projeto

Com este projeto, aprendemos a adaptar um simulador desenvolvido anteriormente para uma nova finalidade, acrescentando cálculos e funções em Python. Também aprofundamos nossos conhecimentos sobre o funcionamento do PNAE, os critérios de repasse dos recursos federais e a importância de comparar o financiamento público com os custos da alimentação escolar.

Além disso, aprendemos a consultar e interpretar os microdados do Censo Escolar, identificar uma escola real na base do INEP e utilizar informações públicas para construir uma simulação. Por fim, compreendemos melhor a importância de documentar as fontes utilizadas, justificar as escolhas metodológicas e reconhecer as limitações dos resultados apresentados pelo programa.

### Papel de cada integrante

| Integrante     | Responsabilidade                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Camile         | Organização dos parâmetros do simulador, pesquisa dos valores per capita do PNAE e conferência das informações da legislação.                        |
| Danielle       | Pesquisa e seleção da escola pública utilizada na simulação, consulta dos dados de matrícula no Censo Escolar e conferência das informações do INEP. |
| Manuela        | Desenvolvimento e revisão das funções em Python, incluindo os cálculos do repasse e a classificação do porte da escola.                              |
| Maria Gabriela | Pesquisa do custo dos alimentos por refeição, análise da fonte de preços e realização dos cálculos de cobertura e diferença.                         |
| Henrique       | Testes do programa, conferência dos resultados, organização do README e revisão final do projeto.                                                    |
