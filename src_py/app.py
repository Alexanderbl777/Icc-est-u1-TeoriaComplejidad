from BenchMarking import generar_arreglo_maestro, ejecutar_benchmark, graficar_resultados

if __name__ == "__main__":
    print("Iniciando benchmark de algoritmos de ordenamiento...\n")
    maestro = generar_arreglo_maestro(100000)
    resultados = ejecutar_benchmark(maestro)
    graficar_resultados(resultados)
