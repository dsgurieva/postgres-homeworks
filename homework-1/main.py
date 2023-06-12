"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="1111") as conn:

    with conn.cursor() as cur:

        # Добавление данных  в таблицу employee
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s)", (2, 'Петров П.П', 'менеджер', 'aaa'))
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s)", (3, 'Сидоров С.С.', 'менеджер', 'aaa'))

        # Добавление данных  в таблицу customers
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('BBB', 'Максимов М.М.', '7777'))
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('CCC', 'Александров А.А.', '7474'))

        # Добавление данных  в таблицу orders
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s)", (102, 'BBB', 2, 'aaa'))

        # Чтение донных из таблицы customers
        cur.execute("SELECT * FROM customers")

        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()

