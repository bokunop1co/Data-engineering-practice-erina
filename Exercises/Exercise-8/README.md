## Ejercicio 8 - Comprensión y uso de DuckDB

En este ejercicio vamos a resolver algunos problemas que requerirán
usar varias funciones y capacidades de DuckDB. Podés consultar la documentación
en https://duckdb.org/docs/

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-8`: `cd Exercises/Exercise-8`
   
2. Ejecutá `docker build --tag=exercise-8 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-8`; allí debe ir tu código de `DuckDB` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-8`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-8`. Dentro de ella
hay un archivo `csv`. El archivo se llama `electric-cars.csv`. Es un conjunto de datos de código abierto
sobre vehículos eléctricos en el estado de Washington.

En general, los archivos tienen este aspecto:
```
VIN (1-10),County,City,State,Postal Code,Model Year,Make,Model,Electric Vehicle Type,Clean Alternative Fuel Vehicle (CAFV) Eligibility,Electric Range,Base MSRP,Legislative District,DOL Vehicle ID,Vehicle Location,Electric Utility,2020 Census Tract
5YJ3E1EB4L,Yakima,Yakima,WA,98908,2020,TESLA,MODEL 3,Battery Electric Vehicle (BEV),Clean Alternative Fuel Vehicle Eligible,322,0,14,127175366,POINT (-120.56916 46.58514),PACIFICORP,53077000904
5YJ3E1EA7K,San Diego,San Diego,CA,92101,2019,TESLA,MODEL 3,Battery Electric Vehicle (BEV),Clean Alternative Fuel Vehicle Eligible,220,0,,266614659,POINT (-117.16171 32.71568),,06073005102
7JRBR0FL9M,Lane,Eugene,OR,97404,2021,VOLVO,S60,Plug-in Hybrid Electric Vehicle (PHEV),Not eligible due to low battery range,22,0,,144502018,POINT (-123.12802 44.09573),,41039002401
```

Tu tarea es completar cada una de las tareas que aparecen a continuación, en orden, ya que dependen unas de otras.

1. crear una tabla de DuckDB, incluidos el DDL y los tipos de datos correctos, que almacene los datos de este archivo CSV.
 - inspeccionar los tipos de datos y crear un DDL razonable. No conviertas todo simplemente a `String`.

2. Leer el archivo `CSV` proporcionado en la tabla que creaste.

3. Calcular los siguientes análisis.
 - Contar la cantidad de autos eléctricos por ciudad.
 - Encontrar los 3 vehículos eléctricos más populares.
 - Encontrar el vehículo eléctrico más popular de cada código postal.
 - Contar la cantidad de autos eléctricos por año del modelo. Escribir la respuesta como archivos parquet particionados por año.


Nota: tu código de `DuckDB` debe estar encapsulado dentro de funciones o métodos.

Crédito adicional: escribí pruebas unitarias para tu código de `DuckDB`.
