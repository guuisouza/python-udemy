"""
Exercício 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append("Bell")
lista.append("João")
indices = range(len(lista))

for nome in indices:
    print(nome, lista[nome])
    

