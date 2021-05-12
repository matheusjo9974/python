# importando bibliotecas
from random import randint
import os


# funcão que mostra o cabeçalho
def start_layout():
    print("=======================================")
    print("----------Adivinhe se puder------------")
    print("=======================================")
    start_game()

# função que gera o valor aleatório
def generate_value():
    number = randint(0, 100)
    return number

#função que testa se o usuário quer continuar
def restart_game():
    restart = input("Deseja jogar novamente? Responda com 'sim/nao: ")
    if restart.lower() == "sim":
        os.system("cls")
        start_layout()
    elif restart.lower() == "nao":
        print("Até mais!!!")
        exit()
    else:
        print("Desculpe valor invalido. tente novamente somente com 'sim/nao'")
        restart_game()

# função que principal
def start_game():
    global user
    value_true = generate_value()
    # laço que repete as entradas do usuario até ele acertar
    lace = True
    while lace == True:

        # laço que valida as entradas do usuario
        lace2 = True
        while lace2 == True:
            value_test = input("Chute um numero inteiro entre 0 e 100: ")
            if value_test.isdigit() and int(value_test) in range(100 + 1):
                user = value_test
                lace2 = False
            else:
                print("valor invalido. tente novamente somente com numeros inteiros entre 0 e 100\n")

        #comparador que testa as entradas do usuário
        if int(user) == value_true:
            print("Parabéns você acertou!!\n")
            lace = False
        elif int(user) > value_true:
            print("Número muito alto, digite um valor menor.\n")
        else:
            print("valor muito baixo, digite um avlor maior.\n")

    restart_game()
# programa principal
start_layout()


