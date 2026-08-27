## Ejercicio 10 - Calidad de datos con Great Expectations

En este ejercicio vamos a aprender sobre la calidad de datos y sus comprobaciones,
específicamente con una herramienta llamada Great Expectations. https://greatexpectations.io/
Tenemos un conjunto de datos en Postgres junto con un pipeline existente que presenta
problemas de calidad de datos; tenés que implementar comprobaciones de calidad de datos para detectar estos problemas.

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-10`: `cd Exercises/Exercise-10`
   
2. Ejecutá `docker build --tag=exercise-10 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-10`; allí existe el pipeline de datos
   y deben colocarse las comprobaciones de calidad de datos.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-10`.
   El código debería generar algunos errores de calidad de datos.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-10`. Dentro de ella
hay un archivo `csv`. El archivo se llama `202306-divvy-tripdate.csv`. Es un conjunto de datos de código abierto
de viajes en bicicleta.

En general, los archivos tienen este aspecto:
```
"ride_id","rideable_type","started_at","ended_at","start_station_name","start_station_id","end_station_name","end_station_id","start_lat","start_lng","end_lat","end_lng","member_casual"
"6F1682AC40EB6F71","electric_bike","2023-06-05 13:34:12","2023-06-05 14:31:56",,,,,41.91,-87.69,41.91,-87.7,"member"
```

Recientemente, los análisis que calculan las duraciones máximas de los viajes en bicicleta mostraron duraciones
muy extrañas y largas. Se espera que la mayoría de los viajes en bicicleta comiencen y terminen el mismo día. Necesitamos
implementar una alerta de calidad de datos que nos avise cuando obtengamos duraciones de viaje erróneas.

1. Usar Great Expectations para cumplir este requisito.
2. El conjunto de datos actual incluye duraciones de viaje erróneas; cuando ejecutes este pipeline (usando `docker-compose up run`),
   tus comprobaciones de calidad de datos deberían detectarlas.


Si no sabés por dónde empezar, consultá esta publicación: https://www.confessionsofadataguy.com/great-expectations-with-apache-spark-a-tale-of-data-quality/


