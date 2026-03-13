#backend-api

API REST construida con FastAPI como proyecto de aprendizaje.

##Tecnologías
- Python
- FastAPI
- Pydantic
- Uvicorn

##Instalación
# backend-api

API REST construida con FastAPI como proyecto de aprendizaje.

## Tecnologías
- Python
- FastAPI
- Pydantic
- Uvicorn

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/Ferchu19/backend-api.git
cd backend-api
```

2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Correr el servidor
```bash
uvicorn main:app --reload
```

## Documentación
Una vez corriendo, accedé a la documentación interactiva en:
- Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

### Productos
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /productos | Listar todos los productos |
| GET | /productos/{id} | Obtener un producto |
| POST | /productos | Crear un producto |
| DELETE | /productos/{id} | Eliminar un producto |

### Usuarios
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /usuarios/{id} | Obtener un usuario |
| POST | /usuarios | Crear un usuario |

1. Clonar el repositorio
```bash
git clone https://github.com/Ferchu19/backend-api.git
cd backend-api
```

2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Correr el servidor
```bash
uvicorn main:app --reload
```

## Documentación
Una vez corriendo, accedé a la documentación interactiva en:
- Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

### Productos
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /productos | Listar todos los productos |
| GET | /productos/{id} | Obtener un producto |
| POST | /productos | Crear un producto |
| DELETE | /productos/{id} | Eliminar un producto |

### Usuarios
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /usuarios/{id} | Obtener un usuario |
| POST | /usuarios | Crear un usuario |
