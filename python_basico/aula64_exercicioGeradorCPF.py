"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
for _ in range(100): # GERANDO 100 CPFS
    # Aqui vamos gerar numeros de CPF aleatóriamente
    import random
    # Utilizando o random pra gerar números de forma aleatória de 0 a 9
    # Nosso algoritmo abaixo irá gerar os últimos 2 digitos da forma correta sempre
    # Gerando asssim cpfs validos
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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

    # Segunda etapa - Segundo dígito
    dez_digitos = nove_digitos + str(primeiro_digito)

    contador_regressivo_2 = 11
    soma2 = 0

    for digito in dez_digitos:
        soma2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    resto_digito2_divisao11 = (soma2 * 10) % 11
    segundo_digito = resto_digito2_divisao11 if resto_digito2_divisao11 <= 9 else 0
    print(segundo_digito)

    cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado_pelo_calculo)
