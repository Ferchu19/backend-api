from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
from security import verificar_password, crear_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model= TokenResponse)
def login(datos: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    #1- Buscar el usuarion por Email
    usuario = db.query(Usuario).filter(Usuario.email == datos.username).first()

    #2- Verifica que existe y que el password es correcto
    if not usuario or not verificar_password(datos.password, usuario.password):
        raise HTTPException(
            status_code=401, 
            detail="Credenciales incorrectas"
        )
    
    #3- Crear y devolver el token 
    token = crear_token({"sub": usuario.email, "id": usuario.id})
    return {"access_token": token}
