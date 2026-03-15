from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Producto


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


# Lo que recibe el cliente al crear
class ProductoCreate(BaseModel):
    nombre: str
    precio: float

# Lo que recibe el cliente al modificar un producto
class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = None

# Lo que devuelve la API (incluye el id)
class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float

    class Config:
        from_attributes = True ## permite convertir objetos SQLAlchemy a JSON

# GET todos
@router.get("/", response_model=list[ProductoResponse])
def mostrar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

# GET uno
@router.get("/{producto_id}", response_model=ProductoResponse)
def buscar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if producto is None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    
    return producto

# POST crear
@router.post("/", response_model=ProductoResponse, status_code=201)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_product = Producto(**producto.model_dump())
    db.add(nuevo_product)
    db.commit()
    db.refresh(nuevo_product)

    return nuevo_product 

# DELETE
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="No existe el producto"
        )

    db.delete(producto)
    db.commit()
    return {"mensaje": "Producto eliminado"}

@router.put("/{producto_id}", response_model= ProductoResponse)
def actualizar_producto(producto_id: int, datos: ProductoUpdate, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(
            status_code= 404, 
            detail="Producto no encontrado"
        )

    #Solo actualizamos los campos que llegaron con valor
    if datos.nombre is not None:
        producto.nombre = datos.nombre
    if datos.precio is not None:
        producto.precio = datos.precio

    db.commit()
    db.refresh(producto)
    return producto