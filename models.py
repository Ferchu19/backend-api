from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


# models.py — le dice a la BD cómo es la tabla

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable= False)
    email = Column(String, nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)