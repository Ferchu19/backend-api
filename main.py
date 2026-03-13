from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def inicio() -> dict:
    return {"mensaje": "Hola mundo desde FastAPI"}

@app.get("/saludo")
def saludo() -> dict:
    return {"mensaje": "Bienvenidos a mi API"}

@app.get("/version")
def version() -> dict:
    return {"version": "1.0.0", "autor": "Fernando"}

@app.get("/estado")
def estado() -> dict:
    return {"estado": "online", "activo": True}

@app.get("/productos/{producto_id}")
def productos(producto_id: int) -> dict:
    return {"producto_id": producto_id, "nombre": "camisa"}

@app.get("/buscar")
def buscar(termino: str, limite: int = 5) -> dict:
    return {"termino": termino, "limite": limite}

#@app.get("/usuarios/{usuario_id}/perfil")
#def usuarios(usuario_id: int, mostrar_email: bool = False) -> dict:
#    return {"usuario_id": usuario_id, "mostrar_id": mostrar_email}



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


@app.post("/usuarios")
def crear_usuarios(usuario: Usuario) -> dict:
    return {"mensaje": "Usuarion Creado", "datos": usuario.model_dump()}

@app.post("/tareas")
def tareas(tarea: Tarea) -> dict:
    return {"mensaje": "Tarea creada", "datos": tarea.model_dump()}

@app.get("/usuarios/{usuario_id}")
def  obtener_usuarios( usuario_id: int) -> dict:
    
    usuario = Usuario(nombre="nilo", email="elgato@miau.com", edad=4)
    return {"usuario_id": usuario_id, "datos": usuario.model_dump()}




