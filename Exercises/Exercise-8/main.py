import duckdb
from pathlib import Path



def main():
    con = duckdb.connect("electric_cars.db")
    create_table(con)
    load_data(con)
    autos_por_ciudad(con)
    top_tres_vehiculos(con)
    auto_por_codigo_postal(con)
    autos_por_modelo(con)
    con.close()

    pass


def create_table(con):
    con.execute("""
        CREATE OR REPLACE TABLE electric_cars(
        vin VARCHAR,
        county VARCHAR,
        city VARCHAR,
        state VARCHAR,
        postal_code VARCHAR,
        model_year INTEGER,
        make VARCHAR,
        model VARCHAR,
        electric_vehicle_type VARCHAR,
        cafv_eligibility VARCHAR,
        electric_range INTEGER,
        base_msrp DOUBLE,
        legislative_district INTEGER,
        dol_vehicle_id INTEGER,
        vehicle_location VARCHAR,
        electric_utility VARCHAR,
        census_tract_2020 BIGINT
        )
    
    """)

def load_data(con):
    con.execute("""
        INSERT INTO electric_cars
        SELECT * FROM read_csv_auto('data/Electric_Vehicle_Population_Data.csv', header=True)
    """)


def autos_por_ciudad(con):
    resultado = con.execute("""
        SELECT
            city,
            COUNT(*) AS car_count
        FROM electric_cars
        GROUP BY city
        ORDER BY car_count DESC, city
    """).fetchall()

    print("Cantidad de autos por ciudad:")
    for row in resultado:
        print(row)

    return resultado

def top_tres_vehiculos(con):
    resultado = con.execute("""
        SELECT
            make,
            model,
            COUNT(*) AS vehicle_count
        FROM electric_cars
        GROUP BY make, model
        ORDER BY vehicle_count DESC, make, model
        LIMIT 3
    """).fetchall()

    print("Top 3 vehículos:")
    for row in resultado:
        print(row)

    return resultado


def auto_por_codigo_postal(con):
    resultado = con.execute("""
        WITH vehicle_counts AS (
            SELECT
                postal_code,
                make,
                model,
                COUNT(*) AS vehicle_count
            FROM electric_cars
            GROUP BY postal_code, make, model
        ),
        ranked_vehicles AS (
            SELECT
                postal_code,
                make,
                model,
                vehicle_count,
                ROW_NUMBER() OVER (
                    PARTITION BY postal_code
                    ORDER BY vehicle_count DESC, make, model
                ) AS position
            FROM vehicle_counts
        )
        SELECT
            postal_code,
            make,
            model,
            vehicle_count
        FROM ranked_vehicles
        WHERE position = 1
        ORDER BY postal_code
    """).fetchall()

    print("Vehículo más popular por código postal:")
    for row in resultado:
        print(row)

    return resultado

def autos_por_modelo(con):
    Path("output").mkdir(exist_ok=True)
    con.execute("""
        COPY (
            SELECT
                model_year,
                COUNT(*) AS car_count
            FROM electric_cars
            GROUP BY model_year
            ORDER BY model_year
        )
        TO 'output/model_year'
        (
            FORMAT PARQUET,
            PARTITION_BY (model_year)
        )
    """)


if __name__ == "__main__":
    main()
