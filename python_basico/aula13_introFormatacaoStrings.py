nome = 'Guilherme Souza'
altura = 1.76
peso = 62.3
imc = peso / (altura**2)

# usando o f conseguimos usar váriaveis dentro de um texto
# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'   
linha_2 = f'pesa {peso} quilos e seu imc é'
imc = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(imc)
# print('Seu nome é:', nome)
# print('Você tem:', altura, "metros de altura")
# print('Você pesa:', peso, "Kg")
# print('Seu IMC é:', imc)






