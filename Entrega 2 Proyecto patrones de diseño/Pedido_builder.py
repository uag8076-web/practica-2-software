from Pedido_model import Pedido

class PedidoBuilder:
    def __init__(self, id):
        self.pedido = Pedido(id)

    def agregar_producto(self, producto, cantidad):
        self.pedido.agregar_producto(producto, cantidad)
        return self

    def set_cliente(self, cliente):
        self.pedido.cliente = cliente
        return self

    def set_tipo_cliente(self, tipo):
        self.pedido.tipo_cliente = tipo
        return self

    def set_metodo_pago(self, metodo):
        self.pedido.metodo_pago = metodo
        return self

    def build(self):
        return self.pedido