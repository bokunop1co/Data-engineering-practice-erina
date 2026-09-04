import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
target_date = "2024-01-19 15:30" # cambiar fecha a buscar


def main():
    response = requests.get(base_url, timeout=60)
    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    archivo = None

    for tr in soup.find_all("tr"):
        columnas = tr.find_all("td")
        if len(columnas) >= 2:
            enlace = columnas[0].find("a", href=True)
            fecha = columnas[1].get_text(strip=True)
            if enlace and target_date in fecha:
                archivo = enlace["href"]
                break

    if archivo is None:
        raise ValueError(f"No se encontró el archivo con fecha: {target_date}")

    url_archivo = urljoin(base_url, archivo)
    print("Archivo encontrado:", archivo)
    print("URL completa:", url_archivo)

    # Descargar el archivo
    respuesta_archivo = requests.get(url_archivo, timeout=60)
    respuesta_archivo.raise_for_status()
    with open("archivo_local.csv", "wb") as f:
        f.write(respuesta_archivo.content)

    # Leer con pandas
    df = pd.read_csv("archivo_local.csv", low_memory=False)

    # Convertir la columna a numérica
    df["HourlyDryBulbTemperature"] = pd.to_numeric(
        df["HourlyDryBulbTemperature"], errors="coerce" # convierte fallos a Nulos
    )

    # Encontrar el valor máximo
    max_temp = df["HourlyDryBulbTemperature"].max()

    # Mostrar solo las filas con ese máximo
    resultado = df[df["HourlyDryBulbTemperature"] == max_temp]

    print("\nRegistros con temperatura máxima:\n")
    print(resultado.to_string(index=False))


if __name__ == "__main__":
    main()
