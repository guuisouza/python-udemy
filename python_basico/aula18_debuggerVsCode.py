# if / elif / else
# se / se não se / se não
# Mudam o fluxo do nosso programa
# O else é sempre a última coisa a ser executada
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print("Codigo para condição 1")
elif condicao2:
    print("Codigo para condição 2")
elif condicao3:
    print("Codigo para condição 3") # É executada pois é a primeira verdadeira
elif condicao4:
    print("Código para condição 4") # Nem é checada pois a acima ja satisfez a condição
else:
    print('Nenhuma condição foi satisfeita')

if 15 == 15: 
    print('Outro if')



print('Fora do if')

