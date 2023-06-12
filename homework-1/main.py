"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="1111") as conn:

    with conn.cursor() as cur:

        # Добавление данных  в таблицу employee
        cur.execute("INSERT INTO employee VALUES (%s, %s, %s)", (2, 'Петров П.П', 'менеджер'))
        cur.execute("INSERT INTO employee VALUES (%s, %s, %s)", (3, 'Сидоров С.С.', 'менеджер'))

        # Добавление данных  в таблицу customers
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (2, 'Максимов М.М.', 7777))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (3, 'Александров А.А.', 7474))

        # Добавление данных  в таблицу orders
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (102, 'tea', 100, 10, 1))

        # Чтение донных из таблицы customers
        cur.execute("SELECT * FROM customers")

        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()

