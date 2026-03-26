import uuid
from typing import List, Tuple

class Producto:
    def __init__(self, codigo: str, descripcion: str, precio: float, cantidad: int):
        self.codigo: str = codigo
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.cantidad: int = cantidad

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.descripcion} - stock: {self.cantidad}"

class OrdenCompra:
    def __init__(self, cliente_id: str, productos: List[Tuple[Producto, int]]):
        self.id: str = str(uuid.uuid4())[:8] # ID corto de 8 caracteres
        self.cliente_id: str = cliente_id
        self.productos: List[Tuple[Producto, int]] = productos
        self.estado: str = "Confirmada"

class Envio:
    def __init__(self, orden: OrdenCompra, transporte: str):
        self.orden: OrdenCompra = orden
        self.transporte: str = transporte
        self.estado: str = "En camino"

    def __str__(self) -> str:
        return f"Envío de orden {self.orden.id} vía {self.transporte} ({self.estado})"