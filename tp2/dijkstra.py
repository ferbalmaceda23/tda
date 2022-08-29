from collections import defaultdict

INFINITO = float("Inf")

def distancia_minima(distancias, visitados, origen_dijkstra):

    (minimo, vertice_minimo) = (INFINITO, origen_dijkstra)

    for vertice in distancias.keys():
        if (minimo > distancias[vertice]) and (visitados[vertice] == False):
            (minimo, vertice_minimo) = (distancias[vertice], vertice)

    return vertice_minimo

def Dijkstra(grafo, grafo_modificado, origen_dijkstra):

    vertices_grafo = grafo.obtener_vertices()

    visitados = defaultdict(lambda : False)

    distancias = {i:INFINITO for i in vertices_grafo}
    distancias[origen_dijkstra] = 0

    for contador in range(len(grafo)):
        vertice_actual = distancia_minima(distancias, visitados, origen_dijkstra)
        visitados[vertice_actual] = True

        for vertice in vertices_grafo:
            if grafo.estan_relacionados(vertice_actual, vertice):
                peso_grafo_original = grafo.obtener_peso(vertice_actual, vertice)
                peso_grafo_modificado = grafo_modificado.obtener_peso(vertice_actual, vertice)
                
                if (visitados[vertice] == False) and (peso_grafo_original) and ((distancias[vertice] > distancias[vertice_actual]) + peso_grafo_modificado):
                    distancias[vertice] = distancias[vertice_actual] + grafo_modificado.obtener_peso(vertice_actual, vertice)

    return distancias