## Ejercicio n.º 4 - Conversión de JSON a CSV + directorios irregulares

En este cuarto ejercicio vas a volver a practicar tus habilidades de Python;
vamos a buscar en una estructura de directorios irregular para encontrar archivos `json`.
Cuando encontremos archivos `json`, los convertiremos a archivos `csv`.

Podemos trabajar con tres excelentes paquetes de `Python`: `glob`, `json` y `csv`.


#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-4`: `cd Exercises/Exercise-4`
   
2. Ejecutá `docker build --tag=exercise-4 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-4`; allí debe ir tu código de `Python` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-4`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-4`. También hay
archivos `json` ubicados en distintos lugares dentro de esta estructura de directorios.

Tu tarea es usar `Python` para encontrar todos los archivos `json` ubicados en la carpeta `data`.
Una vez encontrados, leelos con `Python` y convertílos a archivos `csv`; para hacerlo
vas a tener que aplanar algunas de las estructuras de datos `json` anidadas.

Por ejemplo, hay un `{"type":"Point","coordinates":[-99.9,16.88333]}` que debe aplanarse.

En general, tu script debería hacer lo siguiente:
1. recorrer el directorio `data` con `Python` e identificar todos los archivos `json`;
2. cargar todos los archivos `json`;
3. aplanar la estructura de datos `json`;
4. escribir los resultados en un archivo `csv`, uno por cada archivo json, incluidos los nombres de encabezado.