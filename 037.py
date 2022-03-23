import random


while True:
    opc = ["pedra", "papel", "tesoura"]

    maquina = random.choice(opc)
    jogador = None

    while jogador not in opc:
        jogador = input("Pedra, papel ou tesoura?: ").lower()

    if jogador == maquina:
        print("A máquina: ", maquina)
        print("Jogador: ", jogador)
        print("Empate!")

    elif jogador == "pedra":
        if maquina == "papel":
            print("A máquina: ", maquina)
            print("Jogador: ", jogador)
            print("HAHAHAH, otário!")
        if maquina == "tesoura":
            print("A máquina: ", maquina)
            print("O jogador: ", jogador)
            print("Você ganhou!")

    elif jogador == "tesoura":
        if maquina == "pedra":
            print("A máquina: ", maquina)
            print("Jogador: ", jogador)
            print("Perdeu, trouxa!")
        if maquina == "papel":
            print("A máquina: ", maquina)
            print("O jogador: ", jogador)
            print("Você ganhou!")

    elif jogador == "papel":
        if maquina == "pedra":
            print("A máquina: ", maquina)
            print("Jogador: ", jogador)
            print("Amassa o novato!")
        if maquina == "tesoura":
            print("A máquina: ", maquina)
            print("O jogador: ", jogador)
            print("PICOTADO, COMÉDIA!")

    extra = input("Quer jogar de novo? (s/n): ").lower()
    if extra != "s":
        break
print("Até logo!")