"""
    Argumentos nomeados e não nomeados em funções python
    Argumento nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor) - chamado de posicional
"""

def soma(x, y, z):
# Definição da função
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3) # Argumento posicional, passando 1 para x e 2 para y
soma(y= 2, x= 1, z=3) # Argumento nomeado, passando 2 para y e 1 para x fora da ordem
# Sempre que criar um argumento nomeado os próximos precisam ser nomeados