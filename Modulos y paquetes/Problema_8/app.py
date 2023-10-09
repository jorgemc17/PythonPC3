import pmodulo 

if __name__ == "__main__":
    numeros_aleatorios = pmodulo.generar_numeros_aleatorios()
    print("Números aleatorios generados:")
    pmodulo.mostrar_lista(numeros_aleatorios)

    numeros_ordenados = pmodulo.ordenar_lista(numeros_aleatorios)
    print("\nNúmeros ordenados:")
    pmodulo.mostrar_lista(numeros_ordenados)