# 20262CGAPN_G -Grupo-1- Portfólio da disciplina Análise de Dados para Pesquisas em Políticas Públicas (CGAPN) — 2º Semestre 2026, Professora Érica Siqueira.

# Portfólio de Análise de Dados para Pesquisas em Políticas Públicas

### 2026.2 | CGAPN | Grupo 1 | FGV

Este repositório reúne os projetos desenvolvidos por **Camile Vitória, Danielle Mickaelly, Henrique Silva, Manuela Fasti e Maria Gabriela**, durante o segundo semestre de 2026, na disciplina de **Análise de Dados para Pesquisas em Políticas Públicas (CGAPN)**, ministrada pela professora Érica Siqueira.

O portfólio tem como objetivo documentar e compartilhar os conhecimentos adquiridos ao longo da disciplina, demonstrando como ferramentas de análise de dados podem ser aplicadas à interpretação de informações e ao apoio à tomada de decisões no contexto das políticas públicas.

Ao longo dos projetos, foram exploradas diferentes ferramentas e linguagens de programação, como Excel, Power Query e Python, além de técnicas de tratamento, organização, análise e visualização de dados. Os exercícios práticos também permitiram compreender como informações públicas podem ser transformadas em indicadores, simulações e painéis que auxiliam na identificação de problemas e na compreensão de diferentes realidades.

Mais do que apresentar os resultados finais, este repositório registra a evolução do aprendizado do grupo, desde a construção de simuladores e dashboards até o desenvolvimento de aplicações interativas em Python.

---

## Projetos desenvolvidos

### Projeto 1 — Simulador de Repasse do PNAE (Excel)

O primeiro projeto consiste na construção de um simulador em Excel para calcular o repasse financeiro anual do **Programa Nacional de Alimentação Escolar (PNAE)** destinado à EMEB Vila Quitaúna.

O simulador utiliza os valores per capita e as regras de cálculo estabelecidas pela Resolução CD/FNDE nº 1/2026, considerando a quantidade de matrículas por etapa de ensino e os dias letivos do ano.

Para desenvolver a ferramenta, foram utilizadas funções do Excel, como PROCV, SE aninhado com E/OU e SOMARPRODUTO, além de uma Tabela de Dados, que permite testar diferentes cenários a partir da alteração do número de matrículas.

O projeto também conta com um artefato HTML interativo, desenvolvido com apoio de Inteligência Artificial, que reproduz os cálculos do simulador em uma interface de navegação mais acessível.

**Principais ferramentas e conhecimentos aplicados:**

- Fórmulas e funções do Excel;
- Condições lógicas e cálculos automatizados;
- Simulação de diferentes cenários;
- Aplicação de regras de financiamento de políticas públicas.

### Projeto 2 — Dashboard do Censo Escolar (Excel e Power Query)

O segundo projeto consiste na construção de um dashboard a partir dos microdados do **Censo Escolar da Educação Básica de 2024**, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

O painel foi desenvolvido com foco nas escolas do município de São Paulo e permite explorar diferentes indicadores educacionais por meio de tabelas dinâmicas, gráficos dinâmicos e segmentações de dados.

Entre as informações apresentadas estão as condições de infraestrutura das escolas, como abastecimento de água, fornecimento de energia elétrica, esgotamento sanitário e destinação do lixo. Também são analisadas a distribuição das escolas por zona da cidade, a rede de Centros de Educação Infantil (CEIs) e as características das matrículas por cor/raça, sexo e faixa etária.

O tratamento e a organização da base foram realizados por meio do Power Query, permitindo estruturar os dados para a construção das visualizações.

**Principais ferramentas e conhecimentos aplicados:**

- Power Query para tratamento e organização de dados;
- Tabelas e gráficos dinâmicos;
- Segmentação de dados e filtros;
- Construção de indicadores educacionais;
- Visualização e interpretação de dados públicos.

### Projeto 3 — Simulador do PNAE (Python)

No terceiro projeto, o simulador desenvolvido inicialmente em Excel foi adaptado e ampliado utilizando a linguagem Python.

O programa permite estimar os recursos financeiros repassados pelo Governo Federal às escolas públicas por meio do PNAE, considerando a quantidade de matrículas por etapa de ensino, os valores per capita estabelecidos pelo FNDE e os dias letivos.

Além de calcular o repasse federal, o simulador incorpora uma nova funcionalidade: a estimativa do custo anual dos gêneros alimentícios utilizados nas refeições escolares. Com isso, é possível comparar o custo estimado dos alimentos com os recursos transferidos pelo Governo Federal, identificando o percentual de cobertura do repasse e a diferença que precisaria ser complementada por outras fontes de financiamento.

Para demonstrar a aplicação do programa, foi utilizada como referência a EMEF Celso Leite Ribeiro Filho, localizada no município de São Paulo, com informações de matrícula obtidas no Censo Escolar de 2024.

O projeto também permite refletir sobre o caráter suplementar do financiamento do PNAE e sobre a importância da participação dos estados e municípios na garantia da alimentação escolar.

**Principais ferramentas e conhecimentos aplicados:**

- Programação em Python;
- Criação e utilização de funções;
- Validação de entradas de dados;
- Estruturas condicionais e cálculos automatizados;
- Utilização de dados públicos do Censo Escolar;
- Estimativa de custos e análise de cobertura de recursos públicos.

### Projeto 4 — Painel Interativo do Censo Escolar (Python)

O quarto projeto amplia o trabalho iniciado no Dashboard do Censo Escolar (Projeto 2), transferindo a construção do painel do Excel para o ambiente Python.

**O painel interativo reúne informações de escolas em atividade, distribuídas em 30 municípios de quatro regiões do estado de São Paulo**: Região Metropolitana de São Paulo, Baixada Santista, Litoral Norte e Vale do Ribeira.

Desenvolvido com as bibliotecas pandas e Streamlit, o programa permite explorar os dados por meio de filtros de região, localização (urbana ou rural) e porte da escola (micro, pequena, média ou grande).

A partir das opções selecionadas, os indicadores, gráficos, mapas e tabelas são atualizados automaticamente, permitindo observar diferenças entre as regiões e identificar características da infraestrutura e da distribuição das escolas.

Entre os elementos disponíveis estão a quantidade de escolas, o total de matrículas, a distribuição por porte e dependência administrativa, as condições de abastecimento de água, a destinação do lixo e a localização geográfica das instituições em um mapa.

Uma das principais novidades em relação ao Projeto 2 é a inclusão de um mapa com a localização das escolas, além da ampliação da abrangência territorial da análise.

**Principais ferramentas e conhecimentos aplicados:**

- Python e biblioteca pandas;
- Streamlit para desenvolvimento de aplicações interativas;
- Carregamento e organização de arquivos CSV;
- Criação de funções e colunas calculadas;
- Filtros dinâmicos e indicadores;
- Gráficos e visualização geográfica de dados;
- Análise comparativa entre regiões e municípios.
---

## Como navegar pelo repositório

O repositório está organizado em pastas independentes, uma para cada projeto. Cada pasta possui seu próprio README, com explicações específicas sobre os objetivos, o desenvolvimento, as ferramentas utilizadas e os resultados obtidos.

Para conhecer melhor cada trabalho, basta acessar a pasta correspondente:

- **Projeto 1:** Simulador de Repasse do PNAE (Excel).
- **Projeto 2:** Dashboard do Censo Escolar (Excel e Power Query).
- **Projeto 3:** Simulador do PNAE (Python).
- **Projeto 4:** Painel Interativo do Censo Escolar (Python).

Os READMEs individuais também apresentam capturas de tela dos resultados, explicações sobre a utilização dos programas, fontes de dados, reflexões sobre os resultados e os três registros de transparência exigidos pela disciplina:

1. **Inteligência Artificial:** ferramentas utilizadas como apoio, exemplos de prompts e ajustes realizados manualmente pelo grupo.
2. **Fonte de Dados:** origem das informações utilizadas, links de acesso e explicação sobre os dados trabalhados.
3. **Participação do Grupo:** divisão das atividades e conhecimentos adquiridos durante o desenvolvimento.

Dessa forma, o repositório funciona não apenas como um espaço para armazenamento dos projetos, mas também como um registro do processo de aprendizagem desenvolvido ao longo da disciplina, reunindo as ferramentas, técnicas e conhecimentos aplicados pelos alunos na análise de dados voltada às políticas públicas.

