"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 
# Inicio do jogo

palavra_secreta = "ambiente"
print("Seja bem vindo ao jogo da palavra secreta, você deverá adivinhar ela")

letra_do_usuario = ''
letras_acertadas = ''
palavra_final = ''
tentativas = 0

while palavra_final != palavra_secreta:
    letra_do_usuario = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_do_usuario) > 1:
        print("Digite apenas uma letra")
        continue
    
    if letra_do_usuario in palavra_secreta:
        letras_acertadas += letra_do_usuario # Mantém na letras_acertada o que ele já acertou
        
    palavra_formada = ''
    for letra in palavra_secreta: # Percorre cada letra da palavra secreta
        if letra in letras_acertadas: # Se a letra atual da palavra secreta tiver o que ele já acertou
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)
    palavra_final = palavra_formada
os.system('cls') # Limpa o terminal

print("Parabéns você acertou")
print("A palavra era:", palavra_secreta)
print("Você ganhou após:", tentativas, "tentativas!")





