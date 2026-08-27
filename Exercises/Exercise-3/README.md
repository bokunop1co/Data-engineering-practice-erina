## Ejercicio n.º 3 - Boto3 AWS + s3 + Python

En este tercer ejercicio vas a volver a practicar tus habilidades de Python;
vamos a ampliar la idea de descargar archivos y comenzar a recuperar archivos
de un bucket de nube `s3` en `aws` mediante un proceso de varios pasos.

Trabajar con el paquete de `Python` `boto3` para interactuar con `aws` es muy
común, y esto te dará una introducción a ese tema.


#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-3`: `cd Exercises/Exercise-3`
   
2. Ejecutá `docker build --tag=exercise-3 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-3`; allí debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-3`.

#### Enunciado del problema
AWS publica algunos datos web de "common crawl", disponibles en `s3` sin necesidad
de permisos especiales. http://commoncrawl.org/the-data/get-started/

Tu tarea tiene dos partes: descargar un archivo `.gz` ubicado en el bucket s3 `commoncrawl`
y con la clave `crawl-data/CC-MAIN-2022-05/wet.paths.gz` usando `boto3`.

Una vez descargado este archivo, debés extraerlo, abrirlo y descargar nuevamente con `boto3`
la uri del archivo ubicada en la primera línea. Almacená el archivo localmente y recorré sus líneas,
imprimiendo cada una en `stdout`.

En general, tu script debería hacer lo siguiente:
1. `boto3` download the file from s3 located at bucket `commoncrawl` and key `crawl-data/CC-MAIN-2022-05/wet.paths.gz`
2. extraer y abrir este archivo con Python (pista: es simplemente texto);
3. obtener la `uri` de la primera línea de este archivo;
4. volver a descargar ese archivo `uri` desde `s3` usando `boto3`;
5. imprimir cada línea y recorrerla hacia stdout/línea de comandos/terminal.

Crédito adicional:

1. NO cargues el archivo final completo en memoria antes de imprimir cada línea; transmití el archivo en streaming.
   
2. NO descargues el archivo `gz` inicial en el disco; descargalo, extraelo y leelo en memoria.
