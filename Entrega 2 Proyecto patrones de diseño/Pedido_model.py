from Estados_Pedido_state import Pendiente
from notificaciones_observer import LoggerObserver
from Descuentos_strategy import Normal, Premium, VIP
from datetime import datetime


class Pedido:
    def __init__(self, id):
        self.id = id
        self.productos = []  # lista de (producto, cantidad)
        self.estado = Pendiente()
        self.tipo_cliente = "normal"
        self.observers = [LoggerObserver()]
        self.cliente = None
        self.metodo_pago = None
        self.creado_en = datetime.now().isoformat()

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def avanzar(self):
        self.estado.avanzar(self)
        self.notificar()

    def cancelar(self):
        if self.estado.nombre == "PENDIENTE":
            self.estado.nombre = "CANCELADO"

    # ---- CALCULOS ----

    def calcular_subtotal(self):
        return sum(p.precio * c for p, c in self.productos)

    def calcular_total(self):
        subtotal = self.calcular_subtotal()

        strategy = {
            "normal": Normal(),
            "premium": Premium(),
            "vip": VIP()
        }.get(self.tipo_cliente, Normal())

        return strategy.aplicar(subtotal)

    def calcular_descuento(self):
        return self.calcular_subtotal() - self.calcular_total()

    # ---- OBSERVER ----

    def notificar(self):
        for o in self.observers:
            o.update(self)

    # ---- SERIALIZAR ----

    def to_dict(self):
        subtotal = self.calcular_subtotal()
        total = self.calcular_total()
        descuento = subtotal - total

        return {
            "id": self.id,
            "cliente": self.cliente,
            "tipo_cliente": self.tipo_cliente,
            "estado": self.estado.nombre,
            "items": [
                {
                    "producto_id": p.id,
                    "nombre_producto": p.nombre,
                    "cantidad": c,
                    "precio_unitario": p.precio
                }
                for p, c in self.productos
            ],
            "subtotal": subtotal,
            "descuento": descuento,
            "total": total,
            "metodo_pago": self.metodo_pago,
            "creado_en": self.creado_en
        }