""" 
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar
try:
...
except ValueError:
...
except ZeroDivisionError:
...
"""


def calcular_porcentaje(fraccion):
    try:
        x, y = map(int, fraccion.split('/'))

        if y == 0 :
            raise Exception(f"Hay un error debido a que el dividendo es {y}")
        elif x > y:
            raise Exception(f"Hay un error debido a que la divisio sale {x/y} mayor a 100%, y el combutible no puede exceder su limite")

        porcentaje = (x / y) * 100

        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f'{round(porcentaje)}%'

    except (ValueError, ZeroDivisionError):
        return "Error: Ingrese una fracción válida (X/Y) donde X e Y sean enteros"


while True:
    fraccion = input("Introduce una fracción, con formato X/Y: ")
    resultado = calcular_porcentaje(fraccion)
    print(resultado)
    if resultado != "Error: Ingrese una fracción válida (X/Y) donde X e Y sean enteros":
        break




