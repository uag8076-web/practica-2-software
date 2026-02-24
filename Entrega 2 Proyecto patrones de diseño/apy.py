import json
from flask import Flask, request, jsonify

from Repositorio_unico_singleton import ProductoRepositorio
from Producto import Producto
from Pedido_builder import PedidoBuilder
from Exportar_decorator import ExportadorJSON, ExportadorTexto
from Descuentos_strategy import Normal, Premium, VIP
from Pedido_model import Pedido

app = Flask(__name__)
repo = ProductoRepositorio()


def cargar_datos_iniciales():
    try:
        with open("datos.json", encoding="utf-8") as f:
            data = json.load(f)

        # -------- PRODUCTO --------
        p = data.get("producto")

        if p:
            producto = Producto(
                p["id"],
                p["nombre"],
                p["precio"],
                p["categoria"]
            )
            repo.agregar_producto(producto)


        o = data.get("orden")

        if o:
            builder = PedidoBuilder(o["id"])

            for item in o["items"]:
                prod = repo.buscar_producto(item["product_id"])
                if prod:
                    builder.agregar_producto(prod, item["cantidad"])

            builder.set_cliente(o.get("cliente"))
            builder.set_tipo_cliente(o.get("tipo_cliente"))
            builder.set_metodo_pago(o.get("metodo_pago"))

            pedido = builder.build()
            repo.agregar_pedido(pedido)

        print("Productos guardados:", len(repo.obtener_productos()))
        print("Pedidos guardados:", len(repo.obtener_pedidos()))

    except Exception as e:
        print("Error cargando datos:", e)


cargar_datos_iniciales()


@app.get("/productos")
def listar_productos():
    return jsonify([p.to_dict() for p in repo.obtener_productos()])


@app.post("/productos")
def crear_producto():
    d = request.json

    p = Producto(
        d["id"],
        d["nombre"],
        d["precio"],
        d["categoria"]
    )

    repo.agregar_producto(p)
    return {"ok": True}


@app.post("/pedidos")
def crear_pedido():
    d = request.json

    builder = PedidoBuilder(d["id"])

    for item in d["items"]:
        prod = repo.buscar_producto(item["producto_id"])
        if prod:
            builder.agregar_producto(prod, item["cantidad"])

    builder.set_cliente(d.get("cliente"))
    builder.set_tipo_cliente(d.get("tipo_cliente"))
    builder.set_metodo_pago(d.get("metodo_pago"))

    pedido = builder.build()
    repo.agregar_pedido(pedido)

    return {"ok": True}


@app.get("/pedidos")
def listar_pedidos():
    return jsonify([p.to_dict() for p in repo.obtener_pedidos()])


@app.get("/pedidos/<id>")
def detalle(id):
    pedido = repo.obtener_pedido(id)
    if not pedido:
        return {"error": "no encontrado"}, 404
    return jsonify(pedido.to_dict())


@app.put("/pedidos/<id>/avanzar")
def avanzar(id):
    pedido = repo.obtener_pedido(id)
    if pedido:
        pedido.avanzar()
    return {"ok": True}


@app.put("/pedidos/<id>/cancelar")
def cancelar(id):
    pedido = repo.obtener_pedido(id)
    if pedido:
        pedido.cancelar()
    return {"ok": True}


@app.get("/pedidos/<id>/exportar")
def exportar(id):
    formato = request.args.get("formato", "json")
    pedido = repo.obtener_pedido(id)

    if not pedido:
        return {"error": "no encontrado"}, 404

    if formato == "texto":
        return ExportadorTexto().exportar(pedido)

    return ExportadorJSON().exportar(pedido)

@app.get("/debug/all")
def debug_all():
    return jsonify({
        "productos": [p.to_dict() for p in repo.obtener_productos()],
        "pedidos": [p.to_dict() for p in repo.obtener_pedidos()]
    })


if __name__ == "__main__":
    app.run(debug=True)