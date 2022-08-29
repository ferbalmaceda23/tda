import os, sys
from grafo import Grafo
from johnson import Johnson

INFINITO = float("Inf")

def limpiar_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def imprimir_techo(largo):
    print("╔" ,end='')
    print("═══╦"*largo, end='')
    print("═══╗")

def imprimir_division(largo):
    print("╠", end='')
    print("═══╬"*largo, end='')
    print("═══╣")

def imprimir_piso(largo):
    print("╚", end='')
    print("═══╩"*largo, end='')
    print("═══╝")

def mostrar_distancias(distancias):
    print("\nCADA FILA ES EL ORIGEN, LAS COLUMNAS EL DESTINO")
    vertices = list(distancias.keys())
    largo = len(distancias)
    imprimir_techo(largo)

    print("║   ", end='')
    for vertice in vertices:
        print(f"║ {vertice} ", end='')
    print("║")

    imprimir_division(largo)

    i = 0
    for vertice in vertices:
        print(f"║ {vertice} ║", end='')
        distancias_vertice = list(distancias[vertice].values())

        for distancia in distancias_vertice:
            if (distancia == INFINITO) or (distancia > 99) or (distancia < -9):
                print(f"{distancia}║", end='')
            elif (distancia < 0) or (distancia > 9):
                print(f"{distancia} ║", end='')
            else:
                print(f" {distancia} ║", end='')
        print()

        i+=1
        if i < largo: imprimir_division(largo)

    imprimir_piso(largo)

def sumar_distancias(distancias):
    suma = 0
    for vertice in distancias:
        suma+=distancias[vertice]
    return suma

def determinar_deposito_optimo(distancias_minimas):
    deposito_optimo = None
    menor_suma = None

    for vertice in distancias_minimas:
        suma_actual = sumar_distancias(distancias_minimas[vertice])
        if suma_actual != INFINITO:
            if (menor_suma == None) or (menor_suma > suma_actual):
                deposito_optimo = vertice
                menor_suma = suma_actual

    return deposito_optimo

def inicializar_grafo(ruta_archivo):
    grafo = Grafo(dirigido=True)

    with open(ruta_archivo) as reader:
        info_depositos = reader.readlines()

        for info_deposito in info_depositos:
            depositos = info_deposito.rstrip("\n")
            vertice1, vertice2, peso = depositos.split(",")
            
            grafo.agregar_vertice(vertice1) if vertice1 not in grafo else None
            grafo.agregar_vertice(vertice2) if vertice2 not in grafo else None
            if not grafo.estan_relacionados(vertice1, vertice2):
                grafo.agregar_arista(vertice1, vertice2, int(peso))

    return grafo

def minimizando_costos(ruta_archivo):

    grafo = inicializar_grafo(ruta_archivo)

    distancias_minimas = Johnson(grafo)

    deposito_optimo = determinar_deposito_optimo(distancias_minimas)

    if deposito_optimo is None:
        print("No hay deposito optimo")
    else:
        print(f"El deposito más optimo para colocar la fabrica es: {deposito_optimo}")
        mostrar_distancias(distancias_minimas)

def main():
    limpiar_terminal()
    argumentos_terminal = sys.argv
    if len(argumentos_terminal) == 1:
        print("Debe ingresar la ruta del archivo para continuar.")
    elif not os.path.isfile(argumentos_terminal[1]):
        print("Debe ingresar la ruta de un archivo que exista.")
    else:
        minimizando_costos(argumentos_terminal[1])

if __name__ == "__main__":
    main()