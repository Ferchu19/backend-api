from fastapi.testclient import TestClient
from main import app

#TestClient simula request HTTP a la app sin necesitar un servidor corriendo 
client = TestClient(app)

def test_listar_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_producto():
    response = client.post("/productos/", json={
        "nombre": "Remera test",
        "precio": 25.0
    })
    assert response.status_code == 201
    assert response.json()["nombre"] == "Remera test"

def test_producto_no_existe():
    response = client.get("/productos/9999")
    assert response.status_code == 404

def test_crear_producto_sin_precio():
    response = client.post("/productos/", json={
        "nombre": "Remera sin precio"
    })
    assert response.status_code == 422 #error de validacion Pydantic

def test_eliminar_producto():

    #Primero crear el producto
    response_crear = client.post("/productos/", json={
        "nombre": "Producto a eliminar",
        "precio": 12
    })
    producto_id = response_crear.json()["id"]

    #Luego lo eliminamos con su id real
    response = client.delete(f"/productos/{producto_id}")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto eliminado"


