from typing import Callable
from typing import Any
import time

#Константы
MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

# Задание 2
def performance_logger(func : Callable[...,Any]) -> Callable[...,Any]:
    """
    Декоратор для замера время выполнения функции и вывода лога

    Args:
        func : Callable[...,Any] - принимает функцию с любыми параметрами

    Returns:
        Callable - возвращает функцию
    """
    def wrapper(*args :Any, **kwargs : Any) -> Any:

        start_time = time.perf_counter()
        sorted_report = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за { (end_time-start_time):.{TIME_DECIMALS}f} сек.")
        return sorted_report
    return wrapper


@performance_logger
def get_sorted_report(sales : list[dict[str, str | float]]) -> list[dict[str, str | float]] :
    """
    Функция сортирует список категорий по total_sales в порядке убывания

    Args:
        sales - список словарей с данными: категория, выручка

    Returns:
        list[dict[str, str | float]] - отсортированный список
    """
    return sorted(sales, key = lambda item: item['total_sales'], reverse=True)


#Тесты
print("Тестирование производительности:\n")

print("Тест 1")
test1 = get_sorted_report([
{"category": "Action", "total_sales": 4311.85},
{"category": "Animation", "total_sales": 4656.30},
{"category": "Children", "total_sales": 3655.55}])

print("Топ категорий по выручке:")
for i,item in enumerate(test1, start=1):
    print(f"{i}. {item.get('category','error')} : {item.get('total_sales',0.0)}")
print("\n")

print("Тест 2")
test2 = get_sorted_report([
{"category": "Classics", "total_sales": 1200.10},
{"category": "Comedy", "total_sales": 4000.00},
{"category": "Documentary", "total_sales": 4000.00}
])

print("Топ категорий по выручке:")
for i,item in enumerate(test2, start=1):
    print(f"{i}. {item.get('category','error')} : {item.get('total_sales',0.0)}")
print("\n")

print("Тест 3")
test3 = get_sorted_report([
{"category": "Drama", "total_sales": 500.00}
])

print("Топ категорий по выручке:")
for i,item in enumerate(test3, start=1):
    print(f"{i}. {item.get('category','error')} : {item.get('total_sales',0.0)}")
print("\n")

#