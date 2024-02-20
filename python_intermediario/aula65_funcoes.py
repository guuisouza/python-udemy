"""
    Introdução às funções (def) em Python
    Funções são trechos de código usados para
    replicar determinada ação ao longo do seu código
    Elas podem receber valores para parâmetros (argumentos)
    e retornar um valor específico.
    Por padrão, funções Python retornam None (nada).
"""
def imprimir(a, b, c): # Parametro
    print(a,b,c)

# Se quiser executar a ação tem que abrir e fechar os ()
imprimir(2, 15, 5) # Argumento (valores)

def saudacao(nome):
    print(f'Olá "{nome}"')

nome = input("Digite seu nome: \n")
saudacao(nome)
