# 1° Projeto - SIMULADOR PNAE

## Objetivo

O objetivo deste Simulador é simular o cálculo do repasse anual do PNAE (Programa Nacional de Alimentação Escolar) para a escola EMEB Vila Quitaúna, em Osasco/SP, a partir do número de matrículas por modalidade de ensino, do valor per capita diário de cada modalidade e dos dias letivos no ano. O simulador também permite classificar o porte da escola, verificar a elegibilidade para complementação municipal e testar diferentes cenários de variação nas matrículas.
Nesta nova versão, o simulador também conta com uma automação em VBA, que permite registrar cada simulação realizada em uma aba de banco de dados. Dessa forma, além de visualizar os resultados numéricos, é possível guardar a data e horário da simulação, o fator de ajuste utilizado, o racional apresentado pelo usuário e o nome de quem realizou a simulação.

## Como usar

● Para acessar a planilha, clique no arquivo correspondente e, na página que será aberta, selecione “View raw” ou clique no ícone de download, localizado no canto superior direito.

● Abra o arquivo “Simulador-PNAE- automatizado_com_VBA” e habilite a edição e o conteúdo/macros quando solicitado.

● Na aba “Parametros_PNAE”, confira os valores per capita por modalidade e os dias letivos utilizados no cálculo.

● Na aba “Simulador_Escola”, preencha o número de matrículas por modalidade.

● Preencha o campo Usuário com o nome da pessoa que está realizando a simulação.

● Utilize o Fator de Ajuste para testar diferentes cenários de variação nas matrículas.

● No campo Racional da Taxa, explique o motivo pelo qual o fator de ajuste escolhido parece adequado para aquele cenário.

● Confira os resultados calculados, como total de matrículas, porte da escola, repasse anual estimado e elegibilidade para complementação municipal.

● Após preencher os campos necessários, utilize o botão de registro da simulação. A macro irá validar as informações, registrar os dados na aba “Banco_de_Dados” e limpar os campos para que uma nova simulação possa ser realizada.

● A aba “Banco_de_Dados” permite consultar as simulações já realizadas, incluindo o usuário responsável por cada registro.

## Automação em VBA

A automação foi desenvolvida a partir do padrão apresentado em aula e utiliza a macro RegistrarSimulacao para registrar as simulações realizadas no simulador.

A macro realiza as seguintes etapas:

● Lê o Fator de Ajuste, o Racional da Taxa e o Usuário preenchidos na tela do simulador;
● Valida se os campos obrigatórios foram preenchidos;
● Impede o registro quando o campo Usuário estiver vazio;
● Grava as informações em uma nova linha da aba Banco_de_Dados;
● Limpa os campos preenchidos após o registro, permitindo a realização de uma nova simulação.

O banco de dados contém informações como ID, Data/Hora, Fator de Ajuste, Racional da Taxa, Total de Matrículas Ajustadas, Repasse Ajustado e Usuário.

## Prints do resultado:

<img width="718" height="806" alt="Captura de tela 2026-10-04 171242" src="https://github.com/user-attachments/assets/437d1b18-3a2f-40bc-a141-7de08207c58d" />

<img width="1343" height="237" alt="Captura de tela 2026-10-04 171300" src="https://github.com/user-attachments/assets/248bb388-cb75-4917-ae74-10be599a820b" />

## Uso de Inteligência Artificial

Ferramenta utilizada: Claude.
Para que foi usada: A Inteligência Artificial foi utilizada como apoio na criação do artefato HTML interativo desenvolvido na etapa anterior do projeto, reproduzindo as fórmulas e os resultados da planilha em uma interface navegável.
Também foram realizados ajustes manuais na interface, como a alteração da cor dos detalhes do simulador para uma tonalidade roxo-azulada.
Exemplo de prompt utilizado:
“Você vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construí em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).”
A ferramenta foi utilizada como apoio, enquanto os dados, fórmulas e regras utilizados no simulador foram baseados na planilha desenvolvida pelo grupo.

## Fonte de Dados
Fonte: Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026, que altera a Resolução CD/FNDE nº 6/2020.
Link: https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view
O que os dados representam: Os valores per capita diários (R$/dia) repassados por modalidade de ensino no âmbito do PNAE, além dos dias letivos anuais utilizados para calcular o repasse total.
A escola, o bairro (Quitaúna, Osasco/SP) e as matrículas por modalidade são fictícios, criados para fins didáticos. As faixas de porte da escola (Pequena/Média/Grande) também foram criadas apenas para fins didáticos deste curso.
Estrutura:
Modalidade: categoria de ensino (Creche, Pré-escola, Fundamental, Médio, EJA, Indígena/Quilombola e AEE);
Valor per capita (R$/dia): valor diário repassado por aluno matriculado em cada modalidade;
Matrículas: número de alunos matriculados em cada modalidade (dado fictício);
Dias letivos: número de dias letivos no ano (200);
Porte: classificação da escola de acordo com a faixa de matrículas totais.

## Participação do Grupo

O que aprendemos com este projeto: Aprendemos mais sobre o contexto do PNAE e sobre como seus dados e regras podem ser transformados em uma ferramenta de análise. Na prática, aprofundamos o uso do Excel, utilizando fórmulas como SE, E, OU, PROCV e SOMARPRODUTO, além da Tabela de Dados para testar diferentes cenários de matrículas e repasses.
Nesta nova etapa, também aprendemos a utilizar VBA para automatizar o registro das simulações, entendendo como criar, ler, validar, gravar e limpar informações por meio de uma macro.

<img width="718" height="806" alt="Captura de tela 2026-10-04 171242" src="https://github.com/user-attachments/assets/15569891-8c6d-43d8-818e-3a6b99a74b0c" />



