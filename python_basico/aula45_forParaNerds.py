"""
Iterável - str, range, etc - tem um método dentro chamado iter (__iter__)
Métodos -> Uma ação que executa dentro de um objeto
Iterador - quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu valor
"""
# for letra in texto
texto = 'Guilherme' # Iterável
iterador = iter(texto) # Iterator


while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# É a mesma coisa de fazer 
# for letra in texto:
#     print(letra)