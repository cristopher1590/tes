import csv
import json

def mostrar(datos):
    for l in datos:
    
     print(l)
            
             
def abrirjson():
    with open('crime_history.json', mode ='r') as archivos_json:
        
        leer = json.load(archivos_json)
    
        return(leer)
        

def abrircsv():

    with open('people_list.csv', mode= 'r',encoding="utf8") as archivo_csv:

        leer = csv.DictReader(archivo_csv)
 
        return(list(leer)) 
    
    
def buscarDni(datoscsv):
    dnibuscar = input('ingrese una dni: ')
    for fila in datoscsv:
        if fila['DNI'] == dnibuscar:
            print(fila)
            break
    else:
        print('DNI no encontrado')
    return(fila)

def buscar_rut(datosjson,dni):
    
    for fila in datosjson:
        if fila['rut'] == dni['DNI']:
            print(fila)
            break
        else:
            print('rut no encontrado')
        

datos_csv = abrircsv()
datos_json = abrirjson()
dni = buscarDni(datos_csv)
buscar_rut(datos_json, dni)



""" mostrar(datos_csv) """
#89924440-Y
