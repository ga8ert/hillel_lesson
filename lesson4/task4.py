#1. Дана довільна строка.
# Напишіть код, який знайде в ній і виведе на екран кількість слів,
# які містять дві голосні літери підряд.

#Сучасна абетка нараховує 10 букв, що позначають голосні звуки на письмі:
# А, Е, Є, И, І, Ї, О, У, Ю, Я.
# В українській мові букви «Я», «Ю», «Є», «Ї» називають йотованими.

vowel_letters = set('аеєиіїоуюя')

world_counter = 0

text = input('Введіть свій текст, для пошуку Українською : ').lower().split()

for word in text:
    vowel_letters_counter = 0
    for letter in word:
        if letter in vowel_letters:
            vowel_letters_counter += 1
        else:
            vowel_letters_counter = 0
        if vowel_letters_counter == 2 :
            world_counter += 1
            break
print(world_counter)

# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.


min_price = 38
max_price = 48.3

price_dict = { "cito": 47.999,
               "BB_studio": 42.999,
               "momo": 49.999,
               "main-service": 37.245,
               "buy.now": 38.324,
               "x-store": 37.166,
               "the_partner": 38.988,
               "store": 37.720,
               "rozetka": 38.003
               }
for key, values in price_dict.items():
    if max_price > values > min_price:
        print(key.capitalize())