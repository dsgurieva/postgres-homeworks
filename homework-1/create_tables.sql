-- SQL-команды для создания таблиц
CREATE TABLE customers
(
    customer_id varchar(50) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
);

INSERT INTO customers VALUES('AAA', 'aaa', 'aaa');

CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(100) NOT NULL,
    title varchar(100) NOT NULL,
    notes text
);

INSERT INTO employees VALUES(1, 'aaa', 'aaa', 'aaa');

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(50) REFERENCES customers(customer_id),
    employe_id int REFERENCES employees(employee_id),
    ship_city varchar(100) NOT NULL
)

INSERT INTO orders VALUES(101, 'AAA', 1, 'aaa');

