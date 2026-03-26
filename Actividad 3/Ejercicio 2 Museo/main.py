class Producto:
    def __init__(self, codigo, descripcion, precio, cantidad):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Cod: {self.codigo} | {self.descripcion} | Precio: ${self.precio} | Stock: {self.cantidad}"

class SistemaTeleVentas:
    def __init__(self):
        # Simulamos la interacción con el sistema de inventario existente
        self.catalogo = [
            Producto("P001", "Televisor 4K", 1500, 10),
            Producto("P002", "Soporte Pared", 50, 25),
            Producto("P003", "Cable HDMI 2.1", 20, 50)
        ]

    def consultar_catalogo(self):
        print("\n--- Catálogo de Productos ---")
        for p in self.catalogo:
            print(p)

# Instancia inicial para prueba
if __name__ == "__main__":
    sistema = SistemaTeleVentas()
    sistema.consultar_catalogo()