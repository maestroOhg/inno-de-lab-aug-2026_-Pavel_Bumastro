#Константы

MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

#Задание 1
def  calculate_rental_batch(quantity : int, rental_rate :float , discount : float=0.0) -> tuple[float, bool] :
    """
    Функция для расчета стоимости партии дисков
    с учетом жанровой скидки

    Args:
            quantity(int) - количество дисков
            rental_rate(float) - арендная ставка
            discount(float) - процент скидки

    Returns:
        tuple[float, bool] - Кортеж из двух элементов:
        final_sum (float): Итоговая стоимость.
        is_limit_exceeded (bool): Флаг превышения лимита
    """
    final_sum: float =  round(quantity * rental_rate * (1 -
    discount),2)
    is_limit_exceeded : bool = final_sum > MAX_RENTAL_BATCH_LIMIT
    return (final_sum, is_limit_exceeded)

#Функция для удобного вывода
def create_report (name_batch : str, quantity : int, rental_rate : float, discount :float=0.0) :
    calc_batch = calculate_rental_batch(quantity ,rental_rate,discount)

    print(f"""
    Партия ({name_batch}), {quantity} - количество дисков, {rental_rate}$ - cтоимость арендной ставки 
    Сумма - {calc_batch[0]}. Превышение лимита: {calc_batch[1]}""")

create_report("Academy Dinosaur",quantity=30,rental_rate= 2.99) #Именованный вызов
create_report("Affair Prejudice",40,4.99,0.10)
create_report("Agent Truman",10,1.99)
create_report("African Egg",50,3.50,0.20)

#

