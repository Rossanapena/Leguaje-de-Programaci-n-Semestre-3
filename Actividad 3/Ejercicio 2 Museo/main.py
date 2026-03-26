from usuarios import SistemaSeguridad
from obras import Cuadro, Escultura
from gestion_museo import GestionMuseo

def ejecutar_museo():
    # Inicialización del sistema
    seguridad = SistemaSeguridad()
    museo = GestionMuseo()

    # --- 1. SECCIÓN: ENCARGADO (Carga de datos) ---
    # Simulamos que el encargado entra al sistema
    user_encargado = seguridad.autenticar("ross_admin")
    if user_encargado and user_encargado.rol == "Encargado":
        print(f"✅ Sesión iniciada: {user_encargado.username} [{user_encargado.rol}]")
        
        obra1 = Cuadro("La persistencia de la memoria", "Dalí", "Surrealismo", 5000000.0, "1931", "Surrealismo", "Óleo")
        obra2 = Escultura("El Pensador", "Rodin", "Impresionismo", 3000000.0, "1904", "Modernismo", "Bronce")
        
        museo.agregar_obra(obra1)
        museo.agregar_obra(obra2)
        print("Obras cargadas exitosamente al catálogo.")

    # --- 2. SECCIÓN: RESTAURADOR JEFE (Gestión de mantenimiento) ---
    user_restaurador = seguridad.autenticar("jefe_restaura")
    if user_restaurador and user_restaurador.rol == "Restaurador":
        print(f"\n✅ Sesión iniciada: {user_restaurador.username} [{user_restaurador.rol}]")
        # El restaurador encuentra una obra dañada y la envía a reparar inmediatamente
        museo.enviar_a_restauracion(museo.obras[0], "Reparación de grietas en lienzo")
        # Consulta el historial de la obra
        museo.consultar_historial_obra(museo.obras[0])

    # --- 3. SECCIÓN: DIRECTOR (Finanzas y Cesiones) ---
    user_director = seguridad.autenticar("dir_museo")
    if user_director and user_director.rol == "Director":
        print(f"\n✅ Sesión iniciada: {user_director.username} [{user_director.rol}]")
        
        # Consulta el valor total de la colección
        total = museo.obtener_valoracion_total()
        print(f"💰 VALORACIÓN TOTAL DE LA COLECCIÓN: ${total:,.2f}")
        
        # Gestiona una cesión
        museo.ceder_obra(museo.obras[1], "Museo del Prado", 25000.0, 90)

    # --- 4. SECCIÓN: VISITANTE (Monitor de vestíbulo) ---
    user_visitante = seguridad.autenticar("monitor_vestibulo")
    if user_visitante and user_visitante.rol == "Visitante":
        # El monitor solo muestra obras en la sala 'Impresionismo' que estén 'Expuesta'
        museo.consultar_obras_por_sala("Impresionismo")

if __name__ == "__main__":
    ejecutar_museo()