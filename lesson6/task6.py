# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.


def get_number(message='Enter the number: '):

    while True:
        try:
            val = (input(message))
            float_num = float(val)
        except ValueError as e:
            return 0
            print('0')
        else:
            break

    return float_num

number = get_number()
print(number)


# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів


def validation(arg1, arg2):
    if type(arg1) == int or type(arg1) == float:
        if type(arg2) == int or type(arg2) == float:
            return print(arg1*arg2)
    elif type(arg1) == str:
        if type(arg2) == str:
            return print(arg1 + arg2)
        else:
            argument = (arg1, arg2)
            return print(argument)



num_val = validation('4',3)


# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).


def get_years(age):

    if 11 <= int(age) <= 19:
        return ' років'
    elif int(age[-1]) == 1:
        return ' рік'
    elif int(age[-1]) in (2, 3, 4):
        return ' роки'
    else:
        return ' років'


def cinema(age,get_years):
    if age <= 0:
        return 'Здається сталась помилка!'
    elif age > 100:
        return print('Здається сталась помилка!')
    elif age < 7:
        return print(f'Тобі ж {age}{get_years}! Де твої батьки?')
    elif age % 10 == 7 or age // 7 == 10:
        return print(f'Вам {age}{get_years}, вам пощастить')
    elif age < 16:
        return print(f'Тобі лише {age}{get_years}, а це фільм для дорослих!')
    elif age > 65:
        return print(f'Вам {age}{get_years}? Покажіть пенсійне посвідчення!')
    else:
        return print(f'Незважаючи на те, що вам {age}{get_years}, білетів всеодно нема!')

age = cinema(int(input('Вкажіть ваш вік: ')), get_years(str(input('Уточніть ваш вік: '))))

# Не придумав, як по іншому подружити дві функції, щоб все працювало з одного вводу даних.
# Напишіть будь ласка ваші зауваження та поради після перевірки, прийму до уваги)))
