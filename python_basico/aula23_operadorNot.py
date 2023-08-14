# Operador lógico "not"
# É usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

# Com o ! invertemos a lógica da condição, será aceito qualquer senha diferente de 123456
if senha != '123456':
    print('entrou')
else:
    print('Senha incorreta!')

# Falsy
print(0)

# Verdadeiro pois usamos o not para inverter o valor bool
print(not 0)

print(not True) #False
print(not False) #True