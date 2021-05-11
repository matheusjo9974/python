# Importando bibliotecas

from random import randint
import os
#Função que gera a tela inicial
def start_layout():
    print("====================================================================")
    print("-----------------------------DADO DIGITAL---------------------------")
    print("====================================================================")
    start_game()

#funcao que gera o jogo
def start_game():
    action = input("Você gostaria de jogar esse dado? Responda com: 'sim/nao': ")
    if action.lower() == "sim":
        os.system("cls")
        print("\n")
        print("------------------------------")
        print("O lado do dado que caiu foi:", randint(1, 6))
        print("------------------------------\n")
        start_layout()
    elif action.lower() == "nao":
        print("----------")
        print("Até mais!!")
        print("----------")
        exit()
    else:
        os.system("cls")
        print("\n")
        print("--------------------------------------------------------------")
        print("Desculpe valor invalido. tente novamente somente com 'sim/nao'")
        print("--------------------------------------------------------------\n")
        start_layout()

start_layout()
