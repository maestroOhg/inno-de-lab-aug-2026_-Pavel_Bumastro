# Задача 5*: Сборщик метрик инфраструктуры
# Разработать агрегатор метрик, который обрабатывает список кортежей
# телеметрии. Программа должна:
# 1. Распаковать элементы кортежей на переменные: node_name, cpu_load,
# ram_usage, status.
# 2. Отфильтровать (проигнорировать) серверы, имеющие статус offline.
# 3. Сформировать список имен активных серверов.
# 4. Рассчитать суммарные показатели активной группы: общее количество
# работающих серверов, среднюю загрузку CPU (с округлением до двух знаков после
# запятой) и пиковое (максимальное) значение использования оперативной памяти
# RAM.
# 5. Поместить рассчитанные метрики в итоговый вложенный словарь и вывести его
# структуру на экран.

system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]

node_name = [node_name for node_name, *_ in system_telemetry]
cpu_load = [cpu_load for _,cpu_load, *_ in system_telemetry]
ram_usage = [ram_usage for _,_,ram_usage, *_ in system_telemetry]
status = [status for *_,status in system_telemetry]

#создание нового картежа с онлайн серверами
system_telemetry_online = [
    (node_name,cpu_load,ram_usage,status) for node_name, cpu_load, ram_usage, status in system_telemetry
    if status == "online"
]

#Обновленный список для онлайн серверов
node_name = [node_name for node_name, *_ in system_telemetry_online]
cpu_load = [cpu_load for _,cpu_load, *_ in system_telemetry_online]
ram_usage = [ram_usage for _,_,ram_usage, *_ in system_telemetry_online]
status = [status for *_,status in system_telemetry_online]

print(f"Активные узлы сети: {node_name}" )

result_server = {"active_nodes_count" : len(system_telemetry_online),
                 "metrics" : {
                     "average_cpu" : round((sum(cpu_load)/len(cpu_load)),2),
                     "max_ram" : max(ram_usage)
                 }}
print(f"Итоговый отчет телеметрии: {result_server}")

#