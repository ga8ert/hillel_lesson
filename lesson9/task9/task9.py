# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним основну функцію гри з попередньої дз.
# Після закінчення гри декоратор має сповістити, скільки тривала гра.
import random
from time import time


def decorator_time(func):
	"""
	 This function shows the execution time of
	 the function object passed
	"""
	def wrapper(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'The game lasted {(t2-t1):.10f}s')
		return result
	return wrapper



# Rock-paper-scissors

# Game outcomes
rules = {
    "Rock": {"Rock": "Draw", "Paper": "Loss", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Loss"},
    "Scissors": {"Rock": "Loss", "Paper": "Win", "Scissors": "Draw"}
}


@decorator_time
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
        random_numb = random.randint(1, 3)
        ai_choice = number_conversion(random_numb)
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



