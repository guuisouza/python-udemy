# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição que for verdadeira
# avalia toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar ou [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('entrar')
# else:
#     print('sair')

# Avaliação de curto circuito
# Na primeira vez que ele achar um valor verdadeiro ele vai retornar
# Este valor verdadeiro
print(0 or False or 0 or 'abc' or True)