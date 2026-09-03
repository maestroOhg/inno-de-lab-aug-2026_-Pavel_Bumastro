# Задача 2: Фильтрация транзакций платежного шлюза
# Дан список сырых строк, представляющих транзакции в формате
# СТАТУС:СУММА. Требуется написать однострочное выражение (генератор списка),
# которое:
# 1. Отсеивает все транзакции, не имеющие статус SUCCESS.
# 2. Извлекает числовое значение суммы платежа.
# 3. Исключает аномальные транзакции с неположительной суммой (меньше или
# равной нулю).
# 4. Преобразует корректные суммы в целочисленный тип данных (int).

# Список транзакций, полученных от платежного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]

raw_transactions_clear =list(int (elem[8:len(elem)]) for elem in raw_transactions if elem.startswith("SUCCESS:") and int(elem[8:len(elem)])>0)
print(f"Очищенные транзакции: {raw_transactions_clear}")

#вариант 2
# raw_transactions_clear = int(amount) for status, amount in (tx.split(":") for tx in raw_transactions)
#     if status == "SUCCESS" and int(amount) > 0

#