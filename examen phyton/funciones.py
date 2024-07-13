import json
def editarProducto(idPar:int,nombrePar:str,precioPar:int):
    with open("compras.json",mode="r")as lecturaJson:
        leerjson = json.load(lecturaJson)
        #print(leerjson["productos"])
        contador = 0
        for i in leerjson["productos"]:
            if  i["id"] == idPar:
                print("Encontre el producto-----> ",contador)
                break
            contador+=1
        leerjson["productos"][contador]["nombre"]=nombrePar
        leerjson["productos"][contador]["precio"]=precioPar

    with open("compras.json", mode="w")as escribirJson:
        json.dump(leerjson,escribirJson,indent=4)



#editarProducto(30,"11111",111111)
        

def listarProductos():
    with open("compras.json",mode="r")as lecturaJson:
        leerjson = json.load(lecturaJson)

        print("ID       NOMBRE      PRECIO")
        for i in leerjson["productos"]:
            print(i["id"],i["nombre"],i["precio"])


#listarProductos()
            

def crearJson():
    miJson={
            "id": 1,
            "nombre": "1010",
            "precio": 1010
        }

    with open("nuevo_json_creado.json", mode="w")as escribirJson:
        json.dump(miJson,escribirJson,indent=4)
    
