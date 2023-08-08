# Crie dois inputs que recebem dois números e realize uma comparação entre eles

primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

# Convertendo para int
int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

# Comparação
if int_primeiro_valor >= int_segundo_valor: 
    print(f'O {int_primeiro_valor=} é maior ou igual que o {int_segundo_valor=}')
else: 
    print(f'O {int_segundo_valor=} é maior que o {int_primeiro_valor=}')
