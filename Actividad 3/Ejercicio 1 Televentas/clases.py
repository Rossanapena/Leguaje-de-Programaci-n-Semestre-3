from typing import List, Tuple, Optional

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo: str = codigo
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.cantidad: int = cantidad

    def __str__(self) -> str:
        return f"Cod: {self.codigo} | {self.descripcion} | ${self.precio} | Stock: {self.cantidad}"

class OrdenCompra:
    def __init__(self, cliente_id: str, productos: List[Tuple[Producto, int]], tipo_pago: str = "Tarjeta de Crédito"):
        self.cliente_id: str = cliente_id
        self.productos: List[Tuple[Producto, int]] = productos
        self.tipo_pago: str = tipo_pago
        self.estado: str = "Confirmada"

    def __str__(self) -> str:
        detalle = ", ".join([f"{p.descripcion} x{c}" for p, c in self.productos])
        return f"Orden Cliente: {self.cliente_id} | Productos: [{detalle}]"