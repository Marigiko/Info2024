from venta import Venta, VentaOnline, VentaLocal

class GestionVentas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def eliminar_venta(self, id_venta):
        self.ventas = [v for v in self.ventas if v.id != id_venta]

    def listar_ventas(self):
        for v in self.ventas:
            print(v.to_dict())

    def actualizar_venta(self, id_venta, nueva_fecha=None):
        for v in self.ventas:
            if v.id == id_venta:
                if nueva_fecha:
                    v.fecha = nueva_fecha
                    
    def historial_ventas_por_cliente(self, cliente):
        ventas_cliente = [v for v in self.ventas if v.cliente == cliente]
        print(f"Historial de Ventas para {cliente}:")
        for v in ventas_cliente:
            print(v.to_dict())

    @classmethod
    def from_dict_list(cls, data_list):
        gestion_ventas = cls()
        for data in data_list:
            if data.get("tipo") == "online":
                venta = VentaOnline(
                    fecha=data["fecha"],
                    cliente=data["cliente"],
                    productos=data["productos"],
                    metodo_pago=data["metodo_pago"]
                )
            elif data.get("tipo") == "local":
                venta = VentaLocal(
                    fecha=data["fecha"],
                    cliente=data["cliente"],
                    productos=data["productos"],
                    vendedor=data["vendedor"]
                )
            else:
                venta = Venta(
                    fecha=data["fecha"],
                    cliente=data["cliente"],
                    productos=data["productos"]
                )
            gestion_ventas.registrar_venta(venta)
        return gestion_ventas
