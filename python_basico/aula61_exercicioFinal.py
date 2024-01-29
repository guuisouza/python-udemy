"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Parte 1 - Gerar/Validar o primeiro digito de um CPF
# Passo 1: Coletar o cpf e pegar os números
cpf_recebido = '74682489070'
nove_digitos = cpf_recebido[0:9]

# Passo 2: somar seus 9 primeiros dígitos multiplicando cada valor por uma contagem regressiva
# Começando a partir do 10
contador_regressivo_1 = 10
soma = 0

for digito in nove_digitos:
    soma += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

# Passo 3: Multiplicar o resultado anterior por 10 e obter o resto da divisão por 11 do resultado anterior
resto_divisao11 = (soma * 10) % 11
# Passo 4: Verificar o valor com IF
primeiro_digito = resto_divisao11 if resto_divisao11 <= 9 else 0
print(primeiro_digito)

