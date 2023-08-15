""""
Formtatação básica de Strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita 
^ - Centro
Sinal - + ou -
Ex: 0>100, .1f
Conversion flags - !r !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') # Preenche para a esquerda com espaço
print(f'{variavel:.<10}') # Preenche para a direita com .
print(f'{variavel:.^10}') # Preenche para o centro e .
print(f'{1000.1515414:0=+10,.1f}') # Coloca a virgula no milhar e muda as casas decimais e coloca se é positivo
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')

