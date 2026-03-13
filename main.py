from fastapi import FastAPI
from routers import productos, usuarios

app = FastAPI()

app.include_router(productos.router)
app.include_router(usuarios.router)




