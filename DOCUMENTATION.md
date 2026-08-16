# Документация базы данных фитнес-клуба

Проект архитектуры БД для управления клиентами, тренерами, типами тренировок, абонементами и записями на занятия.

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

### 3. Типы тренировок (training_type)
* id (SERIAL) — PRIMARY KEY
* training_name (VARCHAR(100)) — NOT NULL, UNIQUE
* max_capacity (INTEGER) — CHECK (max_capacity > 0)
* instructor_id (INTEGER) — FOREIGN KEY -> instructor(id) (ON DELETE SET NULL)

### 4. Типы абонементов (ticket_type)
* id (SERIAL) — PRIMARY KEY
* type_name (VARCHAR(100)) — NOT NULL, UNIQUE
* duration_days (INTEGER) — NOT NULL, CHECK (duration_days > 0)

### 5. Абонементы (season_ticket)
* id (SERIAL) — PRIMARY KEY
* client_id (INTEGER) — NOT NULL, FOREIGN KEY -> client(id) (ON DELETE CASCADE)
* ticket_type_id (INTEGER) — NOT NULL, FOREIGN KEY -> ticket_type(id) (ON DELETE RESTRICT)
* training_type_id (INTEGER) — NOT NULL, FOREIGN KEY -> training_type(id) (ON DELETE RESTRICT)
* purchase_date (DATE) — NOT NULL, DEFAULT CURRENT_DATE
* end_date (DATE) — NOT NULL
* Constraint: CHECK (end_date >= purchase_date)

### 6. Запись на тренировки (client_training) — Таблица-мост (M:M)
* client_id (INTEGER) — FOREIGN KEY -> client(id) (ON DELETE CASCADE)
* training_type_id (INTEGER) — FOREIGN KEY -> training_type(id) (ON DELETE CASCADE)
* Constraint: PRIMARY KEY (client_id, training_type_id)

---

## Взаимосвязи

1. instructor -> training_type (1:M): Один тренер может вести много типов тренировок.
2. client -> client_training (1:M): Один клиент может иметь много записей на тренировки.
3. training_type -> client_training (1:M): На один тип тренировки может записаться много клиентов.  
   (Пункты 2 и 3 образуют связь Многие-ко-Многим между клиентами и тренировками).
4. client -> season_ticket (1:M): Один клиент может купить несколько абонементов.
5. ticket_type -> season_ticket (1:M): Один тариф может использоваться во множестве абонементов.
6. training_type -> season_ticket (1:M): Одно направление тренировок может указываться во множестве абонементов.

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

CREATE TABLE training_type (
    id SERIAL PRIMARY KEY,
    training_name VARCHAR(100) NOT NULL UNIQUE,
    max_capacity INTEGER CHECK (max_capacity > 0),
    instructor_id INTEGER REFERENCES instructor(id) ON DELETE SET NULL
);

CREATE TABLE ticket_type (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0)
);

CREATE TABLE season_ticket (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(id) ON DELETE CASCADE,
    ticket_type_id INTEGER NOT NULL REFERENCES ticket_type(id) ON DELETE RESTRICT,
    training_type_id INTEGER NOT NULL REFERENCES training_type(id) ON DELETE RESTRICT,
    purchase_date DATE NOT NULL DEFAULT CURRENT_DATE,
    end_date DATE NOT NULL,
    CONSTRAINT chk_season_ticket_dates CHECK (end_date >= purchase_date)
);

CREATE TABLE client_training (
    client_id INTEGER NOT NULL REFERENCES client(id) ON DELETE CASCADE,
    training_type_id INTEGER NOT NULL REFERENCES training_type(id) ON DELETE CASCADE,
    PRIMARY KEY (client_id, training_type_id)
);