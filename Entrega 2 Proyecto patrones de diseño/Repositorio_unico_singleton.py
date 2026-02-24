class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ProductoRepositorio(metaclass=SingletonMeta):

    def __init__(self):
        self.products = {}
        self.pedidos = {}

    def agregar_producto(self, producto):
        self.products[producto.id] = producto

    def buscar_producto(self, id):
        return self.products.get(id)

    def obtener_productos(self):
        return list(self.products.values())

    def agregar_pedido(self, pedido):
        self.pedidos[pedido.id] = pedido

    def buscar_pedido(self, id):
        return self.pedidos.get(id)

    def obtener_pedidos(self):
        return list(self.pedidos.values())

    def obtener_pedido(self, id):
        return self.pedidos.get(id)