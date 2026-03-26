class OrdenCompra:
    def __init__(self, cliente_id, productos, tipo_pago="Tarjeta de Crédito"):
        self.cliente_id = cliente_id
        self.productos = productos  # Lista de tuplas (Producto, cantidad)
        self.tipo_pago = tipo_pago
        self.estado = "Confirmada"

    def __str__(self):
        detalle = ", ".join([f"{p.descripcion} x{c}" for p, c in self.productos])
        return f"Orden Cliente: {self.cliente_id} | Pago: {self.tipo_pago} | Productos: [{detalle}]"

# --- Nueva lógica en la clase principal ---
class SistemaTeleVentas:
    def __init__(self):
        self.catalogo = [
            Producto("P001", "Televisor 4K", 1500, 10),
            Producto("P002", "Soporte Pared", 50, 25)
        ]
        self.ordenes_confirmadas = []

    def consultar_catalogo(self):
        for p in self.catalogo: print(p)

    def ingresar_orden(self, cliente_id, lista_pedidos):
        # lista_pedidos es una lista de (codigo_prod, cantidad)
        productos_finales = []
        for cod, cant in lista_pedidos:
            prod = next((p for p in self.catalogo if p.codigo == cod), None)
            if prod and prod.cantidad >= cant:
                productos_finales.append((prod, cant))
        
        nueva_orden = OrdenCompra(cliente_id, productos_finales)
        self.ordenes_confirmadas.append(nueva_orden)
        print(f"✅ Orden ingresada con éxito: {nueva_orden}")

    def presentar_queja(self, cliente_id, motivo):
        print(f"📩 REENVÍO INMEDIATO AL GERENTE: El cliente {cliente_id} reporta: '{motivo}'")

# --- Bloque de prueba ---
if __name__ == "__main__":
    sistema = SistemaTeleVentas()
    # 1. Cliente consulta y compra
    sistema.ingresar_orden("Cliente_01", [("P001", 1), ("P002", 2)])
    # 2. Cliente pone una queja
    sistema.presentar_queja("Cliente_01", "Demora en la entrega del pedido P001")