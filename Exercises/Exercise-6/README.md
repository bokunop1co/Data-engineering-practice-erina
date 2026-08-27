## Ejercicio 6 - Ingesta y agregación con PySpark

En este sexto ejercicio vamos a subir un nivel y empezar a usar algunas
herramientas de Big Data más comunes, en este caso Spark y PySpark.

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-6`: `cd Exercises/Exercise-6`
   
2. Ejecutá `docker build --tag=exercise-6 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-6`; allí debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-6`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-6`. Dentro de ella
hay dos archivos `csv` comprimidos como `.zip`, que deben permanecer comprimidos durante todo este
ejercicio.

En general, los archivos tienen este aspecto:
```
trip_id,start_time,end_time,bikeid,tripduration,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthyear
25223640,2019-10-01 00:01:39,2019-10-01 00:17:20,2215,940.0,20,Sheffield Ave & Kingsbury St,309,Leavitt St & Armitage Ave,Subscriber,Male,1987
25223641,2019-10-01 00:02:16,2019-10-01 00:06:34,6328,258.0,19,Throop (Loomis) St & Taylor St,241,Morgan St & Polk St,Subscriber,Male,1998
```

Tu tarea es leer estos archivos con `PySpark` y responder las siguientes preguntas. Cada respuesta
debe guardarse como un informe en formato `.csv` dentro de una carpeta `reports`.

1. ¿Cuál es la duración `average` de los viajes por día?
2. ¿Cuántos viajes se realizaron cada día?
3. ¿Cuál fue la estación de inicio más popular de los viajes de cada mes?
4. ¿Cuáles fueron las 3 estaciones de viajes principales de cada día durante las últimas dos semanas?
5. ¿Los `Male`s o las `Female`s realizan viajes más largos en promedio?
6. ¿Cuáles son las 10 principales edades de quienes realizan los viajes más largos y más cortos?

Nota: tu código de `PySpark` debe estar encapsulado dentro de funciones o métodos.

Crédito adicional: escribí pruebas unitarias para tu código de PySpark.
