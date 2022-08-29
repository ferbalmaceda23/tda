from bellmanford import BellmanFord
from dijkstra import Dijkstra

def Johnson(grafo):

    grafo_modificado = grafo.crear_copia()
    origen_bellmanford = "Q"

    pesos_modificados = BellmanFord(grafo_modificado, origen_bellmanford)

    vertices_grafo = grafo.obtener_vertices()

    for origen in vertices_grafo:
        for destino in grafo.obtener_adyacentes(origen):
            peso = grafo.obtener_peso(origen, destino)
            if peso != 0:
                peso_nuevo = peso + pesos_modificados[origen] - pesos_modificados[destino]
                grafo_modificado.borrar_arista(origen, destino)
                grafo_modificado.agregar_arista(origen, destino, peso_nuevo)

    vertices_grafo_modificado = grafo_modificado.obtener_vertices()

    distancias = {i:{} for i in vertices_grafo_modificado}

    for origen in vertices_grafo_modificado:
        distancias[origen] = Dijkstra(grafo, grafo_modificado, origen)

    for origen in vertices_grafo:
        for destino in vertices_grafo:
            distancias[origen][destino] = distancias[origen][destino] - pesos_modificados[origen] + pesos_modificados[destino]

    return distancias