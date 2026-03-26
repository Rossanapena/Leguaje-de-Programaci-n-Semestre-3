from clases import Producto, OrdenCompra, List, Tuple, Optional

class SistemaTeleVentas:
    def __init__(self) -> None:
        # Simulación de inventario inicial
        self.catalogo: List[Producto] = [
            Producto("P001", "Televisor 4K", 1500.0, 10),
            Producto("P002", "Soporte Pared", 50.0, 25)
        ]
        self.ordenes_confirmadas: List[OrdenCompra] = []

    def ingresar_orden(self, cliente_id: str, lista_pedidos: List[Tuple[str, int]]) -> None:
        productos_finales: List[Tuple[Producto, int]] = []
        
        for cod, cant in lista_pedidos:
            prod = next((p for p in self.catalogo if p.codigo == cod), None)
            if prod and prod.cantidad >= cant:
                prod.cantidad -= cant  # Actualizamos disponibilidad (Inventario)
                productos_finales.append((prod, cant))
        
        if productos_finales:
            nueva_orden = OrdenCompra(cliente_id, productos_finales)
            self.ordenes_confirmadas.append(nueva_orden)
            print(f"✅ Orden procesada para: {cliente_id}")

    def presentar_queja(self, cliente_id: str, motivo: str) -> None:
        print(f"📩 GERENCIA: Queja recibida de {cliente_id}: {motivo}")

if __name__ == "__main__":
    app = SistemaTeleVentas()
    app.ingresar_orden("User_Ross", [("P001", 1)])
    app.presentar_queja("User_Ross", "El empaque llegó un poco abollado.")