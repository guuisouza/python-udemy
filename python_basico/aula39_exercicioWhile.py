
# """
# Iterando strings com while
# """
# #       012345678910
# nome = 'Luiz Otávio' # Iteráveis
# #       1110987654321
# tamanho_nome = len(nome) # Pegando o tamanho do nome
# print(nome)
# print(tamanho_nome)
# print(nome[0])

# nova_string = '' # Aqui será onde teremos um * antes de cada letra do nome
# indice = 0 # Definindo um indice de 0 que vai percorrer a pos das letras no while

# while indice < len(nome): # Enquanto o indice for menor que o tamanho do nome
#     nova_string += f'*{nome[indice]}' # Será concatenado na nova string os * antes das letras
#     indice += 1 # Depois de adicionar na nova string subimos o indice para a proxima letra

# nova_string += '*'
# print(nova_string) # Print da nova string





# Jeito que o professor fez: 

"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio' # Iteráveis
#       1110987654321
tamanho_nome = len(nome) # Pegando o tamanho do nome

indice = 0
novo_nome = ''

while indice < len(nome): 
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)