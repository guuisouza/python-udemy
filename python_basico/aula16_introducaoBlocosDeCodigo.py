# if / elif / else
# se / se não se / se não
# Mudam o fluxo do nosso programa
entrada = input("Você quer 'entrar' ou 'sair'? ")

if entrada == 'entrar': 
    print('Você entrou no sistema!')
    print(12341234)
elif entrada == 'sair': 
    print('Você saiu do sistema!')
else:
    print('Você não digitou nem entrar e nem sair!')

print('fora do bloco de código')
