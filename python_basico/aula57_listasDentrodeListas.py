"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2            3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40) ],  # 2
]

# print(salas[0][1]) # Busca o valor helena que está dentro de uma lista na lista Salas
# print(salas[2][2]) # Busca o valor eduarda
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)