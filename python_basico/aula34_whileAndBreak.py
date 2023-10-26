"""
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim e fica executando eternamente
"""

condicao = True

while condicao:
    nome = input("Qual é o seu nome?")
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        print("Você saiu")
        break # Para a execução do while

print('acabou')