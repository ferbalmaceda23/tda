def BFS(grafo, origen, destino, camino):
 
        vertices_grafo = grafo.obtener_vertices()
        # Marco todos los vértices como no visitados
        visitados = {v:False for v in vertices_grafo}
 
        por_visitar = []
        # Agrego el nodo origen a la lista de por visitar
        por_visitar.append(origen)
        visitados[origen] = True

        while por_visitar:

            v = por_visitar.pop(0)
            for adyacente in grafo.obtener_adyacentes(v):
                capacidad = grafo.obtener_peso(v, adyacente)
                if visitados[adyacente] == False and capacidad > 0:
                    # Si se llega al destino, se guarda su "padre" en camino[destino]
                    # y se devuelve True, ya que terminó el BFS
                    por_visitar.append(adyacente)
                    visitados[adyacente] = True
                    camino[adyacente] = v
                    if adyacente == destino:
                        return True

        return False # No se alcanzó el destino
