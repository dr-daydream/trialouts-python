# quiz

def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------")
        print(key)
        print("---------------------------")
        for i in options[question_num-1]:
            print(i)
        guess = input("Responda com (A, B, C ou D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses,guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correto.")
        return 1
    else:
        print("Incorreto.")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Resultados")
    print("---------------------------")
    print("Respostas: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Palpites: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Seus pontos foram: "+str(score)+"%")


def play_again():
    response = input("Deseja repetir o jogo? (sim ou não): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
"Quem matou a Cronos? ":"D",
"Quem deu o boné para Annabeth? ":"C",
"Anaklusmos serviu a quem antes de Percy? ":"B",
"Qual foi o nome dado a Jápeto após o Lete? ": "A"
}

options = [["A. Percy Jackson", "B. Ethan Nakamura", "C. Prometeu", "D. Luke Castellan"],
            ["A. Hades", "B. Dédalo", "C. Atena", "D. Nenhuma das opções"],
            ["A. Teseu", "B. Hércules", "C. Jasão", "D. Aquiles"],
            ["A. Bob", "B. Donny", "C. Jape", "D. Leste"]]

new_game()

while play_again():
    new_game()

print("Que as Parcas lhe acompanhem!")