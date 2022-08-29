INFINITO = float("Inf")

def BellmanFord(grafo, origen_bellmanford):

    grafo.agregar_vertice(origen_bellmanford)

    for vertice in grafo.obtener_vertices():
        if (not grafo.estan_relacionados(origen_bellmanford, vertice)) and (vertice != origen_bellmanford):
            grafo.agregar_arista(origen_bellmanford, vertice, 0)

    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()

    distancias = {i:INFINITO for i in vertices}
    distancias[origen_bellmanford] = 0

    for vertice in vertices:
        for origen,destino,peso in aristas:
            if (distancias[origen] != INFINITO) and ((distancias[origen] + peso) < distancias[destino]):
                distancias[destino] = distancias[origen] + peso
    
    grafo.borrar_vertice(origen_bellmanford)
    del distancias[origen_bellmanford]

    return distancias