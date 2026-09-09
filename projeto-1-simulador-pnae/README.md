
# 1° Projeto - SIMULADOR PNAE
Objetivo: O objetivo deste Simulador é simular o cálculo do repasse anual do PNAE (Programa Nacional de Alimentação Escolar) para a escola EMEB Vila Quitaúna, em Osasco/SP, a partir do número de matrículas por modalidade de ensino, do valor per capita diário de cada modalidade e dos dias letivos no ano, além de classificar o porte da escola, verificar a elegibilidade para complementação municipal e permite testar cenários de variação nas matrículas.

#### Como usar:

● Para acessar a planilha, clique no arquivo correspondente e, na página que será aberta, selecione “View raw” ou clique no ícone de download, localizado no canto superior direito.

● Abra o arquivo “Simulador_att7_MGESS.xlsx”, para melhor a experiência habilite a edição da planilha; 

● Na aba parâmetros PNAE, confira os valores per capita por modalidade (Resolução CD/FNDE nº 1/2026) e os dias letivos do ano; 

● Na aba “Simulador Escola” , preencha o número de matrículas por modalidade;

● Confira os resultados calculados: total de matrículas, porte da escola, repasse anual estimado e elegibilidade para complementação municipal;

● Para testar cenários, ajuste o "Fator de Ajuste",  veja o total de matrículas e o repasse recalculados; 

● Abra o arquivo simulador pnae.html no navegador


#### Prints do resultado:

<img width="1347" height="508" alt="Captura de tela 2026-09-08 161225" src="https://github.com/user-attachments/assets/60b4b7f8-062b-4952-bd25-fa1d58831bc6" />


<img width="1642" height="890" alt="Captura de tela 2026-09-08 161254" src="https://github.com/user-attachments/assets/1080c5c1-be89-4ea9-9f61-fa20b32d47f7" />


## Uso de Inteligência Artificial
Ferramenta utilizada: A Inteligência Artificial escolhida foi a Claude 
Para que foi usada: Foi utilizada para gerar o artefato HTML interativo do simulador, reproduzindo as fórmulas e os resultados da planilha “Simulador_att7_MGESS.xls” em uma interface navegável 
Exemplo de prompt utilizado: 
“Você vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construi em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).

Anexei dois arquivos:

1. Minha planilha Excel, com as abas Parametros_PNAE e Simulador_Escola, contendo os dados e as fórmulas.

2. Um arquivo modelo.html, que é um artefato sobre um assunto totalmente diferente (cálculo do valor atual, matemática financeira). Não use nada do conteúdo desse arquivo — nenhum dado, nenhuma fórmula, nenhum texto dele. Use apenas como referência de: paleta de cores e tipografia, formato dos cards e das tabelas, e o tipo de mecânica interativa (campos editáveis no topo, um botão que avança passo a passo reconstruindo uma tabela de resultados, valores que reagem em tempo real a mudanças nos parâmetros).
O que o artefato deve reproduzir, fielmente ao que está na minha planilha:

● Uma tabela de referência com os parâmetros do PNAE (modalidades e valores per capita), extraída da aba Parametros_PNAE.

● Os dados da minha escola (nome, bairro, município) e a tabela de matrículas por modalidade, com campos editáveis para o número de matrículas.

● O cálculo automático de: total de matrículas, porte da escola (a mesma regra de classificação por faixas que está na minha planilha), repasse anual estimado, e o
resultado da regra de elegibilidade para complementação municipal (se ela existir na minha planilha).

● A simulação com o parâmetro de ajuste que criei na Tabela de Dados do Excel: um campo editável para esse fator, mostrando como matrículas e repasse mudam em tempo real.

● Um mecanismo com botões que percorre, passo a passo, os mesmos cenários que estão na minha Tabela de Dados do Excel, reconstruindo a tabela de resultados cenário a cenário — não apenas mostrando o resultado final de uma vez.

Regras importantes:

● Use os dados reais da minha planilha (nome da escola, matrículas, valores per capita, faixas de classificação, fórmulas). Não invente números nem modalidades que não estejam na minha planilha.

● Siga o mesmo estilo visual do modelo.html anexado: paleta de cores, tipografia, formato dos cards, dos botões e da mecânica de "avançar".

● O artefato deve ser um único arquivo HTML, sem dependências externas (sem CDN, sem chamadas à internet, sem fontes externas), porque será usado sem acesso à web.

● Reproduza as fórmulas da minha planilha com a mesma lógica (soma, PROCV, SOMARPRODUTO, SE aninhado com E/OU, e o fator de ajuste usado na Tabela de Dados) — não simplifique nem troque por uma lógica diferente da que eu construí.

● Ao final, liste rapidamente quais células da minha planilha inspiraram cada parte do artefato (preciso disso para documentar o uso de IA no portfólio do GitHub, junto com este prompt) ”

O que foi ajustado manualmente: Pedimos para a ferramenta IA - Claude mudar a cor dos detalhes do simulador para a cor roxo-azulado.
Prompt: "claude altere a cor dos detalhes no site para a cor roxa-azulado"




## Fonte de Dados
Fonte: Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026 (que altera a Resolução CD/FNDE nº 6/2020) — reajuste médio de 14,35% em relação a 2025, valores em vigor desde a primeira parcela de 2026.
Link: https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view
O que os dados representam: os valores per capita diários (R$/dia) repassados por modalidade de ensino no âmbito do PNAE, além dos dias letivos anuais usados para calcular o repasse total. A escola, o bairro (Quitaúna, Osasco/SP) e as matrículas por modalidade são fictícios, criados para fins didáticos; as faixas de porte da escola (Pequena/Média/Grande) também foram criadas apenas para fins didáticos deste curso.
Estrutura:
Modalidade: Categoria de ensino (Creche, Pré-escola, Fundamental, Médio, EJA, Indígena/Quilombola, AEE)
Valor per capita (R$/dia): Valor diário repassado por aluno matriculado em cada modalidade
Matrículas: Número de alunos matriculados em cada modalidade (dado fictício)
Dias letivos:  Número de dias letivos no ano (200)
Porte: Classificação da escola por faixa de matrículas totais

## Participação do Grupo
O que aprendemos com este projeto: Aprendemos mais sobre o contexto do PNAE e como seus dados e regras podem ser transformados em uma ferramenta de análise. Na prática, aprendemos a usar o Excel de forma mais completa, utilizando fórmulas como SE, E, OU, PROCV e SOMARPRODUTO, além da Tabela de Dados, para fazer os cálculos e testar diferentes cenários de matrículas e repasses.

## Papel de cada integrante:
Criar o repositório e organizar as pastas: Maria Gabriela e Danielle

Projeto 1 (arquivos e readme): Camile e Manuela Fasti

Projeto 2 (arquivos e readme): Camile e Henrique

Registro no Eclass: Maria Gabriela

