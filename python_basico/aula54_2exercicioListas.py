"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista
"""

# [i]Inserir - append
# [a]Apagar - del
# [l]Listar - print
# [s]Sair
import os

lista_compras = []
sair = False

while sair != True :
    opcao = input("Selecione uma opção: \n" "[i]nserir, [a]pagar, [l]istar ou [s]air \n").lower()
    
    if opcao == 's':
        os.system('cls')
        print("Desconectando...")
        sair = True
    
    elif opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)
        
    elif opcao == 'a':
        os.system('cls')
        indice_str = input("Digite o indice que quer apagar: \n")
        
        try: 
            indice_int = int(indice_str)
            del lista_compras[indice_int]
        except ValueError:
            print("A operação não pode ser realizada, digite um número inteiro")
        except IndexError:
            print("Verifique se não digitou um índice inexistente!")
        except:
            print("Erro desconhecido!")
            
    elif opcao == 'l':
        os.system('cls')
        
        for indice, valor in enumerate(lista_compras):
            print(indice, valor)
    else:
        os.system('cls')
        print("Digite uma opção válida!")
        
        
        
    
    
