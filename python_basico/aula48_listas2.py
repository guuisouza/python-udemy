"""
Listas em Pyhon 
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# #Podemos pegar o valor de uma lista e jogar em uma variável
# numero = lista[2]
# # Podemos mudar o valor de uma lista para um novo
# lista[2] = 300
# print(lista[2])
# # Podemos deletar o valor de uma lista com a func del
# del lista[2] - Cuidado ao usar o del, se tiver uma lista muito grande altera o indice de TODOS os elementos
# print(lista[2])
# Adicionando mais coisas na lista - append
lista.append(50) # Adiciona no FINAL da lista
ultimo_valor = lista.pop()
lista.append(60) # Adiciona no FINAL da lista
lista.append(70) # Adiciona no FINAL da lista
# Removendo coisas na lista - pop
ultimo_valor = lista.pop(3) # Pode passar indices ao POP para ele remover
print(lista, "Removido: ", ultimo_valor)
