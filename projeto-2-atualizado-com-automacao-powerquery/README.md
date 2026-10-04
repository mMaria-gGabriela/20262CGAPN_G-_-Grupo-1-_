# Projeto 2 – Painel do Censo Escolar 2024 com Power Query

Painel em Excel que lê a base do Censo Escolar 2024, filtra o município escolhido dentro do Power Query e atualiza todas as tabelas, gráficos e segmentações com um único clique em **Atualizar Tudo**. Atividade: Análise de Dados para Pesquisas em Políticas Públicas (CGAPN), FGV EAESP, 2º semestre de 2026 (Monitorada 2, Projeto 2).

---

## Objetivo

Construir um painel de infraestrutura e matrículas das escolas de **um município**, a partir dos microdados do Censo Escolar 2024. O painel permite responder, por exemplo:

- Quantas escolas e quantas matrículas existem por dependência administrativa (federal, estadual, municipal, privada)?
- Como as escolas se distribuem por tamanho (Micro, Pequena, Média, Grande)?
- Quais são as condições de água, energia e destinação do lixo nas escolas do município?

A análise do município é refeita automaticamente ao trocar o filtro, sem refazer tabelas dinâmicas ou gráficos.

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

### Prints do resultado: 

## Disclaimers

### Inteligência Artificial

A Inteligência Artificial (Claude) foi utilizada para um melhor entendimento das informações dispostas no PDF de instruções para o trabalho e como um auxílio na construção do README. 

### Fonte de Dados

Os dados são os microdados do **Censo Escolar 2024**, divulgados pelo INEP. As tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação) seguem os códigos do dicionário de variáveis do Censo. Os dados não foram alterados, apenas tratados (tipos, classificações e filtro por município). Os resultados refletem a qualidade e a completude das informações declaradas pelas escolas.

### Participação 

- **Camile:** importação da base e consultas do Power Query.
- **Manuela e Danielle:** colunas condicionais e *merges*.
- **Manuela:** tabelas dinâmicas, gráficos e segmentações.
- **Maria Gabriela:** teste da atualização trocando o município e conferência dos resultados.
