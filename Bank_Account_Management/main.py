from gestion_cuentas import GestionCuentas
from cuenta_bancaria import CuentaBancariaCorrientes, CuentaBancariaAhorro
import json

def guardar_cuentas_json(gestion_cuentas, archivo_json):
    with open(archivo_json, 'w') as f:
        json.dump([cuenta.to_dict() for cuenta in gestion_cuentas.cuentas], f)

def cargar_cuentas_json(archivo_json):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
            return GestionCuentas.from_dict_list(data)
    except FileNotFoundError:
        return GestionCuentas()

def mostrar_menu():
    print("=== Sistema de Gestión de Cuentas Bancarias ===")
    print("1. Crear cuenta corriente")
    print("2. Crear cuenta de ahorro")
    print("3. Listar cuentas")
    print("4. Actualizar cuenta")
    print("5. Eliminar cuenta")
    print("6. Balance total de cuentas por tipo")
    print("7. Guardar y salir")

def ejecutar_opcion(opcion, gestion_cuentas):
    try:
        if opcion == '1':
            numero_cuenta = input("Número de cuenta: ")
            saldo = float(input("Saldo inicial: "))
            titular = input("Titular de la cuenta: ")
            gestion_cuentas.agregar_cuenta(CuentaBancariaCorrientes(numero_cuenta, saldo, titular))
        elif opcion == '2':
            numero_cuenta = input("Número de cuenta: ")
            saldo = float(input("Saldo inicial: "))
            titular = input("Titular de la cuenta: ")
            interes_anual = float(input("Interés anual (%): "))
            gestion_cuentas.agregar_cuenta(CuentaBancariaAhorro(numero_cuenta, saldo, titular, interes_anual))
        elif opcion == '3':
            gestion_cuentas.listar_cuentas()
        elif opcion == '4':
            numero_cuenta = input("Número de cuenta a actualizar: ")
            nuevo_saldo = input("Nuevo saldo (dejar en blanco para no cambiar): ")
            nuevo_titular = input("Nuevo titular (dejar en blanco para no cambiar): ")
            gestion_cuentas.actualizar_cuenta(numero_cuenta, nuevo_saldo, nuevo_titular)
        elif opcion == '5':
            numero_cuenta = input("Número de cuenta a eliminar: ")
            gestion_cuentas.eliminar_cuenta(numero_cuenta)
        elif opcion == '6':
            gestion_cuentas.balance_total_por_tipo()
        elif opcion == '7':
            guardar_cuentas_json(gestion_cuentas, 'data.json')
            print("Cuentas guardadas. Saliendo...")
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
    gestion_cuentas = cargar_cuentas_json('data.json')
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion, gestion_cuentas)
