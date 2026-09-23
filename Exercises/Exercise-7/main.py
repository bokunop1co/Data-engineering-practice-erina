from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql import Window


def main():
    spark = SparkSession.builder.appName("Exercise7").enableHiveSupport().getOrCreate()
    # tu código va aquí

    #leer el archivo CSV
    df= spark.read.csv("data/hard-drive-2022-01-01-failures.csv.zip", header=True, inferSchema=True)
    #1
    df=source(df)

    #2
    df=file(df)

    #3
    df=brand(df)

    #4
    df=model(df)

    #5
    df=primary(df)

    spark.stop()

def source(df):
    df=df.withColumn("source_file", F.input_file_name())
    return df


def file(df):
    df= df.withColumn("file_date", F.to_date(F.regexp_extract(F.col("source_file"), r"(\d{4}-\d{2}-\d{2})", 1), "yyyy-MM-dd"))
    return df
    


def brand(df):
    df= df.withColumn(
            "brand",
            F.when(F.col("model").contains(" "), F.split(F.col("model"), " ")[0])
             .otherwise("unknown")
            
        )
    return df       

def model(df): 

    model_capacity = df.select("model", "capacity_bytes").distinct()
    
    window_spec = Window.orderBy(F.col("capacity_bytes").desc())
    
    model_capacity=model_capacity.withColumn(
            "storage_ranking",
            F.dense_rank().over(window_spec)
        )
    model_capacity = model_capacity.select("model","storage_ranking")
    df= df.join(model_capacity, on="model", how="left")

    return df

def primary(df):
    df = df.withColumn(
            "primary_key",
            F.sha2(F.concat_ws("_", F.col("serial_number"), F.col("date")), 256)
        )
    return df

if __name__ == "__main__":
    main()
