import json

class Exportador:
    def exportar(self, pedido):
        pass

class ExportadorJSON(Exportador):
    def exportar(self, pedido):
        return json.dumps(pedido.to_dict())

class ExportadorTexto(Exportador):
    def exportar(self, pedido):
        return str(pedido.to_dict())