import copy

class Grafo:
    def __init__(self, **kwargs):
        self.vertices = {}
        self.dirigido = kwargs["dirigido"]

    def __len__(self):
        return len(self.vertices)
 
    def __contains__(self, vertice): 
        return vertice in self.vertices
 
    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}
 
    def agregar_arista(self, origen, destino, peso):
        self.vertices[origen][destino] = peso
        if not self.dirigido: self.vertices[destino][origen] = peso
 
    def borrar_vertice(self, vertice):
        for vecino in self.vertices:
            if vertice in self.vertices[vecino].keys():
                del self.vertices[vecino][vertice]
        del self.vertices[vertice]
 
    def borrar_arista(self, origen, destino):
        del self.vertices[origen][destino]
        if not self.dirigido: del self.vertices[destino][origen]
 
    def estan_relacionados(self, origen, destino):
        return destino in self.vertices[origen]
 
    def obtener_vertices(self):
        return list(self.vertices)
    
    def obtener_aristas(self):
        aristas = []
        for origen in self.obtener_vertices():
            for destino in self.obtener_adyacentes(origen):
                peso = self.obtener_peso(origen, destino)
                aristas.append((origen, destino, peso))
        return aristas

    def obtener_adyacentes(self, vertice):
        return self.vertices[vertice].keys()

    def obtener_peso(self, origen, destino):
        return self.vertices[origen][destino]

    def actualizar_peso(self, origen, destino, nuevo_peso):
        del self.vertices[origen][destino]
        if not self.dirigido: del self.vertices[destino][origen]
        self.vertices[origen][destino] = nuevo_peso
        if not self.dirigido: self.vertices[destino][origen] = nuevo_peso

    def crear_copia(self):
        return copy.deepcopy(self)