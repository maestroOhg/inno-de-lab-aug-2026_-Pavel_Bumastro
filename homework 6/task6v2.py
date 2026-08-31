#   Задание 6
# Напишите программу, которая работает как простой
# калькулятор. Программа должна запросить у пользователя два числа и
# символ операции (+, -, *, /), а затем выполнить расчёт и вывести результат.

#Способ 2
#Стандарт
while True:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    user_operators = (input("Введите оператор  (+, -, *, /):")).strip()
#strip для удаления символов в данном случае пробела
    if user_operators == "+":
        print(first_number + second_number)
    elif user_operators == "-":
        print(first_number - second_number)
    elif user_operators == "*":
        print(first_number * second_number)
    elif user_operators == "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("Ошибка деления")
    else:
        print("Неверный оператор")
