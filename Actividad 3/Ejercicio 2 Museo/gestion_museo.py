from datetime import datetime
from typing import List, Dict, Any
from obras import ObraArte

class GestionMuseo:
    def __init__(self) -> None:
        self.obras: List[ObraArte] = []
        self.museos_colaboradores: List[str] = ["Museo del Prado", "Louvre", "MET"]
        # Cola de espera: { 'titulo_obra': ['Museo B', 'Museo C'] }
        self.cola_espera_cesiones: Dict[str, List[str]] = {}

    def agregar_obra(self, obra: ObraArte) -> None:
        self.obras.append(obra)

    def enviar_a_restauracion(self, obra: ObraArte, tipo: str) -> None:
        obra.estado = "Restauración"
        # Tipamos el diccionario explícitamente para evitar el error de Pylance
        registro: Dict[str, Any] = {
            "tipo": tipo,
            "inicio": datetime.now(),
            "fin": None
        }
        obra.historial_restauraciones.append(registro)
        print(f"🛠️ Obra '{obra.titulo}' enviada a restauración ({tipo}).")

    # --- Requerimiento: Gestión de Cesiones y Colas ---
    def ceder_obra(self, obra: ObraArte, museo_destino: str, importe: float, dias: int) -> None:
        if obra.estado == "Cedida":
            if obra.titulo not in self.cola_espera_cesiones:
                self.cola_espera_cesiones[obra.titulo] = []
            self.cola_espera_cesiones[obra.titulo].append(museo_destino)
            print(f"⏳ La obra '{obra.titulo}' ya está cedida. {museo_destino} añadido a lista de espera.")
        else:
            obra.estado = "Cedida"
            print(f"🏛️ Obra '{obra.titulo}' cedida a {museo_destino} por ${importe} ({dias} días).")

    # --- Requerimiento: Consulta Restaurador Jefe (Ordenada) ---
    def consultar_historial_obra(self, obra: ObraArte) -> None:
        print(f"\n📜 Historial de restauraciones de: {obra.titulo}")
        # Ordenamos por la fecha de inicio (antigüedad)
        historial_ordenado = sorted(obra.historial_restauraciones, key=lambda x: x['inicio'])
        for res in historial_ordenado:
            estado_fin = res['fin'] if res['fin'] else "En curso"
            print(f"   - {res['tipo']} | Inicio: {res['inicio'].strftime('%Y-%m-%d')} | Fin: {estado_fin}")

    def obtener_valoracion_total(self) -> float:
        return sum(obra.valor for obra in self.obras)
    
    def consultar_obras_por_sala(self, sala: str) -> None:
        print(f"\n🖥️ MONITOR VESTÍBULO - SALA: {sala}")
        # Simulamos que filtramos por sala (usando el periodo como sala)
        obras_sala = [o for o in self.obras if o.periodo == sala and o.estado == "Expuesta"]
        if obras_sala:
            for o in obras_sala:
                print(f"🖼️ {o.titulo} - Autor: {o.autor}")
        else:
            print("No hay obras expuestas en esta sala actualmente.")