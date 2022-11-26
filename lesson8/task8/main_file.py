#     Візьміть гру з попереднього ДЗ ('rock scissors paper lizard spock')  і модифікуйте наступним чином:
#     винесіть всі функції в окремий файл (нехай буде library.py) і імпортуцте їх звідти для роботи в основний файл
#     додайте запис статистики в файл (які фігури грали і хто переміг на кожному ході), використовуйте open.
import random

from library import number_conversion, rules

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
        break
    except:
        print("Invalid Input!!")


statistic = open('statistic.txt', 'a')

statistic.write("\n")
statistic.write("You selected : ")
statistic.write(user_choice)

statistic.write("\nThe computer selected : ")
statistic.write(ai_choice)

statistic.write('\n')
statistic.write(rules[user_choice][ai_choice])

statistic.close()
