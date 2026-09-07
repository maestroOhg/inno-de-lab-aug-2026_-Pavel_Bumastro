# Задача 3: Безопасный парсинг конфигурации API
# Написать программу для анализа конфигурации базы данных. Скрипт должен:
# 1. Извлечь значения host и port из вложенного словаря connection.
# 2. Безопасно проверить наличие ключа ssl_settings. Если этот ключ или вложенный в
# него параметр ssl_mode отсутствуют, переменная должна принять дефолтное
# значение verify-full.
# 3. Изменить значение пользователя (user) во вложенном словаре на admin.
# 4. Добавить новый параметр max_connections со значением 100 непосредственно во
# вложенный словарь connection.
# 5. Вывести обновленное содержимое конфигурации connection, используя итерацию
# по парам ключ-значение.

db_config = {
    "connection": {
    "host": "production-db.internal",
    "port": 5432,
    "user": "postgres"
     }
}

connection = db_config.get("connection",{})
host_value = connection.get("host")
port_value = connection.get("port")

#Можно было бы просто так
ssl_mode = connection.get("ssl_settings",{}).get("ssl_mode","verify-full")

#захотелось сделать что-то такое еще(создает все в случае отсутствия ключа или значения
#---------Некая херня----------------------
# if("ssl_settings" in connection and isinstance(connection["ssl_settings"],dict)):
#     if("ssl_mode" in connection["ssl_settings"]):
#         if(connection["ssl_settings"]["ssl_mode"] == "verify-full"):
#             ssl_mode = "verify-full"
#         else:
#             connection["ssl_settings"]["ssl_mode"] = "verify-full"
#             ssl_mode ="verify-full"
#     else:
#         connection["ssl_settings"]["ssl_mode"] = "verify-full"
#         ssl_mode = "verify-full"
# else:
#     connection["ssl_settings"] = {"ssl_mode": "verify-full"}
#     ssl_mode = "verify-full"
#

print(f"SSL MODE: {ssl_mode}")

connection["user"] = "admin"

connection["max_connections"] = 100

for k,v in connection.items():
    print(f"{k}: {v}")

#


