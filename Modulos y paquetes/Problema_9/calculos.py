import operacionesBasicas

if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        resultado_suma = operacionesBasicas.suma(a, b)
        print(f"Suma: {resultado_suma}")

        resultado_resta = operacionesBasicas.resta(a, b)
        print(f"Resta: {resultado_resta}")

        resultado_producto = operacionesBasicas.producto(a, b)
        print(f"Producto: {resultado_producto}")

        resultado_division = operacionesBasicas.division(a, b)
        print(f"División: {resultado_division}")

    except:
        print("Error: Ingrese valores numéricos válidos.")
