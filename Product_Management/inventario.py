from producto import Producto, ProductoElectronico, ProductoAlimenticio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]

    def listar_productos(self):
        for p in self.productos:
            print(p.to_dict())

    def actualizar_cantidad(self, nombre, cantidad):
        for p in self.productos:
            if p.nombre == nombre:
                p.actualizar_cantidad(cantidad)
                
    def reporte_inventario_por_categoria(self):
        categorias = {}
        for p in self.productos:
            if p.categoria in categorias:
                categorias[p.categoria] += 1
            else:
                categorias[p.categoria] = 1
        print("Reporte de Inventario por Categoría:")
        for categoria, cantidad in categorias.items():
            print(f"{categoria}: {cantidad} productos")

    @classmethod
    def from_dict_list(cls, data_list):
        inventario = cls()
        for data in data_list:
            if 'garantia' in data:
                producto = ProductoElectronico(
                    nombre=data['nombre'],
                    precio=data['precio'],
                    cantidad=data['cantidad'],
                    garantia=data['garantia'],
                    **data['detalles']
                )
            elif 'fecha_expiracion' in data:
                producto = ProductoAlimenticio(
                    nombre=data['nombre'],
                    precio=data['precio'],
                    cantidad=data['cantidad'],
                    fecha_expiracion=data['fecha_expiracion'],
                    **data['detalles']
                )
            else:
                producto = Producto(
                    nombre=data['nombre'],
                    precio=data['precio'],
                    cantidad=data['cantidad'],
                    **data['detalles']
                )
            inventario.agregar_producto(producto)
        return inventario
