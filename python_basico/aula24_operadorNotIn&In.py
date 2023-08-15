# Operadores in e not in
# Strings em Python são iteráveis (Podemos navegar item por item através de indices)
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

# In significa Está Entre e Not In significa Não Está Entre

nome = 'Otávio'
# Acessando o A que está no indice 2
# print(nome[2])
# print(nome[-4])

#Podemos checar se uma letra está naquela string
print('á' in nome)
print('z' in nome)
print(10 * '-')

#Usando o Not In verificamos se algo não está naquele nome
print('vio' not in nome) # Está no nome mas vai retornar falso por causa do Not In
print('zero' not in nome) # True pois não tem zero em nome

# Mais um exemplo
nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')

