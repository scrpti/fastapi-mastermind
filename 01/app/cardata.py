import json
# Clase que nos permite trabajar con los datos de prueba
class CarData:

    #Propiedades que almacenarán todos los datos
    coches=[]

    def __init__(self):
        #Carga de los ficheros de datos de prueba
        fileCoches=open('data/coches_usados.json')
        self.coches = json.load(fileCoches)

#COCHES
    #Devolucion asincrona de datos de acoches
    async def get_coches(self,skip,total):
        return {'coches':self.coches['coches'][skip:(total+skip)]}
    async def get_allICoches(self):
        return self.coches

    # Devolucion asincrona de coches de una marca en concreto
    async def get_cochesMarca(self,marca: str):
        # si no se encuentra el alimento se devolverá el nulo en vez de un objeto JSON
        coches=[]
        #Recorremos todos los datos JSON
        for item in self.coches['coches']:
            #Comparamos el id que es int
            if item['marca']==marca:
                coches.append(item)
        return coches

    # Devolucion asincrona de un coche
    async def get_coche(self,coche_id: int):
        # si no se encuentra el alimento se devolverá el nulo en vez de un objeto JSON
        coche=None
        #Recorremos todos los datos JSON
        for item in self.coches['coches']:
            #Comparamos el id que es int
            if item['id']==coche_id:
                coche=item
                break
        return coche