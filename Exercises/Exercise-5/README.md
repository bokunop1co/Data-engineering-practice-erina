## Ejercicio n.º 5 - Modelado de datos para Postgres + Python

En este quinto ejercicio vas a trabajar con varios temas:
modelado de datos, Python y Postgres. Son problemas comunes
en la ingeniería de datos.

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-5`: `cd Exercises/Exercise-5`
   
2. Ejecutá `docker build --tag=exercise-5 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-5`; allí debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-5`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-5`. También hay
3 archivos `csv` ubicados en esa carpeta. Abrí cada uno y examinálo; la
primera tarea es crear un script `sql` con el `DDL` que contenga
una sentencia `CREATE` para cada archivo de datos. Acordate de considerar los tipos de datos.
Además, estas sentencias `CREATE` deben incluir índices para cada tabla, así como
claves primarias y foráneas.

Después de terminar estos scripts `sql`, debemos conectarnos a `Postgres` usando el paquete de `Python`
llamado `psycopg2`. Una vez conectados, ejecutaremos nuestros scripts `sql` contra la base de datos.

Nota: el script `main.py` predeterminado ya tiene configurada la conexión de Python para conectarse
a la instancia de `Postgres` que `Docker` inicia automáticamente cuando ejecutás
el comando `docker-compose up run` (dentro del directorio `Exercises/Exercise-5`).

Finalmente, usaremos `psycopg2` para insertar los datos de cada archivo `csv` en la tabla que creaste.

En general, tu script debería hacer lo siguiente:
1. examinar cada archivo `csv` de la carpeta `data`. Diseñar una sentencia `CREATE` para cada archivo;
2. asegurarte de tener índices, claves primarias y foráneas;
3. usar `psycopg2` para conectarte a `Postgres` en `localhost` y el `port` predeterminado;
4. crear las tablas en la base de datos;
5. ingerir los archivos `csv` en las tablas creadas, también usando `psycopg2`.
