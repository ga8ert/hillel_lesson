# Напишіть гру "rock scissors paper lizard spock".
# Використайте розділення всієї програми на функції (Single-Responsibility principle).
# Як скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію


# Rock-paper-scissors

import random

# Game outcomes
rules = {
    "Rock": {"Rock": "Draw", "Paper": "Loss", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Loss"},
    "Scissors": {"Rock": "Loss", "Paper": "Win", "Scissors": "Draw"}
}


def number_conversion(number):
    """
    This function converts the result
    """
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Scissors"

    while True:
        random_num = random.randint(1, 3)
        ai_choice = number_conversion(random_num)
        user_choice = input(str("Select Rock/Paper/Scissors : "))
        try:
            print("")
            print("**********************************")
            print("You selected : ", user_choice)
            print("The computer selected : ", ai_choice)
            print("(* Game over *) ")
            print(rules[user_choice][ai_choice])
            print("**********************************")
            print("")
        except:
            print("Invalid Input!!")
