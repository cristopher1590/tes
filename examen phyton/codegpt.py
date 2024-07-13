""" import csv
import json

def mostrar(datos):
    for linea in datos:
        print(linea)

def abrirjson():
    with open('crimen_history.json', mode='r') as archivo_json:
        datos = json.load(archivo_json)
    return datos

def abrircsv():
    with open('people_list.csv', mode='r', encoding="utf8") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        # Convertir el lector a una lista para poder mostrar o procesar los datos posteriormente
        datos = list(lector_csv)
    return datos

#Cargar datos desde CSV y JSON
datos_csv = abrircsv()
datos_json = abrirjson()

#Mostrar datos cargados
print("Datos del archivo CSV:")
mostrar(datos_csv)

print("\nDatos del archivo JSON:")
print(datos_json)  # Aquí puedes imprimir directamente el JSON completo o procesarlo como necesites """

import csv
import json
import time

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # Leer el archivo CSV
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)

    # Convertir la lista de diccionarios a una cadena JSON
    jsonString = json.dumps(jsonArray, indent=4)

    # Escribir la cadena JSON en un archivo
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(jsonString)

# Rutas de los archivos
csvFilePath = r'data.csv'
jsonFilePath = r'data.json'

# Convertir CSV a JSON
start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversión de 100,000 filas completada con éxito en {finish - start:.4f} segundos")
