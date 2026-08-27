## Ejercicio n.º 1 - Descarga de archivos con Python

En este primer ejercicio vas a practicar tus habilidades de Python,
además de aprender una tarea muy común: descargar archivos de datos
desde una fuente `HTTP`.
También vas a tener que descomprimir los archivos con Python.


#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-1`: `cd Exercises/Exercise-1`
   
2. Ejecutá `docker build --tag=exercise-1 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-1`; allí
   debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-1`.

#### Enunciado del problema
Tenés que descargar 10 archivos ubicados en las siguientes urls `HTTP` especificadas.
Para hacerlo vas a usar el paquete de `Python` `requests`.

Vas a tener que extraer el nombre de archivo de la uri de descarga.

Los archivos son archivos `zip` que también deben descomprimirse a su formato `csv`.

Deben descargarse en una carpeta llamada `downloads`, que actualmente no existe dentro de la carpeta `Exercise-1`.
Debés usar `Python` para crear el directorio; no lo hagas manualmente.

En general, tu script debería hacer lo siguiente:
1. crear el directorio `downloads` si no existe;
2. descargar los archivos uno por uno;
3. separar el nombre de archivo de la uri para que conserve su nombre original;
   
4. cada archivo es un `zip`; extraer el `csv` del `zip` y eliminar el archivo `zip`;
5. para obtener crédito adicional, descargar los archivos de manera `async` usando el paquete de `Python` `aiohttp`.
   También probá usar `ThreadPoolExecutor` en `Python` para descargar los archivos y escribí pruebas unitarias para mejorar tus habilidades.

#### Las URIs de descarga están listadas en el archivo `main.py`.

### Sugerencias
1. No asumas que todas las uri son válidas.
2. Una opción sería usar el método de `Python` `split()` para obtener el nombre de archivo de la uri,
   o buscar la última aparición de `/` y tomar el resto de la cadena.