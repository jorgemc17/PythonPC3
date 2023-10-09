""" 
Cree un programa que solicite al usuario una lista de calificaciones 
separadas por comas. Divida la cadena en calificaciones individuales y 
almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except 
para informar al usuario cuando los valores introducidos no puedan ser 
convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad) 
""" 

def obtener_calificaciones():
    calificaciones_enteros = []
    while True:
        calificaciones_input = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones = calificaciones_input.split(',')

        for calificacion in calificaciones:
            calificacion = calificacion.strip()
            try:
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)
            except ValueError:
                print(f"Error: '{calificacion}' no es una calificación válida (debe ser un número entero).")

        if len(calificaciones_enteros) > 0:
            return calificaciones_enteros

calificaciones = obtener_calificaciones()
print("Calificaciones correctamente ingresadas:", calificaciones)
