from tarea import Tarea, TareaSimple, TareaRecurrente
from collections import defaultdict

class GestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, id_tarea):
        self.tareas = [t for t in self.tareas if t.id != id_tarea]

    def listar_tareas(self):
        for t in self.tareas:
            print(t.to_dict())

    def actualizar_tarea(self, id_tarea, nueva_descripcion=None, nueva_fecha=None, nuevo_estado=None):
        for t in self.tareas:
            if t.id == id_tarea:
                if nueva_descripcion:
                    t.descripcion = nueva_descripcion
                if nueva_fecha:
                    t.fecha_vencimiento = nueva_fecha
                if nuevo_estado:
                    t.estado = nuevo_estado
                    
    def tareas_pendientes_por_fecha(self):
        tareas_pendientes = defaultdict(list)
        for t in self.tareas:
            if t.estado == "pendiente":
                tareas_pendientes[t.fecha_vencimiento].append(t.to_dict())
        print("Tareas Pendientes por Fecha de Vencimiento:")
        for fecha, tareas in sorted(tareas_pendientes.items()):
            print(f"{fecha}:")
            for tarea in tareas:
                print(f"  {tarea}")

    @classmethod
    def from_dict_list(cls, data_list):
        gestion_tareas = cls()
        for data in data_list:
            if data.get("tipo") == "recurrente":
                tarea = TareaRecurrente(
                    descripcion=data["descripcion"],
                    fecha_vencimiento=data["fecha_vencimiento"],
                    estado=data["estado"],
                    frecuencia=data["frecuencia"]
                )
            else:
                tarea = TareaSimple(
                    descripcion=data["descripcion"],
                    fecha_vencimiento=data["fecha_vencimiento"],
                    estado=data["estado"]
                )
            gestion_tareas.agregar_tarea(tarea)
        return gestion_tareas
