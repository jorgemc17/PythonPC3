""" 
Una tienda de autopartes necesita un programa para catalogar sus productos, crear 
la clase Catálogo y Producto, realizar un objeto dentro de un catálogo productos 
el cual debe tener un método para agregar productos y otra para mostrar toda 
la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi 
mismo se puede agregar más atributos a los productos para que se puedan hacer 
otras funcionalidades. Guiarse de
https://github.com/gdelgador/ProgramacionPython/blob/main/Modulo3/scripts/clases_objetos/catalogo_peliculas.py 
"""
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        print('Se ha creado el producto:', self.nombre)

    def __str__(self):
        return '{} (Año: {}, Precio: ${:.2f})'.format(self.nombre, self.año, self.precio)

class Catalogo:
    productos = []

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return Catalogo(productos_filtrados)

autoparte1 = Producto("Filtro de aire", 15.99, 2022)
autoparte2 = Producto("Batería de auto", 89.99, 2021)
autoparte3 = Producto("Aceite de motor", 12.99, 2022)

catalogo_autopartes = Catalogo([autoparte1, autoparte2, autoparte3])

catalogo_autopartes.agregar(Producto("Llantas", 59.99, 2022))
catalogo_autopartes.agregar(Producto("Amortiguadores", 49.99, 2020))

print('Catálogo de Autopartes:')
catalogo_autopartes.mostrar()

print('\nProductos de Autopartes del año 2022:')
catalogo_filtrado = catalogo_autopartes.filtrar_por_año(2022)
catalogo_filtrado.mostrar()
