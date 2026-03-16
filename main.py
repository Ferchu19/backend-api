from fastapi import FastAPI
from routers import productos, usuarios, auth
from database import engine, Base

#Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(productos.router)
app.include_router(usuarios.router)
app.include_router(auth.router)



