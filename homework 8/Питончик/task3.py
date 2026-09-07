from typing import Any

#Константы
DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(name_film,days_overdue,fine_rate: Any) -> tuple[float, float] | None :
    """
    Отказоустойчивая функция для расчета штрафа и технического индекса оборачиваемости.

    Args:
        name_film: Название фильма.
        days_overdue: Количество просроченных дней.
        fine_rate: Штраф за один день просрочки.

    Returns:
        tuple[float, float] | None: Возвращает кортеж (total_fine, return_index) или None при ошибке.
        total_fine: Штраф за просрочку.
        return_index: Технический индекс оборачиваемости.

    Raises:
        TypeError: Передан неверный тип данных.
        ValueError: Передана нерелевантная строка (нельзя привести к числу).
        ZeroDivisionError: Нулевые дни просрочки (деление на 0 при расчете индекса).
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

    except TypeError as error_type:
        print(f"[ОШИБКА ТИПА]  Некорректный тип данных для '{name_film}' : {error_type}\n")
    except ValueError as error_value:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{name_film}': {error_value}\n")
    except ZeroDivisionError as error_zero_division:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{name_film}': {error_zero_division}\n")

    else:
        return (total_fine, return_index)
    finally:
        print("--- Проверка транзакции возврата завершена ---")

print("--- Проверка возвратов ---")

test1 = calculate_overdue_fine("Matrix",5,1.5)
if(test1 is not None):
    print(f"Фильм: 'Matrix' | Итоговый штраф: {test1[0]}$ | Индекс: {test1[1]}\n")


test2 = calculate_overdue_fine("Inception",'пять',2.0)
if(test2 is not None):
    print(f"Фильм: 'Inception' | Итоговый штраф: {test2[0]}$ | Индекс: {test2[1]}\n")


test3 = calculate_overdue_fine("Avatar",0,2.5)
if(test3 is not None):
    print(f"Фильм: 'Avatar' | Итоговый штраф: {test3[0]}$ | Индекс: {test3[1]}\n")

test4 = calculate_overdue_fine("Interstellar",[3,],3.0)
if(test4 is not None):
    print(f"Фильм: 'Interstellar' | Итоговый штраф: {test4[0]}$ | Индекс: {test4[1]}\n")
#