""" 
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador 
radio. La clase “CIRCULO” debe tener un método que puede calcular el área 
en utilizando el atributo radio. 
"""
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

radio_circulo = float(input("Ingrese el radio del círculo: "))
mi_circulo = Circulo(radio_circulo)
area_del_circulo = mi_circulo.calcular_area()
print(f"El área del círculo con radio es: {area_del_circulo:.2f}")
