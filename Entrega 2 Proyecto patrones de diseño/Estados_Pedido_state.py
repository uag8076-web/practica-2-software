class EstadoPedido:
    nombre = "BASE"

    def avanzar(self, pedido):
        pass

class Pendiente(EstadoPedido):
    nombre = "PENDIENTE"

    def avanzar(self, pedido):
        pedido.estado = Procesando()

class Procesando(EstadoPedido):
    nombre = "PROCESANDO"

    def avanzar(self, pedido):
        pedido.estado = Enviado()

class Enviado(EstadoPedido):
    nombre = "ENVIADO"

    def avanzar(self, pedido):
        pedido.estado = Entregado()

class Entregado(EstadoPedido):
    nombre = "ENTREGADO"