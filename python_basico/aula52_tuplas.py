"""
Tipo tupla - Uma lista imutável
Lista carregam muitos métodos que alteram ela, são um pouco mais lentas que as tuplas
Se quisermos uma lista que não vai ser alterada é melhor criar uma tupla
"""

nomes = ('Maria', 'Helena', 'Luiz') # Criando tupla
# nomes[1] = 'Outro' - Erro, tupla não suporta outras atribuições / Modificações
print(nomes[-1])
print(nomes)

# Podemos ter uma lista e converte-la em uma tupla
nomes_lista = ['Maria', 'Helena', 'Luiz']
nomes_tupla = tuple(nomes_lista) # Conversão, para converter de volta pra lista usamos list()
print(nomes_tupla)


