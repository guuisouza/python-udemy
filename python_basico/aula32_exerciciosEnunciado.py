"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um número inteiro: ")
# numero_inteiro = int(numero)

# if (numero_inteiro % 2 == 0):
#     print(f'O número "{numero}" é par')
# elif (numero_inteiro % 2 != 0):
#     print(f'O número "{numero}" é impar')
# else: 
#     print("Você não digitou um número inteiro")

# Melhorando

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0: 
        print(f'O número "{numero_inteiro}" é par')
    else:
        print(f'O número "{numero_inteiro}" é impar')
else:
    print("Você não digitou um número inteiro!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Nos diga a hora: ")


# if hora.isdigit():
#     hora_inteira = int(hora)
#     if (hora_inteira >= 0 and hora_inteira <= 11): 
#         print("Bom Dia!")
#     elif (hora_inteira >= 12 and hora_inteira <= 17):
#         print("Boa Tarde!")
#     else:
#         print("Boa Noite")
# else:
#     print("Digite um valor váido")

# Melhorando

entrada = input("Digite a hora em números inteiros: ")

try:
    hora = int(entrada)
    if (hora >= 0 and hora <= 11):
        print("Bom Dia!")
    elif (hora >= 12 and hora <= 17):
        print("Boa Tarde!")
    elif (hora >= 18 and hora <= 23): 
        print("Boa Noite!")
    else: 
        print("Não conheço essa hora")
except:
    print("Por favor digite apenas números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# primeiro_nome = input("Nos diga seu primeiro nome: ")

# if primeiro_nome:
#     if (len(primeiro_nome) > 0 and len(primeiro_nome) < 5):
#         print("Seu nome é curto!")
#     elif (len(primeiro_nome) >4 and len(primeiro_nome) <7):
#         print("Seu nome é normal!")
#     else: 
#         print("Seu nome é muito grande!")
# else: 
#     print("Por favor digite alguma coisa")

# Melhorado

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')