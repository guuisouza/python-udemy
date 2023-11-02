# Não é comum usar while com coisas
# Que a gente sabe quando termina
# Usamos o while quando não sabemos precisamente o nº de repetições

# while
# password_save = '123456'
# password_typed = ''
# repetitions = 0

# while password_save != password_typed:
#     password_typed = input("Type your password again!")

#     repetitions += 1

# print('Aquele laço acima pode ter repetições infinitas!')

# for

texto = "Python"
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'

novo_texto += '*'
print(f'{novo_texto}')
