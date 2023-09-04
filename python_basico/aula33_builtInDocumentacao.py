"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

# O que significa a imutabilidade?
# Supondo que tenhamos uma string com o nome guilherme
string_imutavel = 'Guilherme'
# Se quisermos pegar um valor da string e alterar um indice
# Trocar o L por 58 por exemplo

# string_imutavel[3] = 58
# print(string_imutavel[3])

# Dará erro pois str é um tipo imutavel

# Para fazer isso fariamos asssim

string_imutavel2 = 'guilherme'
outra_variavel =  f'{string_imutavel2[0:3]}ABC{string_imutavel2[4:]}'
print(outra_variavel) # GuiABCherme e tiramos o L


# str, int, float e bool são objetos e temos ações para executar dentro desses objetos (métodos)
print(string_imutavel2.capitalize()) # Método que retorna a primeira letra em maiusculo e o resto min
print(string_imutavel2.zfill(10)) # Preenche todos os valores a esquerda da string com 0 até dar 100 caracteres