from clases import Producto, OrdenCompra, Envio, List, Tuple

class SistemaTeleVentas:
    def __init__(self) -> None:
        self.catalogo: List[Producto] = [
            Producto("P001", "Televisor 4K", 1500.0, 10),
            Producto("P002", "Soporte Pared", 50.0, 25)
        ]
        self.ordenes_confirmadas: List[OrdenCompra] = []
        self.envios_realizados: List[Envio] = []

    # --- Lógica de Cliente ---
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
            print(f"✅ Orden {cliente_id} guardada en depósito.")

    # --- Lógica de Agente de Depósito (Logística) ---
    def procesar_logistica(self) -> None:
        print("\n--- SECCIÓN DEPÓSITO: Procesando pedidos ---")
        for orden in self.ordenes_confirmadas:
            # El agente selecciona transporte según disponibilidad
            empresa_transporte = "Servientrega" if "P001" in [p[0].codigo for p in orden.productos] else "Mensajería Local"
            
            nuevo_envio = Envio(orden, empresa_transporte)
            self.envios_realizados.append(nuevo_envio)
            print(f"📦 Pedido empaquetado: {nuevo_envio}")
        
        # Limpiamos las órdenes ya procesadas
        self.ordenes_confirmadas.clear()

if __name__ == "__main__":
    app = SistemaTeleVentas()
    # 1. Se genera la orden
    app.ingresar_orden("Ross_Pena", [("P001", 1)])
    # 2. El agente de depósito la procesa
    app.procesar_logistica()