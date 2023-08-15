"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: A funçao len retorna a quantidade
de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[4:8])
print(variavel[0:len(variavel):2])
print(variavel[::-1]) # Inverte a string

