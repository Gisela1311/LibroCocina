from receta import Receta

class Libro:
    def __init__(self, n:str, fc: str, fa:str):
        self.nombre = n
        self.fecha_creacion = fc
        self.fecha_actualización = fa
        self.recetas = {"entrante":[], "postres":[], "principal": []} #arreglar para hacer el diccionario

    def __str__(self):
        return self.nombre, self.fecha_creacion, self.fecha_actualización
    
    def guarda_receta(self, receta:Receta):
        if receta.tipo not in self.recetas:
            print(f"El tipo {receta.tipo} NO existe en este libro")
        else:
            self.recetas[receta.tipo].append(receta)

    
    def listar_tipo (self):
        for listareceta in self.recetas.values():
            for receta in listareceta:
                print(receta)

    def buscar_receta (self, nombre):
        for listareceta in self.recetas.values():
            for receta in listareceta:
                if receta.nombre ==  nombre:
                    return receta
        print(f"No se ha encontrado la receta con nombre: {nombre}")

