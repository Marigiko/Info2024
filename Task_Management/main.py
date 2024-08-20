from gestion_tareas import GestionTareas
from tarea import TareaSimple, TareaRecurrente
import json

def guardar_tareas_json(gestion_tareas, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump([tarea.to_dict() for tarea in gestion_tareas.tareas], f)

def cargar_tareas_json(archivo_json):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            return GestionTareas.from_dict_list(data)
    except FileNotFoundError:
        return GestionTareas()

def mostrar_menu():
    print("=== Sistema de Gestión de Tareas ===")
    print("1. Crear tarea simple")
    print("2. Crear tarea recurrente")
    print("3. Listar tareas")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Tareas pendientes por fecha de vencimiento")
    print("7. Guardar y salir")

def ejecutar_opcion(opcion, gestion_tareas):
    try:
        if opcion == '1':
            descripcion = input("Descripción de la tarea: ")
            fecha_vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ")
            estado = input("Estado (pendiente, en progreso, completada): ")
            gestion_tareas.agregar_tarea(TareaSimple(descripcion, fecha_vencimiento, estado))
        elif opcion == '2':
            descripcion = input("Descripción de la tarea: ")
            fecha_vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ")
            estado = input("Estado (pendiente, en progreso, completada): ")
            frecuencia = input("Frecuencia (diaria, semanal, mensual): ")
            gestion_tareas.agregar_tarea(TareaRecurrente(descripcion, fecha_vencimiento, estado, frecuencia))
        elif opcion == '3':
            gestion_tareas.listar_tareas()
        elif opcion == '4':
            id_tarea = int(input("ID de la tarea a actualizar: "))
            nueva_descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ")
            nueva_fecha = input("Nueva fecha de vencimiento (dejar en blanco para no cambiar): ")
            nuevo_estado = input("Nuevo estado (dejar en blanco para no cambiar): ")
            gestion_tareas.actualizar_tarea(id_tarea, nueva_descripcion, nueva_fecha, nuevo_estado)
        elif opcion == '5':
            id_tarea = int(input("ID de la tarea a eliminar: "))
            gestion_tareas.eliminar_tarea(id_tarea)
        elif opcion == '6':
            gestion_tareas.tareas_pendientes_por_fecha()
        elif opcion == '7':
            guardar_tareas_json(gestion_tareas, 'data.json')
            print("Tareas guardadas. Saliendo...")
            return False
        else:
            print("Opción no válida.")
        return True
    except ValueError:
        print("Error en los datos ingresados. Por favor, intenta nuevamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return True

if __name__ == "__main__":
    gestion_tareas = cargar_tareas_json('data.json')
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion, gestion_tareas)
