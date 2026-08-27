## Ejercicio n.º 2 - Web scraping y descarga de archivos con Python

En este segundo ejercicio vas a volver a practicar tus habilidades de Python;
vamos a ampliar la idea de descargar archivos desde fuentes `HTTP` con Python, pero agregando una variante.

Vas a tener que hacer "web scraping" de una página `HTML` para buscar una fecha e identificar
el archivo correcto con el que construir una URL para descargarlo.


#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-2`: `cd Exercises/Exercise-2`
   
2. Ejecutá `docker build --tag=exercise-2 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-2`; allí debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-2`.

#### Enunciado del problema
Tenés que descargar un archivo de datos meteorológicos desde un sitio web gubernamental.
El archivo se encuentra en la siguiente ubicación especificada.

https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

You are looking for the file that was `Last Modified` on `2024-01-19 10:27	`, you
can't cheat and lookup the file number yourself. You must use Python to scrape
this webpage, finding the corresponding file-name for this timestamp, `2024-01-19 10:27	`

Una vez que hayas obtenido y descargado el archivo correcto, debés cargarlo en `Pandas` y encontrar
los registros con el valor más alto de `HourlyDryBulbTemperature`. Imprimí esos registros en la línea de comandos.

En general, tu script debería hacer lo siguiente:
1. Attempt to web scrap/pull down the contents of `https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/`
2. Analizar su estructura y determinar cómo encontrar el archivo correspondiente a `2024-01-19 10:27	` usando Python.
3. Construir la `URL` necesaria para descargar este archivo y escribirlo localmente.
4. Abrir el archivo con `Pandas` y encontrar los registros con el valor más alto de `HourlyDryBulbTemperature`.
5. Imprimir el resultado en stdout/línea de comandos/terminal.
