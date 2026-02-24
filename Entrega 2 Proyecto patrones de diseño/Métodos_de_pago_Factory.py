
class Pago:
    def pagar(self, monto):
        return f"Pagado {monto}"

class Tarjeta(Pago):
    pass

class Paypal(Pago):
    pass

class Transferencia(Pago):
    pass

class PagoFactory:
    @staticmethod
    def crear(tipo):
        if tipo == "tarjeta":
            return Tarjeta()
        if tipo == "paypal":
            return Paypal()
        if tipo == "transferencia":
            return Transferencia()