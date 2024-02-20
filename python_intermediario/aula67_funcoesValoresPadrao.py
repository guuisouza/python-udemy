"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado
Refatorar: editar o seu código.
"""

# Parametros nomeados também precisam que o restante em sua sequência
# Seja nomeado também
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}, {y=}, {z=}', '|', 'x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
soma(1, 2, 0)
soma(y=9, z= 0, x=7)
soma(2, 3)
