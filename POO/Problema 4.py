
""" 
Definir una clase llamada “RECTANGULO” que puede ser construida por los 
atributos largo y ancho. La clase “RECTANGULO” debe tener un método 
que puede calcular el área utilizando los atributos de la clase. 
"""
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
mi_rectangulo = Rectangulo(largo, ancho)
area_rectangulo = mi_rectangulo.calcular_area()
print(f"El área del rectángulo es: {area_rectangulo:.2f}")
