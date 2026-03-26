from clases import Producto, OrdenCompra, Envio, List, Tuple

class SistemaTeleVentas:
    def __init__(self) -> None:
        self.catalogo: List[Producto] = [
            Producto("P001", "Televisor 4K", 1500.0, 10),
            Producto("P002", "Soporte Pared", 50.0, 25),
            Producto("P003", "Control Remoto", 30.0, 40)
        ]
        self.ordenes_confirmadas: List[OrdenCompra] = []
        self.envios_realizados: List[Envio] = []

    # --- Requerimiento: Consultar y Enviar Catálogo ---
    def enviar_catalogo_correo(self, email_cliente: str) -> None:
        print(f"📧 Catálogo enviado con éxito a: {email_cliente}")

    # --- Requerimiento: Cancelar Orden ---
    def cancelar_orden(self, orden_id: str) -> None:
        orden = next((o for o in self.ordenes_confirmadas if o.id == orden_id), None)
        if orden:
            # Devolvemos el stock al inventario
            for prod, cant in orden.productos:
                prod.cantidad += cant
            self.ordenes_confirmadas.remove(orden)
            print(f"❌ Orden {orden_id} ha sido cancelada y el stock restaurado.")

    def ingresar_orden(self, cliente_id: str, lista_pedidos: List[Tuple[str, int]]) -> None:
        productos_finales: List[Tuple[Producto, int]] = []
        for cod, cant in lista_pedidos:
            prod = next((p for p in self.catalogo if p.codigo == cod), None)
            if prod and prod.cantidad >= cant:
                prod.cantidad -= cant 
                productos_finales.append((prod, cant))
        
        if productos_finales:
            nueva_orden = OrdenCompra(cliente_id, productos_finales)
            self.ordenes_confirmadas.append(nueva_orden)
            print(f"✅ Orden {nueva_orden.id} para {cliente_id} guardada.")

    def presentar_queja(self, cliente_id: str, motivo: str) -> None:
        # El sistema remite inmediatamente al gerente
        print(f"🚨 ALERTA GERENTE: Queja de {cliente_id} por '{motivo}'")

    def procesar_logistica(self) -> None:
        print("\n--- SECCIÓN DEPÓSITO ---")
        for orden in self.ordenes_confirmadas:
            empresa = "Servientrega" if any(p[0].precio > 1000 for p in orden.productos) else "Local Express"
            nuevo_envio = Envio(orden, empresa)
            self.envios_realizados.append(nuevo_envio)
            print(f"📦 {nuevo_envio}")
        self.ordenes_confirmadas.clear()

if __name__ == "__main__":
    app = SistemaTeleVentas()
    app.enviar_catalogo_correo("rossana@mail.com")
    app.ingresar_orden("Ross_Pena", [("P002", 2)])
    app.presentar_queja("Ross_Pena", "El sistema de pago demoró en cargar.")
    app.procesar_logistica()