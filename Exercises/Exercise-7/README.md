## Ejercicio 7 - Uso de varias funciones de PySpark

En este ejercicio vamos a resolver algunos problemas que requerirán
usar varias funciones de PySpark. Solo deberías usar las funciones proporcionadas en `spark.sql.functions`.
¡No uses UDF ni métodos de Python para resolver los problemas! Usaremos archivos de datos de fallas
de discos rígidos de código abierto como fuente de datos.

#### Configuración
1. Cambiá de directorio en la línea de comandos
   para estar dentro de la carpeta `Exercise-7`: `cd Exercises/Exercise-7`
   
2. Ejecutá `docker build --tag=exercise-7 .` para construir la imagen de `Docker`.

3. Hay un archivo llamado `main.py` en el directorio `Exercise-7`; allí debe ir tu código de `PySpark` para completar el ejercicio.
   
4. Cuando hayas terminado el proyecto o quieras probar tu código,
   ejecutá el siguiente comando: `docker-compose up run` desde el directorio `Exercises/Exercise-7`.

#### Enunciado del problema
Hay una carpeta llamada `data` en este directorio actual, `Exercises/Exercise-7`. Dentro de ella
hay un archivo `csv` comprimido como `.zip`, que debe permanecer comprimido durante todo este
ejercicio. El archivo se llama `hard-drive-2022-01-01-failures.csv.zip`. (Estos datos son gratuitos
y provienen de https://www.backblaze.com/b2/hard-drive-test-data.html)

En general, los archivos tienen este aspecto:
```
date,serial_number,model,capacity_bytes,failure,smart_1_normalized,smart_1_raw,smart_2_normalized,smart_2_raw,smart_3_normalized,smart_3_raw,smart_4_normalized,smart_4_raw,smart_5_normalized,smart_5_raw,smart_7_normalized,smart_7_raw,smart_8_normalized,smart_8_raw,smart_9_normalized,smart_9_raw,smart_10_normalized,smart_10_raw,smart_11_normalized,smart_11_raw,smart_12_normalized,smart_12_raw,smart_13_normalized,smart_13_raw,smart_15_normalized,smart_15_raw,smart_16_normalized,smart_16_raw,smart_17_normalized,smart_17_raw,smart_18_normalized,smart_18_raw,smart_22_normalized,smart_22_raw,smart_23_normalized,smart_23_raw,smart_24_normalized,smart_24_raw,smart_160_normalized,smart_160_raw,smart_161_normalized,smart_161_raw,smart_163_normalized,smart_163_raw,smart_164_normalized,smart_164_raw,smart_165_normalized,smart_165_raw,smart_166_normalized,smart_166_raw,smart_167_normalized,smart_167_raw,smart_168_normalized,smart_168_raw,smart_169_normalized,smart_169_raw,smart_170_normalized,smart_170_raw,smart_171_normalized,smart_171_raw,smart_172_normalized,smart_172_raw,smart_173_normalized,smart_173_raw,smart_174_normalized,smart_174_raw,smart_175_normalized,smart_175_raw,smart_176_normalized,smart_176_raw,smart_177_normalized,smart_177_raw,smart_178_normalized,smart_178_raw,smart_179_normalized,smart_179_raw,smart_180_normalized,smart_180_raw,smart_181_normalized,smart_181_raw,smart_182_normalized,smart_182_raw,smart_183_normalized,smart_183_raw,smart_184_normalized,smart_184_raw,smart_187_normalized,smart_187_raw,smart_188_normalized,smart_188_raw,smart_189_normalized,smart_189_raw,smart_190_normalized,smart_190_raw,smart_191_normalized,smart_191_raw,smart_192_normalized,smart_192_raw,smart_193_normalized,smart_193_raw,smart_194_normalized,smart_194_raw,smart_195_normalized,smart_195_raw,smart_196_normalized,smart_196_raw,smart_197_normalized,smart_197_raw,smart_198_normalized,smart_198_raw,smart_199_normalized,smart_199_raw,smart_200_normalized,smart_200_raw,smart_201_normalized,smart_201_raw,smart_202_normalized,smart_202_raw,smart_206_normalized,smart_206_raw,smart_210_normalized,smart_210_raw,smart_218_normalized,smart_218_raw,smart_220_normalized,smart_220_raw,smart_222_normalized,smart_222_raw,smart_223_normalized,smart_223_raw,smart_224_normalized,smart_224_raw,smart_225_normalized,smart_225_raw,smart_226_normalized,smart_226_raw,smart_230_normalized,smart_230_raw,smart_231_normalized,smart_231_raw,smart_232_normalized,smart_232_raw,smart_233_normalized,smart_233_raw,smart_234_normalized,smart_234_raw,smart_235_normalized,smart_235_raw,smart_240_normalized,smart_240_raw,smart_241_normalized,smart_241_raw,smart_242_normalized,smart_242_raw,smart_244_normalized,smart_244_raw,smart_245_normalized,smart_245_raw,smart_246_normalized,smart_246_raw,smart_247_normalized,smart_247_raw,smart_248_normalized,smart_248_raw,smart_250_normalized,smart_250_raw,smart_251_normalized,smart_251_raw,smart_252_normalized,smart_252_raw,smart_254_normalized,smart_254_raw,smart_255_normalized,smart_255_raw
2022-01-01,ZLW18P9K,ST14000NM001G,14000519643136,0,73,20467240,,,90,0,100,12,100,0,87,495846641,,,89,9937,100,0,,,100,12,,,,,,,,,100,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,100,0,100,0,,,66,34,,,100,2,99,2641,34,34,,,,,100,0,100,0,200,0,10
```

Tu tarea es leer este archivo con `PySpark` y responder las siguientes preguntas.
Respondé cada pregunta agregando una nueva columna con la respuesta.

1. Agregar el nombre de archivo como una columna del DataFrame y llamarla `source_file`.
2. Extraer la `date` ubicada dentro de la cadena de la columna `source_file`. El tipo de dato final debe ser
`date` o `timestamp`, no `string`. Llamar a la nueva columna `file_date`.
3. Agregar una nueva columna llamada `brand`. Se basará en la columna `model`. Si la
columna `model` contiene un espacio, es decir, ` `, dividirla usando ese `space`. El valor
   encontrado antes del espacio ` ` se considerará la `brand`. Si no hay
   ningún espacio para dividir, completar `brand` con el valor `unknown`.
   
4. Inspeccionar una columna llamada `capacity_bytes`. Crear un DataFrame secundario que
relacione `capacity_bytes` con la columna `model`; crear "buckets" / "rankings" para
   esos modelos, desde el de mayor capacidad hasta el de menor. Incorporar esos
   datos al conjunto principal como una columna llamada `storage_ranking`.
   
5. Crear una columna llamada `primary_key` que sea un `hash` de las columnas que hacen único
un registro en este conjunto de datos.


Nota: tu código de `PySpark` debe estar encapsulado dentro de funciones o métodos.

Crédito adicional: escribí pruebas unitarias para tu código de PySpark.
