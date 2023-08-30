"""
Introdução ao Try & Except
try -> tentar executar determinado código
except -> ocorreu um erro ao tentar executar
estourar uma excessão ou aparecer uma exceção significa que estamos vendo um erro
try catch do python é o try except

o IF não evita erros de ocorrerem

"""

numero_str = input("Digite um número: ")

try: 
    numero_float = float(numero_str) # Se ocorrer um erro aqui ele já pula pro except
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except: 
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
# else: 
#     print('Isso não é um número')