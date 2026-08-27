import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def extraer_nombre(url):
    return url.split("/")[-1]


def descargar(url, ruta):
    nombre = extraer_nombre(url)
    try:
        respuesta = requests.get(url, timeout=30)
        if respuesta.status_code == 200:
            destino = ruta / nombre
            destino.write_bytes(respuesta.content)
            with zipfile.ZipFile(destino) as zf:
                zf.extractall(ruta)
            destino.unlink()
        else:
            print(f"Error al descargar {url}: {respuesta.status_code}")
    except Exception as e:
        print(f"Error al procesar {url}: {e}")


def main():
    ruta = Path("downloads")
    ruta.mkdir(exist_ok=True)

    with ThreadPoolExecutor(max_workers=7) as executor:
        for url in download_uris:
            executor.submit(descargar, url, ruta)


if __name__ == "__main__":
    main()
