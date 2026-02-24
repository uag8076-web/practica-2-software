class Producto:
    def __init__(self, id, nombre, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }