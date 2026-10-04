# Projeto 2 – Painel do Censo Escolar 2024 com Power Query

Painel em Excel que lê a base do Censo Escolar 2024, filtra o município escolhido dentro do Power Query e atualiza todas as tabelas, gráficos e segmentações com um único clique em **Atualizar Tudo**.

Atividade: Análise de Dados para Pesquisas em Políticas Públicas (CGAPN), FGV EAESP, 2º semestre de 2026 (Monitorada 2, Projeto 2).

**Arquivo:** `CENSO_AUTOMATIZADO_COM_POWERQUERY.xlsx`

---

## Objetivo

Construir um painel de infraestrutura e matrículas das escolas de **um município**, a partir dos microdados do Censo Escolar 2024. O painel permite responder, por exemplo:

- Quantas escolas e quantas matrículas existem por dependência administrativa (federal, estadual, municipal, privada)?
- Como as escolas se distribuem por tamanho (Micro, Pequena, Média, Grande)?
- Quais são as condições de água, energia e destinação do lixo nas escolas do município?

A análise do município é refeita automaticamente ao trocar o filtro, sem refazer tabelas dinâmicas ou gráficos.

---

## O que mudou em relação à versão anterior

| | Versão anterior (Aulas 9 e 10) | Esta versão |
|---|---|---|
| Base de dados | Recorte do estado de São Paulo | Base nacional do Censo Escolar 2024, com todos os municípios |
| Escolha do município | Fixa, feita no próprio recorte | Informada em uma tabela de filtro (UF e município) |
| Filtro | Feito antes, fora do Power Query | Feito **dentro do Power Query**, por *Merge* com Junção Interna (*Inner Join*) |
| Atualização | Manual, por partes | Um clique em **Atualizar Tudo** |

O filtro dentro do Power Query faz com que as tabelas dinâmicas e os gráficos trabalhem apenas com as escolas do município escolhido, mesmo que a base de origem tenha centenas de milhares de linhas.

---

## Como funciona

### Consultas do Power Query

| Consulta | Função |
|---|---|
| `Microdados` | Consulta principal. Importa a base, trata os tipos, faz os *merges*, cria as colunas condicionais e aplica o filtro de município |
| `Filtro` | Lê a tabela com UF e município escolhidos (`Coluna1` = sigla da UF, `Coluna2` = município) |
| `Dependencia` | Tabela auxiliar: Federal, Estadual, Municipal, Privada |
| `Localizacao` | Tabela auxiliar: Urbana, Rural |
| `LocDiferenciada` | Tabela auxiliar: Assentamento, Terra indígena, Comunidade quilombola, Comunidades tradicionais |
| `Situacao` | Tabela auxiliar: Ativa, Inativa |

### Etapas da consulta `Microdados`

1. **Importação** da aba `Microdados` por Dados > Obter Dados > De Arquivo > Pasta de Trabalho do Excel, com promoção de cabeçalhos e definição dos tipos de coluna.
2. **Left Join** com `Dependencia` (por `TP_DEPENDENCIA`), trazendo o nome da dependência.
3. **Left Join** com `Localizacao`, trazendo a localização da escola (Urbana ou Rural).
4. **Colunas condicionais**, descritas abaixo.
5. **Inner Join** com `Filtro`, pelos dois campos ao mesmo tempo (`SG_UF` + `NO_MUNICIPIO`). Esta etapa reduz a base ao município escolhido.

### Colunas condicionais

**Tamanho da escola** (coluna `TAM_ESCOLAA`), pelo total de matrículas da educação básica (`QT_MAT_BAS`):

| Faixa | Classificação |
|---|---|
| Até 50 | Micro |
| De 51 a 200 | Pequena |
| De 201 a 500 | Média |
| Acima de 500 | Grande |

**Indicadores de infraestrutura** (Água, Energia, Esgoto e Lixo). Cada indicador usa uma regra de prioridade: vale a primeira coluna binária marcada com `1`, na ordem abaixo.

| Indicador | Ordem de prioridade (primeira marcada com 1) | Se nenhuma estiver marcada |
|---|---|---|
| Água | Rede pública, Potável, Cacimba, Carro-pipa, Rio, Poço artesiano | Inexistente |
| Energia | Rede pública, Gerador fóssil, Renovável | Inexistente |
| Esgoto | Rede pública, Fossa, Fossa comum, Fossa séptica | Inexistente |
| Lixo | Coleta, Enterra, Queima | Outro |

A consulta também traz uma segunda coluna de água (`AGUA`), com a prioridade Potável, Rede pública, Poço artesiano, Cacimba, Rio, Carro-pipa, Inexistente e Outro.

---

## Conteúdo do painel

- **Aba visível:** `Planilha5`, com o título *Dashboard Censo Escolar 2024*.
- **Gráficos dinâmicos:** Escolas por dependência, Matrículas por dependência, Escolas por tamanho, Escolas por energia, Escolas por água e Escolas por lixo.
- **Segmentações de dados:** Dependência, Tamanho da escola, Água, Energia e Lixo.
- **Abas ocultas:** `Microdados` (tabela tratada carregada pelo Power Query), tabelas auxiliares, tabelas de filtro e abas com as tabelas dinâmicas de apoio.

---

## Como usar

1. Abra o arquivo no **Excel para desktop**.
2. Garanta que a consulta encontre a base: o arquivo de origem está referenciado por caminho (`PROJETOOOO 2.xlsx`). Se o arquivo estiver em outra pasta, ajuste em Dados > Obter Dados > Configurações da Fonte de Dados.
3. Na tabela de filtro, informe a **sigla da UF** (por exemplo, `RO`) e o **município** (por exemplo, `Porto Velho`), escrevendo o nome exatamente como aparece no Censo (maiúsculas, minúsculas e acentos).
4. Clique em **Dados > Atualizar Tudo**.
5. Use as segmentações para explorar o painel.

> Para o **Atualizar Tudo** esperar a consulta terminar antes de atualizar as dinâmicas, desmarque "Habilitar atualização em segundo plano" nas propriedades da consulta `Microdados` (Dados > Propriedades da Consulta).

**Município atual no arquivo:** Porto Velho (RO), com 93 escolas carregadas.

---

## Disclaimers

### Inteligência Artificial

A Inteligência Artificial (Claude) foi utilizada para um melhor entendimento das informações dispostas no PDF de instruções para o trabalho e como um auxílio na construção do README. 

### Dados

Os dados são os microdados do **Censo Escolar 2024**, divulgados pelo INEP. As tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação) seguem os códigos do dicionário de variáveis do Censo. Os dados não foram alterados, apenas tratados (tipos, classificações e filtro por município). Os resultados refletem a qualidade e a completude das informações declaradas pelas escolas.

### Participação 

- **Camile:** importação da base e consultas do Power Query.
- **Manuela e Danielle:** colunas condicionais e *merges*.
- **Manuela:** tabelas dinâmicas, gráficos e segmentações.
- **Maria Gabriela:** teste da atualização trocando o município e conferência dos resultados.

---

## Estrutura da pasta

```
projeto-2-com-automacao-powerquery/
├── CENSO_AUTOMATIZADO_COM_POWERQUERY.xlsx
└── README.md
```
