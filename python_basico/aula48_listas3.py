"""
Listas em Pyhon 
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item no final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append("Guilherme")
ultimo = lista.pop()
lista.append(1233)
del lista[-1] # Deleta o ultimo item usando o -1
lista.insert(0, 5) # Insere no index desejado
print(lista, ultimo)