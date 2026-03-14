from sqlalchemy import Column, Integer, String, Float
from database import Base


# models.py — le dice a la BD cómo es la tabla
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)