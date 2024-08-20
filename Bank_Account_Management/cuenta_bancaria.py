class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, titular):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.titular = titular

    def to_dict(self):
        return {
            "numero_cuenta": self.numero_cuenta,
            "saldo": self.saldo,
            "titular": self.titular
        }

class CuentaBancariaCorrientes(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular):
        super().__init__(numero_cuenta, saldo, titular)

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["tipo"] = "corriente"
        return base_dict

class CuentaBancariaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular, interes_anual):
        super().__init__(numero_cuenta, saldo, titular)
        self.interes_anual = interes_anual

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["interes_anual"] = self.interes_anual
        base_dict["tipo"] = "ahorro"
        return base_dict
