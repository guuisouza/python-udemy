"""
Escopo de funções em Python
Escopo = local onde determinado código pode atingir
Existe o escopo local e o escopo global
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 
def escopo():
    #global x -> define que o x que está de fora será manipulado nesta função
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
    
# print(x); Erro, pois x está fora do escopo (dentro somente da funcao)
print(x)
escopo()
