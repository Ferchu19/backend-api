from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

productos_db = [
    {"id": 1, "nombre": "remera", "precio": 12.2},
    {"id": 2, "nombre": "short", "precio": 3.45},
    {"id": 3, "nombre": "medias", "precio": 1.45}
]

class Producto(BaseModel):
    nombre: str
    precio: float

@app.get("/productos")
def mostrar_productos() -> list:
    return productos_db

@app.get("/productos/{producto_id}")
def buscar_producto(producto_id: int) -> dict:
    producto = next((u for u in productos_db if u["id"] == producto_id), None)

    if producto is None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    
    return producto

@app.post("/productos", status_code=201)
def crear_producto(producto: Producto) -> dict:
    nuevo_product = {"id": len(productos_db) + 1, **producto.model_dump()}
    productos_db.append(nuevo_product)
    return {"mensaje": "producto creado", "datos": nuevo_product}  

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int) -> dict:
    
    for i, p in enumerate(productos_db):
        if p["id"] == producto_id:
            productos_db.pop(i)
            return {"mensaje": "producto eliminado"}


    raise HTTPException(
        status_code=404,
        detail="No existe el producto"
    )


