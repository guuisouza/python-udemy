"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9 # > 9 = 0 se for < 9 = 9
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if False else 'Outro Valor' if False else 'Fim') # Não recomendado