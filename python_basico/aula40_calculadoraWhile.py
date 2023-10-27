"""" Calculadora com While """
# Pedir o primeiro número pro usuário
# Pedir o segundo número pro usuário
# Pedir um operador = Contas de + - / e *
# Fazer a operação do primeiro número com o segundo número
# Teremos uma calculadora infinita que ja começa pedindo um número
# O usuário poderá sair depois da operação se digitar [s]air - sair
# Esse sair mudará a condição para False
# método startswith = começa com determinada letra / endswith = termina ...

while True:
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    operador = input("Digite a operação que você quer fazer (+-/*): ")

    numeros_sao_validos = None # Flag - Bandeira
    #Declarando a variável fora do bloco
    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_sao_validos = True
    except:
        numeros_sao_validos = None

    if numeros_sao_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue
    
    operadores_permitidos = "+-/*"
        
    if operador	not in operadores_permitidos :
        print("Operador inválido")
        continue

    if len(operador) > 1:
        print("Você deve digitar apenas um operador")
        continue

    ## Fazer as contas agora!
    if operador == "+":
        print(f'O resultado da soma é: {numero1_float + numero2_float}')
    elif operador == "-":
        print(f'O resultado da subtração é: {numero1_float - numero2_float}')
    elif operador == "/":
        print(f'O resultado da divisão é: {numero1_float / numero2_float}')
    elif operador == "*":
        print(f'O resultado da multiplicação é: {numero1_float * numero2_float}')
    else:
        print("Não deveria chegar aqui...")


    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    if sair is True:
        print("Saindo...")
        break
