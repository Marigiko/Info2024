from gestion_ventas import GestionVentas
from venta import VentaOnline, VentaLocal
import json

def guardar_ventas_json(gestion_ventas, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump([venta.to_dict() for venta in gestion_ventas.ventas], f)

def cargar_ventas_json(archivo_json):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            return GestionVentas.from_dict_list(data)
    except FileNotFoundError:
        return GestionVentas()

def mostrar_menu():
    print("=== Sistema de Gestión de Ventas ===")
    print("1. Registrar venta online")
    print("2. Registrar venta local")
    print("3. Listar ventas")
    print("4. Actualizar venta")
    print("5. Eliminar venta")
    print("6. Historial de ventas por cliente")
    print("7. Guardar y salir")

def ejecutar_opcion(opcion, gestion_ventas):
    try:
        if opcion == '1':
            fecha = input("Fecha de la venta (dd/mm/yyyy): ")
            cliente = input("Nombre del cliente: ")
            productos = input("Productos vendidos (separados por coma): ").split(',')
            metodo_pago = input("Método de pago: ")
            gestion_ventas.registrar_venta(VentaOnline(fecha, cliente, productos, metodo_pago))
        elif opcion == '2':
            fecha = input("Fecha de la venta (dd/mm/yyyy): ")
            cliente = input("Nombre del cliente: ")
            productos = input("Productos vendidos (separados por coma): ").split(',')
            vendedor = input("Nombre del vendedor: ")
            gestion_ventas.registrar_venta(VentaLocal(fecha, cliente, productos, vendedor))
        elif opcion == '3':
            gestion_ventas.listar_ventas()
        elif opcion == '4':
            id_venta = int(input("ID de la venta a actualizar: "))
            nueva_fecha = input("Nueva fecha (dejar en blanco para no cambiar): ")
            gestion_ventas.actualizar_venta(id_venta, nueva_fecha)
        elif opcion == '5':
            id_venta = int(input("ID de la venta a eliminar: "))
            gestion_ventas.eliminar_venta(id_venta)
        elif opcion == '6':
            guardar_ventas_json(gestion_ventas, 'data.json')
            print("Ventas guardadas. Saliendo...")
            return False
        elif opcion == '7':
            cliente = input("Cliente para historial: ")
            gestion_ventas.historial_ventas_por_cliente(cliente)
        else:
            print("Opción no válida.")
        return True
    except ValueError:
        print("Error en los datos ingresados. Por favor, intenta nuevamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return True

if __name__ == "__main__":
    gestion_ventas = cargar_ventas_json('data.json')
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion, gestion_ventas)
