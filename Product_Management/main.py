from inventario import Inventario
from producto import ProductoElectronico, ProductoAlimenticio
import json

def cargar_datos_csv(archivo_csv):
    productos = []
    with open(archivo_csv, 'r', encoding='latin-1') as file:
        next(file)
        for linea in file:
            campos = linea.strip().split(';')
            productos.append({
                "tienda": campos[0],
                "marca": campos[1],
                "tipo": campos[2],
                "genero": campos[3],
                "talla": campos[4],
                "color": campos[5],
                "categoria": campos[6],
                "precio_venta": float(campos[7]),
                "fecha": campos[8],
                "hora": campos[9]
            })
    return productos

def guardar_inventario_json(inventario, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump([producto.to_dict() for producto in inventario.productos], f)

def cargar_inventario_json(archivo_json):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            return Inventario.from_dict_list(data)
    except FileNotFoundError:
        return Inventario()

def mostrar_menu():
    print("=== Sistema de Gestión de Productos ===")
    print("1. Agregar producto electrónico")
    print("2. Agregar producto alimenticio")
    print("3. Listar productos")
    print("4. Actualizar cantidad de producto")
    print("5. Eliminar producto")
    print("6. Cargar productos desde ventas.csv")
    print("7. Reporte de inventario por categoría")
    print("8. Guardar y salir")

def ejecutar_opcion(opcion, inventario):
    try:
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            garantia = input("Garantía: ")
            inventario.agregar_producto(ProductoElectronico(nombre, precio, cantidad, garantia))
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            fecha_expiracion = input("Fecha de expiración: ")
            inventario.agregar_producto(ProductoAlimenticio(nombre, precio, cantidad, fecha_expiracion))
        elif opcion == '3':
            inventario.listar_productos()
        elif opcion == '4':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(nombre, cantidad)
        elif opcion == '5':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '6':
            productos_csv = cargar_datos_csv('../ventas.csv')
            for p in productos_csv:
                inventario.agregar_producto(ProductoElectronico(
                    nombre=p['marca'] + ' ' + p['tipo'],
                    precio=p['precio_venta'],
                    cantidad=1,
                    garantia="1 año"
                ))
        elif opcion == '7':
            guardar_inventario_json(inventario, 'data.json')
            print("Inventario guardado. Saliendo...")
            return False
        elif opcion == '8':
            inventario.reporte_inventario_por_categoria()
        else:
            print("Opción no válida.")
        return True
    except ValueError:
        print("Error en los datos ingresados. Por favor, intenta nuevamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return True

if __name__ == "__main__":
    inventario = cargar_inventario_json('data.json')
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion, inventario)
