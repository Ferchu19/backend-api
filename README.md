# backend-api

API REST construida con FastAPI como proyecto de aprendizaje. Incluye autenticación JWT, base de datos con SQLAlchemy, migraciones con Alembic y tests con pytest.

## Tecnologías

- Python 3.14
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy + SQLite
- Alembic
- bcrypt
- python-jose
- pytest
- Docker

## Instalación

### Opción 1 — Local

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

4. Aplicar migraciones
```bash
alembic upgrade head
```

5. Correr el servidor
```bash
uvicorn main:app --reload
```

### Opción 2 — Docker

```bash
docker build -t backend-api .
docker run -p 8000:8000 backend-api
```

## Documentación

Una vez corriendo, accedé a la documentación interactiva en:
- Swagger UI: http://127.0.0.1:8000/docs

## Tests

```bash
pytest -v
```

## Endpoints

### Auth
| Método | Ruta | Descripción | Protegida |
|--------|------|-------------|-----------|
| POST | /auth/login | Login y obtención de token JWT | No |

### Productos
| Método | Ruta | Descripción | Protegida |
|--------|------|-------------|-----------|
| GET | /productos | Listar todos los productos | No |
| GET | /productos/{id} | Obtener un producto | No |
| POST | /productos | Crear un producto | No |
| PUT | /productos/{id} | Actualizar un producto | No |
| DELETE | /productos/{id} | Eliminar un producto | No |

### Usuarios
| Método | Ruta | Descripción | Protegida |
|--------|------|-------------|-----------|
| GET | /usuarios | Listar todos los usuarios | No |
| GET | /usuarios/me | Obtener perfil propio | ✅ Sí |
| GET | /usuarios/{id} | Obtener un usuario | No |
| POST | /usuarios | Crear un usuario | No |
| PUT | /usuarios/{id} | Actualizar un usuario | No |
| DELETE | /usuarios/{id} | Eliminar un usuario | ✅ Sí |

## Estructura del proyecto

```
backend-api/
├── routers/
│   ├── auth.py
│   ├── productos.py
│   └── usuarios.py
├── tests/
│   └── test_productos.py
├── alembic/
├── main.py
├── database.py
├── models.py
├── security.py
├── Dockerfile
├── requirements.txt
└── README.md
```