"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# print(id(v1)) #Ver a identidade de um elemento na memória
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')

else: 
    print('Não faça algo')

print(passou_no_if, passou_no_if is not None)

# is None (Não passou no if)
if passou_no_if is None:
    print('Não passou no if')

# is not None (Passou no if então não é none)
if passou_no_if is not None:
    print('Passou no if')