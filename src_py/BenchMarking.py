import time
import copy
import matplotlib.pyplot as plt
import random
from SortMethods import (
    bubble_sort,
    bubble_sort_optimized,
    selection_sort,
    insertion_sort,
    shell_sort
)

tamaños = [5000, 10000, 30000, 50000, 100000]

algoritmos = {
    'bubble': bubble_sort,
    'bubbleMejorado': bubble_sort_optimized,
    'seleccion': selection_sort,
    'insercion': insertion_sort,
    'shell': shell_sort
}

def generar_arreglo_maestro(max_tamaño, semilla=42):
    random.seed(semilla)
    return [random.randint(1, 1000000) for _ in range(max_tamaño)]

def ejecutar_benchmark(maestro):
    resultados = {nombre: [] for nombre in algoritmos}
    for tamaño in tamaños:
        base = maestro[:tamaño]
        for nombre, algoritmo in algoritmos.items():
            arreglo = copy.deepcopy(base)
            inicio = time.time()
            algoritmo(arreglo)
            fin = time.time()
            duracion = fin - inicio
            resultados[nombre].append(duracion)
            print(f"Tamano: {tamaño}, Algoritmo: {nombre}, Tiempo: {duracion:.6f} segundos")
    return resultados

def graficar_resultados(resultados):
    for nombre, tiempos in resultados.items():
        plt.plot(tamaños, tiempos, label=nombre)
    plt.xlabel("Cantidad de elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafico_tiempos.png")
    plt.show()
