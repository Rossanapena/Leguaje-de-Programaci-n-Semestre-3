from datetime import datetime
from typing import List

class ObraArte:
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str):
        self.titulo = titulo
        self.autor = autor
        self.periodo = periodo
        self.valor = valor
        self.fecha_entrada = datetime.now()
        self.fecha_creacion = fecha_creacion
        self.estado = "Expuesta"
        self.historial_restauraciones: List[dict] = []

class Cuadro(ObraArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, tecnica: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo = estilo
        self.tecnica = tecnica

class Escultura(ObraArte):
    def __init__(self, titulo: str, autor: str, periodo: str, valor: float, fecha_creacion: str, estilo: str, material: str):
        super().__init__(titulo, autor, periodo, valor, fecha_creacion)
        self.estilo = estilo
        self.material = material