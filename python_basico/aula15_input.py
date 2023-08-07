# nome = input('Qual é o seu nome? ')
# print(f'O seu nome é {nome} ')

# ATENÇÃO!!!
# Colocar o tipo int abaixo já convertendo na entrada do usuário,
# Pode causar transtornos, se o usuário digitar um texto por exemplo,
# Irá gerar um erro já na primeira linha sem o programador ver o que ele digitou,
# Pode ser usado mas é bom evitar "numero_1 = int(input('Digite um número: '))"
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Uma ideia é criar uma nova variável para receber essas de input e converte-las após o usuário digitar
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')