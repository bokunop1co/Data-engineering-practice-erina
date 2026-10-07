import os
from pathlib import Path

import great_expectations as gx
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    date_format,
    sum as _sum,
    to_timestamp,
    unix_timestamp,
)
from pyspark.sql.types import (
    DoubleType,
    StringType,
    StructField,
    StructType,
)


def create_spark_session():
    return SparkSession.builder.appName("BikeRideDuration").getOrCreate()


def build_schema():
    return StructType([
        StructField("ride_id", StringType(), True),
        StructField("rideable_type", StringType(), True),
        StructField("started_at", StringType(), True),
        StructField("ended_at", StringType(), True),
        StructField("start_station_name", StringType(), True),
        StructField("start_station_id", StringType(), True),
        StructField("end_station_name", StringType(), True),
        StructField("end_station_id", StringType(), True),
        StructField("start_lat", DoubleType(), True),
        StructField("start_lng", DoubleType(), True),
        StructField("end_lat", DoubleType(), True),
        StructField("end_lng", DoubleType(), True),
        StructField("member_casual", StringType(), True),
    ])


def load_trip_data(spark):
    df = spark.read.csv(
        "data/202306-divvy-tripdata.csv",
        header=True,
        schema=build_schema(),
        mode="DROPMALFORMED",
    )

    df = df.withColumn(
        "started_at", to_timestamp(col("started_at"), "yyyy-MM-dd HH:mm:ss")
    ).withColumn(
        "ended_at", to_timestamp(col("ended_at"), "yyyy-MM-dd HH:mm:ss")
    )

    df = df.withColumn(
        "duration_seconds",
        unix_timestamp(col("ended_at")) - unix_timestamp(col("started_at")),
    ).withColumn(
        "date", date_format(col("started_at"), "yyyy-MM-dd")
    )

    return df


def validate_trip_durations(df):
    pandas_df = df.select(
        "ride_id",
        "started_at",
        "ended_at",
        "duration_seconds",
    ).toPandas()

    context = gx.get_context(mode="ephemeral")
    batch = context.data_sources.pandas_default.read_dataframe(
        pandas_df,
        asset_name="bike_trip_data",
    )
    validator = context.get_validator(batch=batch)
    result = validator.expect_column_values_to_be_between(
        "duration_seconds",
        min_value=1,
        max_value=86400,
    )

    if result.success:
        print("✅ La validación de Great Expectations pasó: duración de viajes en rango esperado.")
        return

    invalid_rows = pandas_df.loc[
        ~pandas_df["duration_seconds"].between(1, 86400),
        ["ride_id", "started_at", "ended_at", "duration_seconds"],
    ]

    print("ERROR: Se detectaron duraciones erroneas en los viajes en bicicleta.")
    print(
        "Se esperaba que duration_seconds estuviera entre 1 y 86400 segundos "
        "y se encontraron filas invalidas."
    )
    print(f"Cantidad de filas inválidas: {len(invalid_rows)}")
    if not invalid_rows.empty:
        print(invalid_rows.head(10).to_string(index=False))
    print(result)


def main():
    spark = create_spark_session()
    try:
        df = load_trip_data(spark)
        validate_trip_durations(df)

        daily_durations = df.groupBy("date").agg(
            _sum("duration_seconds").alias("total_duration_seconds")
        )

        output_dir = Path("results")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / "output_file.parquet"

        try:
            daily_durations.write.mode("overwrite").parquet(str(output_path))
            print(f"Archivo generado en: {output_path}")
        except Exception as exc:
            if os.name == "nt":
                print(
                    "Advertencia: se omite la escritura de Parquet en Windows "
                    "porque Spark requiere Hadoop local para crear archivos. "
                    f"Detalle: {exc}"
                )
            else:
                raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()


