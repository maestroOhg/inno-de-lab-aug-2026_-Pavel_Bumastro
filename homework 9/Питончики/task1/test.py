#Тесты для задания 1
from task1.trainee import Trainee


# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name = "Иван", surname = "Иванов", score = 9, passing_grade = 10)

# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")

#



