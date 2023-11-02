""" while/else
    O else não é executado quando tem um break, ele não vai chegar no else.
"""

string = "Valor qualquer"
print(len(string))

# Pra que seria um uso desse else :

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == " ":
        break # Não será executado o else pois aqui acaba o programa (Se tiver espaço)

    print(letra)
    i += 1
else:  # Acontece quando não tem espaço, o If nao valida e vem parar aqui
    print("Não encontrei espaço")