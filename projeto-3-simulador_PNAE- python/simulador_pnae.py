## PARÂMETROS

# Valores de repasse do PNAE - 2026

valorRepasse_Creche = 1.57
valorRepasse_Preescola = 0.82
valorRepasse_Fundamental = 0.57
valorRepasse_Medio = 0.57
valorRepasse_EJA = 0.57

# Fonte: Resolução CD/FNDE nº 01, de 18 de fevereiro de 2026.



# Custo dos alimentos por refeição
# Fonte: Prefeitura de São Paulo, proposta de 07/08/2025

CUSTO_ALIMENTOS_REFEICAO = 2.67

diasLetivos = 200




## Funções (processo do backend)

# função para validar a entrada de números 
def validaNumero(mensagem):
    numero = input(mensagem)
    
    while not numero.isdigit():
        print("você digitou numero incorreto")
        numero = input(mensagem)
        
    numero = int(numero)
    return numero                    

# função para classoficar o porte da escola por número de matrículas

def classifica_porte(numeroMatriculas):
    if numeroMatriculas <=  50:
        porteEscola = "Micro"
    elif numeroMatriculas <= 200:
        porteEscola = "Pequena"
    elif numeroMatriculas <= 400:
        porteEscola = "Média"
    else: porteEscola = "Grande"

    return porteEscola


# função para calcular o valor que o governo repassará para a escola simuluada

def calculo_repasse(qtdmatriculas, valorUnitario, dias):
    TotalRepasse = qtdmatriculas * valorUnitario * dias
    return TotalRepasse

## esse total repasse é diferente do Repasse_TOTAL do programa princial, esse TotalRepasse é o escopo



def calcula_cobertura(totalMatriculas, dias, repasseTotal, custoRefeicao):

    custoAnual = totalMatriculas * dias * custoRefeicao

    if custoAnual == 0:
        cobertura = 0
        diferenca = 0

    else:
        cobertura = (repasseTotal / custoAnual) * 100

        if repasseTotal >= custoAnual:
            diferenca = 0
        else:
            diferenca = custoAnual - repasseTotal

    return custoAnual, cobertura, diferenca

    
### PROGRAMA PRINCIPAL

print("Olá, bem-vinda(o) ao simulador PNAE")
print()
print("*** DADOS DA ESCOLA ***")
print()

nome = input("Digite o seu nome: ")
escola = input("Digite o nome da sua escola: ")

diasLetivos = validaNumero("Qual a quantidade de dias letivos do ano: ")

print()

### PEDIR AS MATRÍCULAS

print("DIGITAÇÃO DAS MATRÍCULAS")
print()

creche = validaNumero("Digite a quantidade de matrículas na creche: ")
pre_escola = validaNumero("Digite a quantidade de matrículas na pré-escola: ")
fundamental = validaNumero("Digite a quantidade de matrículas no fundamental regular: ")
medio = validaNumero("Digite a quantidade de matrículas no ensino médio regular: ")
eja = validaNumero("Digite a quantidade de matrículas na EJA: ")

print()
print()
print()

### SOMA DAS MATRÍCULAS

totalMatriculas = (creche + pre_escola + fundamental + medio + eja)

### CÁLCULO DOS REPASSES

Repasse_Creche = calculo_repasse(creche, valorRepasse_Creche, diasLetivos)

Repasse_Preescola = calculo_repasse(pre_escola, valorRepasse_Preescola, diasLetivos)

Repasse_Fundamental = calculo_repasse(fundamental, valorRepasse_Fundamental, diasLetivos)

Repasse_Medio = calculo_repasse(medio, valorRepasse_Medio, diasLetivos)

Repasse_EJA = calculo_repasse(eja, valorRepasse_EJA, diasLetivos)


### SOMA DO REPASSE TOTAL

Repasse_TOTAL = (Repasse_Creche + Repasse_Preescola + Repasse_Fundamental
                 + Repasse_Medio + Repasse_EJA)

### CLASSIFICAR O PORTE

porte = classifica_porte(totalMatriculas)

### CÁLCULO DO CUSTO DOS ALIMENTOS

custoAnual, cobertura, diferenca = calcula_cobertura(
    totalMatriculas,
    diasLetivos,
    Repasse_TOTAL,
    CUSTO_ALIMENTOS_REFEICAO
)

### RESULTADOS

print("=== CÁLCULOS ===")
print()

print("Sua Escola é de porte:", porte)
print("Total de matrículas:", totalMatriculas)

print()
print("=== REPASSES DO PNAE ===")

print("Creche: R$", round(Repasse_Creche, 2))
print("Pré-escola: R$", round(Repasse_Preescola, 2))
print("Ensino Fundamental: R$", round(Repasse_Fundamental, 2))
print("Ensino Médio: R$", round(Repasse_Medio, 2))
print("EJA: R$", round(Repasse_EJA, 2))

print()
print("Repasse total: R$", round(Repasse_TOTAL, 2))

print()
print("=== CUSTO DA ALIMENTAÇÃO ESCOLAR ===")

print("Custo dos alimentos por refeição: R$", CUSTO_ALIMENTOS_REFEICAO)
print("Custo anual estimado: R$", round(custoAnual, 2))
print("Cobertura do repasse:", round(cobertura, 2), "%")

if diferenca == 0:
    print("O repasse cobre o custo estimado dos alimentos.")
else:
    print("Diferença a ser coberta por outras fontes: R$", round(diferenca, 2))

print()
print("==== FIM DOS CÁLCULOS ====")
input("Pressione Enter para encerrar...")

