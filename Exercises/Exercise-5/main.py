import csv

import psycopg2


def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # tu código va aquí
    cur = conn.cursor()

    # se llama a la funcion para crear las tablas
    query = create_table()
    cur.execute(query)
    conn.commit()

    # llamar a las funciones para insertar los datos en las tablas
    insert_accounts(cur)
    insert_products(cur)
    insert_transactions(cur)
    conn.commit()

    cur.close()
    conn.close()


def create_table():
    query = """
    DROP TABLE IF EXISTS transactions, products, accounts CASCADE;

    CREATE TABLE accounts(
        customer_id INTEGER PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address_1 VARCHAR(100) NOT NULL,
        address_2 VARCHAR(100),
        city VARCHAR(50) NOT NULL,
        state VARCHAR(50) NOT NULL,
        zip_code VARCHAR(10) NOT NULL,
        join_date DATE NOT NULL
    );

    CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        product_code VARCHAR(50) NOT NULL,
        product_description VARCHAR(100) NOT NULL
    );

    CREATE TABLE transactions(
        transaction_id VARCHAR(50) PRIMARY KEY,
        transaction_date DATE NOT NULL,
        product_id INTEGER REFERENCES products(product_id),
        product_code VARCHAR(50) NOT NULL,
        product_description VARCHAR(100) NOT NULL,
        quantity INTEGER NOT NULL,
        account_id INTEGER REFERENCES accounts(customer_id)
    );

    CREATE INDEX idx_transactions_product_id ON transactions(product_id);
    CREATE INDEX idx_transactions_account_id ON transactions(account_id);
    """
    return query


def insert_accounts(cur):
    with open("data/accounts.csv") as f:
        reader = csv.reader(f)
        next(reader)  # saltar el header
        for row in reader:
            row = [v.strip() for v in row]
            cur.execute(
                "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )


def insert_products(cur):
    with open("data/products.csv") as f:
        reader = csv.reader(f)
        next(reader)  # saltar el header
        for row in reader:
            row = [v.strip() for v in row]
            cur.execute(
                "INSERT INTO products VALUES (%s, %s, %s)",
                row
            )


def insert_transactions(cur):
    with open("data/transactions.csv") as f:
        reader = csv.reader(f)
        next(reader)  # saltar el header
        for row in reader:
            row = [v.strip() for v in row]  # eliminar espacios en blanco
            cur.execute(
                "INSERT INTO transactions VALUES (%s, %s, %s, %s, %s, %s, %s)",
                row
            )


if __name__ == "__main__":
    main()
