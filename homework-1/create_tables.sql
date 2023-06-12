-- SQL-команды для создания таблиц
CREATE TABLE employee
(
	id_employee int PRIMARY KEY,
	full_name varchar(100) NOT NULL,
	job_title varchar(50) NOT NULL
);

INSERT INTO employee VALUES (1, 'Иванов И.И.', 'менеджер');

CREATE TABLE customers
(
    id_customers int PRIMARY KEY,
	full_name varchar(100) NOT NULL,
	phone_number int NOT NULL
);

INSERT INTO customers VALUES (1, 'Васильев В.В.', 7808);

CREATE TABLE orders
(
	id_orders int PRIMARY KEY,
	name_of_product varchar(100) NOT NULL,
	price int NOT NULL,
	quantity int NOT NULL,
	id_order int REFERENCES customers(id_customers) NOT NULL
);

INSERT INTO orders VALUES (101, 'apple', 1000, 10, 1);
