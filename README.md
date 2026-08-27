## Problemas prácticos de Ingeniería de Datos

Uno de los principales desafíos de la Ingeniería de Datos es la gran
variedad de habilidades técnicas que pueden ser necesarias en el
trabajo diario.

*** Nota: si enviás por correo un enlace a tu repositorio de GitHub con todos los
ejercicios completos, te enviaré una copia gratuita de mi libro electrónico Introduction to Data Engineering. ***

El objetivo de este repositorio es ayudarte a desarrollar y
aprender esas habilidades. En general, estos son los temas
principales que cubren estos problemas prácticos.

- Procesamiento de datos con Python.
- csv, flat-file, parquet, json, etc.
- Diseño de tablas de bases de datos SQL.
- Python + Postgres, ingesta y recuperación de datos.
- PySpark
- Limpieza de datos / datos sucios.

### Cómo trabajar en los problemas
Vas a necesitar dos cosas para trabajar eficazmente en la mayoría
de estos problemas.
- `Docker`
- `docker-compose`

Todas las herramientas y tecnologías que necesitás estarán incluidas
en el `dockerfile` de cada ejercicio.

Para cada ejercicio vas a tener que hacer `cd` en esa carpeta y
ejecutar el comando `docker build`; ese comando estará indicado en
el `README` de cada ejercicio. Seguí esas instrucciones.

### Ejercicios para principiantes

#### Ejercicio 1 - Descarga de archivos
El [primer ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-1) evalúa tu capacidad para descargar varios archivos
desde una fuente `HTTP` y descomprimirlos, almacenándolos localmente con `Python`.
Ejecutá `cd Exercises/Exercise-1` y consultá el `README` de esa ubicación para ver las instrucciones.

#### Ejercicio 2 - Web scraping + descarga + Pandas
El [segundo ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-2)
evalúa tu capacidad para hacer web scraping, construir uris, descargar archivos y usar Pandas para
realizar algunas operaciones acumulativas simples.
Ejecutá `cd Exercises/Exercise-2` y consultá el `README` de esa ubicación para ver las instrucciones.

#### Ejercicio 3 - Boto3 AWS + s3 + Python
El [tercer ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-3) evalúa varias habilidades.
Esta vez vamos a usar un paquete popular de `aws` llamado `boto3` para intentar realizar varias
acciones en varios pasos para descargar algunos archivos de datos de código abierto desde `s3`.
Ejecutá `cd Exercises/Exercise-3` y consultá el `README` de esa ubicación para ver las instrucciones.

#### Ejercicio 4 - Conversión de JSON a CSV + directorios irregulares
El [cuarto ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-4)
se enfoca en los tipos de archivo `json` y `csv`, y en trabajar con ellos en `Python`.
Vas a tener que recorrer una estructura de directorios irregular, encontrar los archivos `json`
y convertirlos a `csv`.

#### Ejercicio 5 - Modelado de datos para Postgres + Python
El [quinto ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-5)
va a ser un poco diferente de los demás. En este problema se te proporcionarán varios archivos
`csv`. Debés crear un modelo de datos / esquema para almacenar estos conjuntos de datos, incluidos los índices,
y luego crear todas las tablas dentro de `Postgres` conectándote a la base de datos con `Python`.


### Ejercicios intermedios

#### Ejercicio 6 - Ingesta y agregación con PySpark
El [sexto ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-6)
sube un poco la dificultad y pasa a herramientas más populares. En este ejercicio vamos a
cargar algunos archivos usando `PySpark` y luego realizar algunas agregaciones básicas.
¡Buena suerte!

#### Ejercicio 7 - Uso de varias funciones de PySpark
El [séptimo ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-7)
retoma el ejercicio anterior y se enfoca en usar algunas de las funciones integradas más comunes de PySpark,
`pyspark.sql.functions`, y aplicarlas a problemas de la vida real.

Muchas veces, para resolver problemas simples tenemos que encontrar y usar varias funciones disponibles
en las bibliotecas. Esto pondrá a prueba tu capacidad para hacerlo.

#### Ejercicio 8 - Uso de DuckDB para análisis y transformaciones
El [octavo ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-8)
Usar herramientas nuevas es fundamental para crecer como ingeniero de datos. DuckDB es una de esas herramientas. En este
ejercicio vas a tener que completar varias tareas analíticas y de transformación usando DuckDB. Esto
va a requerir comprender las funciones y la documentación de DuckDB.

#### Ejercicio 9 - Uso del cálculo diferido de Polars
El [noveno ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-9)
Polars es una herramienta nueva basada en Rust, con un excelente paquete de Python, que revolucionó la Ingeniería de Datos.
Es mejor que Pandas porque tiene SQL Context y admite la evaluación diferida para conjuntos de datos más grandes que la memoria.
¡Demostrá tus habilidades con Lazy!


### Ejercicios avanzados

#### Ejercicio 10 - Calidad de datos con Great Expectations
El [décimo ejercicio](https://github.com/danielbeach/data-engineering-practice/tree/main/Exercises/Exercise-10)
te ayudará a aprender sobre calidad de datos, específicamente sobre una herramienta llamada Great Expectations. Se te
proporcionará un conjunto de datos existente en formato CSV, junto con un pipeline existente. Hay un problema de calidad de datos
y se te pedirá que implementes algunas comprobaciones de calidad de datos para detectar algunos de estos problemas.