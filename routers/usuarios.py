from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    activo: bool = True


class Tarea(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool = False
    prioridad: int = 1


@router.post("/")
def crear_usuarios(usuario: Usuario) -> dict:
    return {"mensaje": "Usuario Creado", "datos": usuario.model_dump()}

@router.post("/tareas")
def tareas(tarea: Tarea) -> dict:
    return {"mensaje": "Tarea creada", "datos": tarea.model_dump()}

@router.get("/{usuario_id}")
def  obtener_usuarios( usuario_id: int) -> dict:
    
    usuario = Usuario(nombre="nilo", email="elgato@miau.com", edad=4)
    return {"usuario_id": usuario_id, "datos": usuario.model_dump()}