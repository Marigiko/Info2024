from cuenta_bancaria import CuentaBancaria, CuentaBancariaCorrientes, CuentaBancariaAhorro

class GestionCuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, numero_cuenta):
        self.cuentas = [c for c in self.cuentas if c.numero_cuenta != numero_cuenta]

    def listar_cuentas(self):
        for c in self.cuentas:
            print(c.to_dict())

    def actualizar_cuenta(self, numero_cuenta, nuevo_saldo=None, nuevo_titular=None):
        for c in self.cuentas:
            if c.numero_cuenta == numero_cuenta:
                if nuevo_saldo is not None:
                    c.saldo = float(nuevo_saldo)
                if nuevo_titular:
                    c.titular = nuevo_titular
                    
    def balance_total_por_tipo(self):
        saldo_corriente = 0
        saldo_ahorro = 0
        for c in self.cuentas:
            if isinstance(c, CuentaBancariaCorrientes):
                saldo_corriente += c.saldo
            elif isinstance(c, CuentaBancariaAhorro):
                saldo_ahorro += c.saldo
        print(f"Saldo Total en Cuentas Corrientes: {saldo_corriente}")
        print(f"Saldo Total en Cuentas de Ahorro: {saldo_ahorro}")

    @classmethod
    def from_dict_list(cls, data_list):
        gestion_cuentas = cls()
        for data in data_list:
            if data.get("tipo") == "ahorro":
                cuenta = CuentaBancariaAhorro(
                    numero_cuenta=data["numero_cuenta"],
                    saldo=data["saldo"],
                    titular=data["titular"],
                    interes_anual=data["interes_anual"]
                )
            else:
                cuenta = CuentaBancariaCorrientes(
                    numero_cuenta=data["numero_cuenta"],
                    saldo=data["saldo"],
                    titular=data["titular"]
                )
            gestion_cuentas.agregar_cuenta(cuenta)
        return gestion_cuentas
