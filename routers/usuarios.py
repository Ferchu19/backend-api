from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models import Usuario


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    edad: int
    activo: bool = True

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    edad: int | None = None
    activo: bool | None = None


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int
    activo: bool 

    class Config:
        from_attributes = True


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuario(db: Session =  Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    return usuario


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo =  Usuario(**usuario.model_dump())
    db.add(nuevo)
    try:
        db.commit()
        db.refresh(nuevo)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="El mail ya está registrado"
            )
    return nuevo

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="No existe el usuario"
        )
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado"}

@router.put("/{usuario_id}", response_model= UsuarioResponse)
def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario: 
        raise HTTPException(
            status_code= 404, 
            detail="Usuario no encontrado"
        )
    
     #Solo actualizamos los campos que llegaron con valor
    if datos.nombre is not None:
        usuario.nombre = datos.nombre
    if datos.email is not None:
        usuario.email = datos.email
    if datos.edad is not None:
        usuario.edad = datos.edad
    if datos.activo is not None:
        usuario.activo = datos.activo

    db.commit()
    db.refresh(usuario)
    return usuario