from typing import Optional

class Usuario:
    def __init__(self, username: str, rol: str):
        self.username = username
        self.rol = rol

class SistemaSeguridad:
    def __init__(self):
        self.usuarios = {
            "ross_admin": Usuario("ross_admin", "Encargado"),
            "jefe_restaura": Usuario("jefe_restaura", "Restaurador"),
            "dir_museo": Usuario("dir_museo", "Director"),
            "monitor_vestibulo": Usuario("monitor_vestibulo", "Visitante")
        }

    def autenticar(self, username: str) -> Optional[Usuario]:
        return self.usuarios.get(username)