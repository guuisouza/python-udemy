"""
Exercício 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
#  Enumerate: [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')][(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# Enumera a sua lista
lista = ['Maria', 'Helena', 'Luiz']
lista.append("João")

# lista_enumerada = enumerate(lista) # Enumera cada um dos itens ali dentro
# print(lista_enumerada) # Iterator
# print(next(lista_enumerada))

# Geralmente não vamos usar o enumerate em uma variável e sim direto no for
# Conseguimos usar esse enumerate no FOR
for item in enumerate(lista):
    # Para tirar da tupla no print podemos desempacotar
    indice, nome = item
    print(indice, nome)

# Podemos fazer assim também
for indice, nome in enumerate(lista):
    print(indice, nome)

# Mas nem sempre queremos o for, para usar e ver a lista enumerada podemos converter
lista_enumerada = list(enumerate(lista)) # Converte o enumerate pra lista
print(lista_enumerada)

