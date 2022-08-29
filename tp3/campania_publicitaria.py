import os, sys
from grafo import Grafo
from bfs import BFS

def limpiar_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def inicializar_grafo(ruta_archivo):
    grafo = Grafo(dirigido=True)
    origen = None
    destino = None
    
    with open(ruta_archivo) as reader:
        info_vuelos = reader.readlines()

        for info_vuelo in info_vuelos:
            vuelo = info_vuelo.rstrip("\n").split(",")
            if len(vuelo) == 1:
                if not origen:
                    origen = vuelo[0]
                elif not destino:
                    destino = vuelo[0]
            else:
                vertice1, vertice2, peso = vuelo[0], vuelo[1], vuelo[2]
                
                grafo.agregar_vertice(vertice1) if vertice1 not in grafo else None
                grafo.agregar_vertice(vertice2) if vertice2 not in grafo else None
                if not grafo.estan_relacionados(vertice1, vertice2):
                    grafo.agregar_arista(vertice1, vertice2, int(peso))

    return grafo, origen, destino

# Crea el grafo residual inicial del grafo recibido
def crear_grafo_residual(grafo):

    grafo_residual = grafo.crear_copia()
    aristas_grafo = grafo_residual.obtener_aristas()

    for (origen, destino, peso) in aristas_grafo:
        if not grafo_residual.estan_relacionados(destino, origen):
            grafo_residual.agregar_arista(destino, origen, 0)

    return grafo_residual

# Devuelve el flujo máximo de origen a destino en el grafo recibido, y devuelve
# el grafo residual resultante
def edmonds_karp(grafo, origen, destino):
    
    grafo_residual = crear_grafo_residual(grafo)
    vertices_grafo = grafo_residual.obtener_vertices()

    # Diccionario donde se guarda el vértice "padre" de cada vértice
    # De esta forma, se puede recorrer los padres de los vértices desde el 
    # destino para hallar el camino más corto realizado por BFS
    camino = {v:-1 for v in vertices_grafo}

    flujo_max = 0

    # Se aumenta el flujo mientras haya algún camino posible de origen a destino
    while BFS(grafo_residual, origen, destino, camino):

        # Busca el bottleneck (mínima capacidad en el camino encontrado por BFS), recorriendo
        # el diccionario de camino
        bottleneck = float("Inf")
        actual = destino
        while(actual !=  origen):
            bottleneck = min(bottleneck, grafo_residual.obtener_peso(camino[actual], actual))
            actual = camino[actual]
        
        flujo_max += bottleneck

        # Actualizo las capacidades de las aristas en el grafo residual
        j = destino
        while(j != origen):
            i = camino[j]
            grafo_residual.actualizar_peso(i, j, grafo_residual.obtener_peso(i,j) - bottleneck)
            grafo_residual.actualizar_peso(j, i, grafo_residual.obtener_peso(j,i) + bottleneck)
            j = camino[j]
       
    return flujo_max, grafo_residual

# Busca los vértices accesibles del grafo desde el origen
def buscar_vertices_accesibles(grafo, origen):
    vertices_grafo = grafo.obtener_vertices()
    accesibles = [origen]
    for vertice in grafo.obtener_adyacentes(origen):
        if grafo.obtener_peso(origen, vertice) != 0:
            if vertice not in accesibles:
                accesibles.append(vertice)
            for adyacente in grafo.obtener_adyacentes(vertice):
                if grafo.obtener_peso(vertice, adyacente) != 0:
                    if adyacente not in accesibles:
                        accesibles.append(adyacente)

    return accesibles


def campania_publicitaria(ruta_archivo):
    
    grafo, origen, destino = inicializar_grafo(ruta_archivo)
    vertices_grafo = grafo.obtener_vertices()
    flujo_maximo, grafo_residual = edmonds_karp(grafo, origen, destino)

    # Busco los vértices accesibles desde el origen
    vertices_accesibles = buscar_vertices_accesibles(grafo_residual, origen)

    # Busco las aristas que conectan vértices accesibles con vértices NO accesibles, que a 
    # su vez pertenezcan al grafo original. Esas serán las aristas que conformen el corte mínimo, 
    # es decir, donde deberán ir las publicidades
    corte_minimo = []
    for vertice in vertices_accesibles:
        for adyacente in grafo.obtener_adyacentes(vertice):
            if adyacente not in vertices_accesibles:
                corte_minimo.append((vertice, adyacente, grafo.obtener_peso(vertice, adyacente)))

    print(f'\nEl flujo máximo es {flujo_maximo}')
    print('La publicidad debe ir en las aristas:')
    for (origen, destino, peso) in corte_minimo:
        print(f'\n\t{origen}---{peso}--->{destino}')


def main():
    limpiar_terminal()
    argumentos_terminal = sys.argv
    if len(argumentos_terminal) == 1:
        print("Debe ingresar la ruta del archivo para continuar.")
    elif not os.path.isfile(argumentos_terminal[1]):
        print("Debe ingresar la ruta de un archivo que exista.")
    else:
        campania_publicitaria(argumentos_terminal[1])

if __name__ == "__main__":
    main()
