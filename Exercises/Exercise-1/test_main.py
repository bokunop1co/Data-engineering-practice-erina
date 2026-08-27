from main import extraer_nombre


def test_extraer_nombre():
    url = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip"
    nombre = extraer_nombre(url)
    assert nombre == "Divvy_Trips_2018_Q4.zip"


def test_extraer_nombre_sin_barra():
    url = "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip"
    nombre = extraer_nombre(url)
    assert nombre == "Divvy_Trips_2018_Q4.zip"
