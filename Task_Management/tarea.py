class Tarea:
    id_counter = 1

    def __init__(self, descripcion, fecha_vencimiento, estado):
        self.id = Tarea.id_counter
        Tarea.id_counter += 1
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "fecha_vencimiento": self.fecha_vencimiento,
            "estado": self.estado
        }

class TareaSimple(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, estado):
        super().__init__(descripcion, fecha_vencimiento, estado)

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["tipo"] = "simple"
        return base_dict

class TareaRecurrente(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, estado, frecuencia):
        super().__init__(descripcion, fecha_vencimiento, estado)
        self.frecuencia = frecuencia

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["frecuencia"] = self.frecuencia
        base_dict["tipo"] = "recurrente"
        return base_dict
