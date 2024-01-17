# Desempacotamento em chamadas
# de funções e métodos
string = 'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = "python", "é", "legal"
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2            3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40) ],  # 2
]

# a, b, *_, ap, u  = lista
# print(a, ap, u)

# for nome in lista:  
#     print(nome, end=' ')

# É possível desempacotar direto no print
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')