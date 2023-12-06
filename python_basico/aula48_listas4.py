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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Gerando uma nova lista através de concatenação com o +
lista_a.extend(lista_b) # Não retorna nada, faz uma ação mas não entrega um valor de volta, mexe na lista A
print(lista_a)