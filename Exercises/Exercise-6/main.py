from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("Exercise6").enableHiveSupport().getOrCreate()
    # tu código va aquí


if __name__ == "__main__":
    main()
