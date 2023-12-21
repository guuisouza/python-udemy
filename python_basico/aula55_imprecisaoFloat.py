"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
# Formas de controlar a imprecisão - Resultado final formatado
print(f'{numero_3:.2f}') # Aqui temos uma string (f string)
# Formas de controlar a imprecisão - Round
print(round(numero_3, 1)) # Aqui temos o tipo real (float)
# Formas de controlar a imprecisão - Módulo do python

