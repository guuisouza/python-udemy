"""
Cuidados com dados mútaveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# É possível coletar valores de variáveis mutaveis
nome = 'Lucas'
salvando_antes = nome
nome = 'Guilherme'
print(salvando_antes)
print(nome)

# Mas agora com lista
lista_a = ['Luis', 'Maria']
lista_b = lista_a # Não está copiando a lista A para a lista B, está fazendo esses 2 apelidos apontarem
# para um mesmo valor na memória!!!

# Para realmente fazer um copy podemos fazer o seguinte:
lista_c = lista_a.copy()
print(lista_c)

lista_a[0] = 'Qualquer coisa' # VAI modificar o valor da lista B, mesmo mexendo apenas na A
print(lista_b)

