"""
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim e fica executando eternamente
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6 : #Pula o 6 por causa do continue
        print("Nao vou mostrar o 6")
        continue
    
    if contador >= 10 and contador <= 27: #Pula tudo do 10 ao 27
        print(f"Não vou contar o {contador}")
        continue
        
    print(contador) # Nâo vai ser executado quando for 6 e nem do 10 ao 27 - continue

    if contador == 40: # Condição de parada
        break

print("Acabou")