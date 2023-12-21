"""
split e join com list e str
split - divide uma string
join - une uma string 
strip - corta os espaços do inicio e do final de uma string
rstrip - corta os espaços somente da direita
lstrip - corta os espaços somente da esquerda
"""
# Métodos das strings
# Split aceita um parâmetro para saber onde voce quer dividir

frase = 'Olha só que    , coisa interessante   '
lista_de_palavras = frase.split(',')

lista_de_palavras_fixed = [] # A melhor prática é não alterar uma lista mutavel
for i, frase in enumerate(lista_de_palavras):
    lista_de_palavras_fixed.append(lista_de_palavras[i].strip())

# print(lista_de_palavras)
# print(lista_de_palavras_fixed)

# Join - Passa um separador, que é onde será unido e no parametro
# Temos o iterador, podendo ser str, lista ou tupla
frases_unidas = ', '.join(lista_de_palavras_fixed)
print(frases_unidas)