class Observer:
    def update(self, pedido):
        pass

class LoggerObserver(Observer):
    def update(self, pedido):
        print(f"Pedido {pedido.id} cambió a {pedido.estado.nombre}")