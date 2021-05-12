# importando biblioteca
import random

# criando listas de possiveis perguntas e respostas
list_ask = ["devo sair hoje?", "como esta o clima?", "qual o seu nome?", "quantos anos voce tem?", "quantos anos eu tenho?",
            "como eu me chamo?", "que dia e hoje?", "qual o diametro do planeta terra", "o que e python", "para que serve python?",
            "devo trabalhar hoje?", "devo dormir hoje", "voce dorme?", "quanto tempo leva para chegar em marte", "devo almoçar"]

possible_answers = ["nao sei", "talvez", "sim, vai la", "nao", "posto ipiranga"]

# função que inicia programa
def init_program(list_ask, possible_answers):
    ask = input("Digite sua pergunta ou digite 'sair' para finalizar o programa: ")
    if ask.lower() == "sair":
        exit()
    elif ask.lower() in list_ask:
        print(random.choice(possible_answers), "\n")
        init_program(list_ask, possible_answers)
    else:
        print("pergunta incorreta tente novamente")
        init_program(list_ask, possible_answers)

# chamada a função que inicia o programa
init_program(list_ask, possible_answers)