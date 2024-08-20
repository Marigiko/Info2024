class Producto:
    def __init__(self, nombre, precio, cantidad, **kwargs):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.detalles = kwargs

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "detalles": self.detalles
        }

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia, **kwargs):
        super().__init__(nombre, precio, cantidad, **kwargs)
        self.garantia = garantia

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["garantia"] = self.garantia
        return base_dict

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion, **kwargs):
        super().__init__(nombre, precio, cantidad, **kwargs)
        self.fecha_expiracion = fecha_expiracion

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["fecha_expiracion"] = self.fecha_expiracion
        return base_dict
