## Ejercicio 9 - Aprendé el cálculo diferido de Polars

En este ejercicio vamos a aprender a trabajar con conjuntos de datos más grandes que la memoria.
Para hacerlo usaremos Polars.
https://www.pola.rs/

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-9`: `cd Exercises/Exercise-9`
   
2. Ejecutá `docker build --tag=exercise-9 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-9`; allí debe ir tu código de `Polars` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-9`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-9`. Dentro de ella
hay un archivo `csv`. El archivo se llama `202306-divvy-tripdate.csv`. Es un conjunto de datos de código abierto
de viajes en bicicleta.

En general, los archivos tienen este aspecto:
```
"ride_id","rideable_type","started_at","ended_at","start_station_name","start_station_id","end_station_name","end_station_id","start_lat","start_lng","end_lat","end_lng","member_casual"
"6F1682AC40EB6F71","electric_bike","2023-06-05 13:34:12","2023-06-05 14:31:56",,,,,41.91,-87.69,41.91,-87.7,"member"
```

Tu tarea es usar la funcionalidad `Lazy` de `Polars` para trabajar con estos datos de manera eficiente.

1. Leer el archivo `CSV` proporcionado en un DataFrame diferido.

3. Calcular los siguientes análisis/problemas.
 - Convertir todos los tipos de datos a los correctos.
 - Contar la cantidad de viajes en bicicleta por día.
 - Calcular la cantidad promedio, máxima y mínima de viajes por semana del conjunto de datos.
 - Para cada día, calcular cuántos viajes por encima o por debajo del mismo día de la semana anterior hubo ese día.
