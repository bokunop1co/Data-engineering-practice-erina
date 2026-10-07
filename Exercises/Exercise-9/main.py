import polars as pl


def main():
    trips = pl.scan_csv("data/202306-divvy-tripdata.csv")
    print("Tipos detectados al leer el CSV:")
    print(trips.collect_schema())

    trips = trips.with_columns(
        pl.col("ride_id").cast(pl.String),
        pl.col("rideable_type").cast(pl.String),
        pl.col("started_at").str.strptime(
            pl.Datetime,
            format="%Y-%m-%d %H:%M:%S",
        ),
        pl.col("ended_at").str.strptime(
            pl.Datetime,
            format="%Y-%m-%d %H:%M:%S",
        ),
        pl.col("start_station_name").cast(pl.String),
        pl.col("start_station_id").cast(pl.String),
        pl.col("end_station_name").cast(pl.String),
        pl.col("end_station_id").cast(pl.String),
        pl.col("start_lat").cast(pl.Float64),
        pl.col("start_lng").cast(pl.Float64),
        pl.col("end_lat").cast(pl.Float64),
        pl.col("end_lng").cast(pl.Float64),
        pl.col("member_casual").cast(pl.String),
    )

    print("Tipos después de la conversión:")
    print(trips.collect_schema())

    daily_counts = contar_viajes_por_dia(trips)
    print("Cantidad de viajes por día:")
    print(daily_counts.collect())

    comparison = comparar_con_semana_anterior(daily_counts)
    print("Comparación con el mismo día de la semana anterior:")
    print(comparison.collect())

    weekly_totals, weekly_stats = resumen_semanal(daily_counts)
    print("Viajes totales por semana:")
    print(weekly_totals.collect())

    print("Resumen semanal:")
    print(weekly_stats.collect())


def contar_viajes_por_dia(trips):
    return (
        trips.with_columns(
            pl.col("started_at").dt.date().alias("dia")
        )
        .group_by("dia")
        .agg(
            pl.len().alias("cantidad_viajes")
        )
        .sort("dia")
    )


def resumen_semanal(daily_counts):
    weekly_totals = (
        daily_counts.with_columns(
            pl.col("dia").dt.truncate("1w").alias("semana")
        )
        .group_by("semana")
        .agg(
            pl.col("cantidad_viajes").sum().alias("viajes_semana")
        )
        .sort("semana")
    )

    weekly_stats = weekly_totals.select(
        pl.col("viajes_semana").mean().alias("promedio_semanal"),
        pl.col("viajes_semana").max().alias("maximo_semanal"),
        pl.col("viajes_semana").min().alias("minimo_semanal"),
    )

    return weekly_totals, weekly_stats

def comparar_con_semana_anterior(daily_counts):
    return (
        daily_counts
        .sort("dia")
        .with_columns(
            pl.col("cantidad_viajes")
            .cast(pl.Int64)
            .shift(7)
            .alias("viajes_mismo_dia_semana_anterior")
        )
        .with_columns(
            (
                pl.col("cantidad_viajes").cast(pl.Int64)
                - pl.col("viajes_mismo_dia_semana_anterior")
            ).alias("diferencia")
        )
    )


if __name__ == "__main__":
    main()
