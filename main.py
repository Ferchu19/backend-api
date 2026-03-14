from fastapi import FastAPI
from routers import productos, usuarios
from database import engine, Base

#Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(productos.router)
app.include_router(usuarios.router)




