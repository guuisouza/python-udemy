"""
Introdução ao desempacotamento e empacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz'] # Suponha que queremos extrair esses valores e atribui-los a variáveis
# Poderia ser feito desta forma:
nome1, nome2, nome3 = nomes
print(nome2) # Helena

# Também poderia ser feito assim:
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz'] 

# Pode ser que você queira pegar somente alguns valores
# nome1, nome2 = ['Maria', 'Helena', 'Luiz'] # Assim dará erro, muitos valores para poucas variáveis

# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz'] # Assim dará erro, não tem valores suficientes para desempacotar

# Se quisermos pegar somente o segundo valor ou etc, é necessário falar pro python
# O que ele fará com o resto


nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1, resto) # Pega o primeiro valor e no resto terá uma lista do restante

# Porém não é legal criar variáveis que não vão ser utilizadas, por isso utilizamos o _ como convenção
_, _, nome3, *_ =  ['Maria', 'Helena', 'Luiz']
print(nome3)