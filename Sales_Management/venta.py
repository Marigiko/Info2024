class Venta:
    id_counter = 1

    def __init__(self, fecha, cliente, productos):
        self.id = Venta.id_counter
        Venta.id_counter += 1
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "cliente": self.cliente,
            "productos": self.productos,
        }

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos, metodo_pago):
        super().__init__(fecha, cliente, productos)
        self.metodo_pago = metodo_pago

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["metodo_pago"] = self.metodo_pago
        base_dict["tipo"] = "online"
        return base_dict

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos, vendedor):
        super().__init__(fecha, cliente, productos)
        self.vendedor = vendedor

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["vendedor"] = self.vendedor
        base_dict["tipo"] = "local"
        return base_dict
