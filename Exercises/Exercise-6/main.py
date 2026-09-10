import zipfile
from io import TextIOWrapper

import pandas as pd
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    to_date,
    month,
    year,
    desc,
    row_number,
    lit,
    date_sub,
)
from pyspark.sql.window import Window


def main():
    spark = (
        SparkSession.builder.appName("Exercise6")
        .enableHiveSupport()
        .getOrCreate()
    )
    df_2019 = read_zip_csv(spark, "data/Divvy_Trips_2019_Q4.zip")
    df_2019.show(5)
    average_duration_per_day(df_2019)
    trips_per_day(df_2019)
    month_popular(df_2019)
    top_3_estaciones(df_2019)
    avg_duration_per_gender(df_2019)
    avg_duration_per_age(df_2019)


def read_zip_csv(spark: SparkSession, zip_path: str) -> DataFrame:
    with zipfile.ZipFile(zip_path) as z:
        csv_name = [n for n in z.namelist() if n.endswith(".csv")][0]
        with z.open(csv_name) as f:
            pdf = pd.read_csv(TextIOWrapper(f, encoding="utf-8"))
            pdf["gender"] = pdf["gender"].fillna("Unknown")

    return spark.createDataFrame(pdf)


def average_duration_per_day(df):
    fecha = df.withColumn("start_time", to_date(df["start_time"]))

    prom = (
        fecha.groupBy("start_time")
        .agg({"tripduration": "avg"})
        .withColumnRenamed("avg(tripduration)", "average_duration")
    )

    prom.write.csv(
        "reports/average_duration_per_day", header=True, mode="overwrite"
    )

    return prom


def trips_per_day(df):
    fecha = df.withColumn("start_time", to_date(df["start_time"]))

    trips = (
        fecha.groupBy("start_time")
        .count()
        .withColumnRenamed("count", "trips_per_day")
    )

    trips.write.csv(
        "reports/trips_per_day", header=True, mode="overwrite"
    )

    return trips


def month_popular(df):
    mes = df.withColumn("month", month(df["start_time"]))
    estacion = mes.groupBy("month", "from_station_name").count()

    ventana = Window.partitionBy("month").orderBy(desc("count"))
    estacion = estacion.withColumn("row_number", row_number().over(ventana))
    estacion = estacion.filter(estacion["row_number"] == 1).drop("row_number")

    estacion.write.csv(
        "reports/month_popular", header=True, mode="overwrite"
    )

    return estacion


def top_3_estaciones(df):
    fecha = df.withColumn("start_time", to_date(df["start_time"]))
    fecha_max = fecha.agg({"start_time": "max"}).collect()[0][0]
    fecha_filtrada = fecha.filter(
        fecha["start_time"] >= date_sub(lit(fecha_max), 14)
    )

    mes = fecha_filtrada.groupBy("start_time", "from_station_name").count()

    ventana = Window.partitionBy("start_time").orderBy(desc("count"))
    mes = mes.withColumn("row_number", row_number().over(ventana))
    mes = mes.filter(mes["row_number"] <= 3)

    mes.write.csv(
        "reports/top_3_estaciones", header=True, mode="overwrite"
    )

    return mes


def avg_duration_per_gender(df):
    genero = (
        df.groupBy("gender")
        .agg({"tripduration": "avg"})
        .withColumnRenamed("avg(tripduration)", "average_duration")
    )

    genero.write.csv(
        "reports/avg_duration_per_gender", header=True, mode="overwrite"
    )

    return genero


def avg_duration_per_age(df):
    edad = df.withColumn("age", year(df["start_time"]) - df["birthyear"])
    prom = (
        edad.groupBy("age")
        .agg({"tripduration": "avg"})
        .withColumnRenamed("avg(tripduration)", "average_duration")
    )

    top_largos = prom.orderBy(desc("average_duration")).limit(10)
    top_cortos = prom.orderBy("average_duration").limit(10)

    top_largos.write.csv(
        "reports/top_largos", header=True, mode="overwrite"
    )
    top_cortos.write.csv(
        "reports/top_cortos", header=True, mode="overwrite"
    )

    return top_largos, top_cortos


if __name__ == "__main__":
    main()
