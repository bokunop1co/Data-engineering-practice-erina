import duckdb



def main():
    con = duckdb.connect("electric_cars.db")
    create_table(con)
    load_data(con)
    con.close()

    pass


def create_table(con):
    con.execute("""
        CREATE TABLE electric_cars(
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


if __name__ == "__main__":
    main()
