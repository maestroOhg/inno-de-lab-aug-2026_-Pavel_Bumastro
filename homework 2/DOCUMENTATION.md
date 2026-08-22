# Документация базы данных фитнес-клуба

Проект архитектуры БД для управления клиентами, тренерами, тренировками (групповыми и индивидуальными) и записями клиентов на занятия.

---

## Дорожная карта (Roadmap)

- [x] Идентификация сущностей и их атрибутов
- [x] Настройка связей и каскадных правил (FK)
- [x] Реализация связи «Многие-ко-Многим» (client_training)
- [x] Создание DDL-скрипта для PostgreSQL
- [x] Разработка ER-диаграммы (Концептуальная и Логическая модели)

---

## Таблицы и ограничения

### 1. Клиенты (client)
* id (SERIAL) — PRIMARY KEY
* first_name (VARCHAR(100)) — NOT NULL
* last_name (VARCHAR(100)) — NOT NULL
* phone (VARCHAR(20)) — NOT NULL, UNIQUE
* email (VARCHAR(100))

### 2. Тренеры (instructor)
* id (SERIAL) — PRIMARY KEY
* first_name (VARCHAR(100)) — NOT NULL
* last_name (VARCHAR(100)) — NOT NULL
* phone (VARCHAR(20)) — NOT NULL, UNIQUE
* email (VARCHAR(100))

### 3. Тренировки (training)
* id (SERIAL) — PRIMARY KEY
* training_name (VARCHAR(100)) — NOT NULL
* start_time (TIMESTAMP) — NOT NULL
* is_group (BOOLEAN) — NOT NULL, DEFAULT TRUE
* max_capacity (INTEGER) — CHECK (max_capacity > 0)
* instructor_id (INTEGER) — FOREIGN KEY -> instructor(id) (ON DELETE SET NULL)

### 4. Запись на тренировки (client_training) — Таблица-мост (M:M)
* id (SERIAL) — PRIMARY KEY
* client_id (INTEGER) — NOT NULL, FOREIGN KEY -> client(id) (ON DELETE CASCADE)
* training_id (INTEGER) — NOT NULL, FOREIGN KEY -> training(id) (ON DELETE CASCADE)

---

## Взаимосвязи

1. instructor -> training (1:M): Один тренер может вести множество тренировок в расписании.
2. client -> client_training (1:M): Один клиент может быть записан на множество тренировок.
3. training -> client_training (1:M): На одну тренировку может быть записано множество клиентов.  
   (Пункты 2 и 3 образуют связь Многие-ко-Многим между клиентами и конкретными тренировками).

---

## SQL-скрипт (PostgreSQL)

```sql
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE instructor (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE training (
    id SERIAL PRIMARY KEY,
    training_name VARCHAR(100) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    is_group BOOLEAN NOT NULL DEFAULT TRUE,
    max_capacity INTEGER CHECK (max_capacity > 0),
    instructor_id INTEGER REFERENCES instructor(id) ON DELETE SET NULL
);

CREATE TABLE client_training (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(id) ON DELETE CASCADE,
    training_id INTEGER NOT NULL REFERENCES training(id) ON DELETE CASCADE
);