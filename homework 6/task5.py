#   Задание 5
# Напишите программу, которая генерирует
# случайное число от 1 до 20. У пользователя есть 5 попыток, чтобы его
# угадать. На каждом шаге программа подсказывает («Слишком много!»
# или «Слишком мало!») и сообщает, сколько попыток осталось. Игра
# завершается, если число угадано или закончились попытки.

import random


random_number = random.randint(1, 20)
attempt=5

while (attempt > 0):
    number = int(input(f"Попытка {6-attempt}.Введите число: "))
    attempt -= 1
    if number == random_number:
        print("Ты угадал! Красава")
        break
    if  attempt == 0:
        print(f"Не угадал, загаданное число - {random_number}")
        break
    elif random_number > number:
        print(f'Слишком мало, осталось попыток: {attempt}')
    else:
        print(f'Слишком много, осталось попыток: {attempt}')
