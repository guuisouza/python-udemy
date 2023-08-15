"""
Interpolação básica de Strings - Mesma coisa que fizemos com o format mas de um jeito diferente
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)
"""

nome = 'Guilherme'
preco = 1000.956784
# variavel = 'Guilherme, o preço é R$preco'
# Usando a interpolação (%)
variavel = '%s, o preço é R$%.2f' % (nome, preco)
# Acima passamos as reespectivas variáveis no %()
print(variavel)
print('O hexadecimal de %d é %08x' %(1500, 1500))