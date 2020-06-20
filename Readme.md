# DATASET UTILIZADO
  La url de descarga del dataset usado es la siguiente: https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download
  El archivo ya desccargado se encuentra en: ./data/positivos_covid.csv

# LIMPIEZA DE DATOS
  Se filtraron los datos del departamento asignado (CUSCO), adicionalmente se eliminaron columnas
  no requeridas para el análisis y se creo una columna de rango de edades.
  Esto se hizo mediante python y para ejecutar el script se deberá poner en consola el siguiente comando:
  ```python3 dataset.py``` en macOS o Linux
  ```python dataset.py``` en Windows

# LISTADO DE ILUSTRACIONES ELABORADAS
  En el archivo excel c_ilustraciones.xlsx se podrán encontrar los gráficos creados para la tarea.
  El archivo está dividido en 5 pestañas: DATA, 01, 02, 03, 04
  A continuación se va a detallar el contenido de cada archivo

    DATA: Archivo que contiene el dataset, con data limpia, utilizado para la tarea.
    01: Contiene el gráfico de "Cantidad de Casos Positivos por Provincia"
    02: Contiene el gráfico de "Cantidad de Casos Positivos por Sexo"
    03: Contiene el gráfico de "Cantidad de Casos Positivos por Edad"
    04: Contiene el gráfico de "Cantidad de Casos Positivos por Fecha de Resultado"

# URL DEL VÍDEO
  https://youtu.be/XQgoRscTEA4