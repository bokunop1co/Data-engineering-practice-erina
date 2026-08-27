import psycopg2


def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # tu código va aquí
    cur = conn.cursor()


if __name__ == "__main__":
    main()
