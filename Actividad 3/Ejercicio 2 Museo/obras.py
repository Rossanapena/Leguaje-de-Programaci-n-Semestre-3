from datetime import datetime
from typing import List, Dict, Any

class ObraArte:
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str):
        self.titulo: str = titulo
        self.autor: str = autor
        self.periodo: str = periodo
        self.valor: float = valor
        self.fecha_entrada: datetime = datetime.now()
        self.fecha_creacion: str = fecha_creacion
        self.estado: str = "Expuesta"
        
        self.historial_restauraciones: List[Dict[str, Any]] = []

class Cuadro(ObraArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, tecnica: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo: str = estilo
        self.tecnica: str = tecnica

class Escultura(ObraArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, material: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo: str = estilo
        self.material: str = material