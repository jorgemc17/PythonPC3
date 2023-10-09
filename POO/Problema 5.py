""" 
Cree una clase Alumno e inicialícela con el nombre y el número de registro. 
Haga los métodos para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante. 
"""
class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        info = f"Nombre: {self.nombre}\nNúmero de Registro: {self.num_registro}"
        if self.edad is not None:
            info += f"\nEdad: {self.edad}"
        else:
            info += "\nEdad: No asignada"
        if self.notas:
            info += "\nNotas:\n"
            for i, nota in enumerate(self.notas, start=1):
                info += f"Nota {i}: {nota}\n"
        else:
            info += "\nNotas: No asignadas"
        print(info)

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

alumno1 = Alumno("Jorge", "172417")
alumno1.setAge(23)
alumno1.setNota([80, 75, 84])

alumno2 = Alumno("Genesis", "17195")
alumno2.setAge(22)
alumno2.setNota([84, 98, 79])

alumno1.display()
print()
alumno2.display()
