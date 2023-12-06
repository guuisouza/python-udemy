"""
Listas em Pyhon 
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# .....   01234
# .....  -54321
string = 'ABCDE' # 5 Caracteres (len)
# Temos essas 2 formas de criar uma lista, sendo a segunda a mais comum
lista = list()

#......... 0 .. 1 ...  2 ......   3  .. 4
lista2 = [123, True, 'Guilherme', 1.2, []] # ''
lista2[2] = "Maria" # Mutando o valor, alterando Guilherme para Maria
# Ao acessar o índice de uma lista ele pegará o elemento e não o caractere
print(lista2)
print(lista2[2], type(lista2[2]))
# print(bool(lista2)) # Falsy

# A lista pode ser mudada, você consegue alterar um valor de um índice
