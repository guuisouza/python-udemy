# Aqui queremos descobrir
# Qual a letra apareceu mais vezes nesta frase abaixo


frase = 'O python é uma linguagem de programação '\
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
letra_mais_apareceu = ''
qtde_vezes_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qtde_vezes_apareceu_atual = frase.count(letra_atual)
    if qtde_vezes_apareceu < qtde_vezes_apareceu_atual:
        qtde_vezes_apareceu = qtde_vezes_apareceu_atual
        letra_mais_apareceu = letra_atual
    i += 1
print(f"A letra que mais apareceu foi: {letra_mais_apareceu} aparecendo {qtde_vezes_apareceu}x")

