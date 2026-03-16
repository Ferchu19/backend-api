import bcrypt
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

#Clave secreta
SECRET_KEY = "clave-secreta-super-segura-cambiar-en-produccion"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def hashear_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode("utf-8")

def verificar_password(password: str, hash: str) -> bool:
    password_bytes = password.encode("utf-8")
    hash_bytes  = hash.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hash_bytes)

def crear_token(data: dict) -> str:
    datos = data.copy()
    expira = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    datos.update({"exp": expira})
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
