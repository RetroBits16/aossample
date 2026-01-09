# 🛒 Sistema de Gestión de Supermercado

Sistema completo de gestión de productos para supermercado con backend FastAPI y frontend HTML/CSS/JS.

## 📋 Características

- ✅ Gestión completa de productos (Crear, Leer, Actualizar, Eliminar)
- ✅ Base de datos SQLite con 20 productos de ejemplo
- ✅ Categorías y descripciones de productos
- ✅ Interfaz web moderna y responsiva
- ✅ Operaciones adicionales (sumar, concatenar, longitud)
- ✅ Sistema de notificaciones
- ✅ Indicador de stock bajo

## 📁 Estructura del Proyecto

```
supermercado_app/
├── app/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py                    # Lógica de base de datos
│   │   └── supermercado.db          # Base de datos SQLite (se crea automáticamente)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py               # Modelo de producto
│   │   └── item.py                  # Modelo de item
│   └── routes/
│       ├── __init__.py
│       ├── product_routes.py        # Rutas de productos
│       └── sample.py                # Rutas de operaciones sample
├── frontend/
│   ├── index.html                   # Interfaz web
│   ├── styles.css                   # Estilos
│   └── script.js                    # Lógica frontend
├── main.py                          # Punto de entrada de la aplicación
├── requirements.txt                 # Dependencias
└── README.md                        # Este archivo
```

## 🚀 Instalación y Ejecución

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Ejecutar el servidor backend

```bash
python main.py
```

El servidor se iniciará en `http://127.0.0.1:8000`

La base de datos se creará automáticamente con 20 productos de ejemplo en el primer inicio.

### Paso 3: Abrir el frontend

Abre el archivo `frontend/index.html` en tu navegador web.

También puedes usar un servidor local:

```bash
# Con Python 3
cd frontend
python -m http.server 8080
```

Luego abre: `http://localhost:8080`

## 📊 Productos de Ejemplo

La base de datos incluye 20 productos de supermercado:

- Lácteos (Leche, Yogures)
- Bebidas (Coca-Cola, Agua, Cerveza, Zumos)
- Conservas (Tomate, Atún)
- Panadería (Pan de Molde)
- Frutas y Verduras (Tomates, Plátanos)
- Y más...

## 🔌 API Endpoints

### Productos

- `GET /products` - Obtener todos los productos
- `GET /products/{id}` - Obtener un producto específico
- `POST /products` - Crear un nuevo producto
- `PUT /products/{id}` - Actualizar un producto
- `DELETE /products/{id}` - Eliminar un producto

### Operaciones

- `POST /process` - Sumar dos valores
- `GET /concat?param1=X&param2=Y` - Concatenar dos strings
- `GET /length?string=X` - Calcular longitud de string

## 📖 Uso de la Aplicación

### Agregar Producto

1. Ve a la pestaña "Productos"
2. Rellena el formulario con:
   - Nombre del producto
   - Precio
   - Stock
   - Categoría (opcional)
   - Descripción (opcional)
3. Haz clic en "Agregar Producto"

### Ver Productos

- Los productos se cargan automáticamente al abrir la página
- Haz clic en "🔄 Actualizar" para recargar la lista

### Eliminar Producto

- Haz clic en el botón "🗑️ Eliminar" en la tarjeta del producto
- Confirma la eliminación

### Operaciones

Ve a la pestaña "Operaciones" para probar las funciones de ejemplo:
- Sumar valores
- Concatenar textos
- Calcular longitud de texto

## 🛠️ Tecnologías

**Backend:**
- FastAPI
- SQLite3
- Pydantic
- Uvicorn

**Frontend:**
- HTML5
- CSS3 (con gradientes y animaciones)
- JavaScript (Vanilla)
- Fetch API

## 🎨 Características de la Interfaz

- ✨ Diseño moderno con gradientes morados
- 📱 Totalmente responsivo
- 🔔 Sistema de notificaciones en tiempo real
- 🎯 Indicadores visuales de stock bajo
- 🏷️ Categorías con colores
- ⚡ Animaciones suaves

## 🔧 Configuración

Para cambiar el puerto del backend, edita `main.py`:

```python
uvicorn.run(app, host="127.0.0.1", port=8000)  # Cambia el puerto aquí
```

Para cambiar la URL del backend en el frontend, edita `frontend/script.js`:

```javascript
const API_BASE_URL = 'http://127.0.0.1:8000';  // Cambia aquí
```

## 📝 Notas

- La base de datos SQLite se crea automáticamente al iniciar el servidor por primera vez
- Los productos de ejemplo solo se insertan si la base de datos está vacía
- CORS está habilitado para permitir peticiones desde cualquier origen (para desarrollo)

## 🐛 Solución de Problemas

**Error de conexión en el frontend:**
- Asegúrate de que el backend está ejecutándose
- Verifica que la URL en `script.js` sea correcta

**Error al instalar dependencias:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**La base de datos no se crea:**
- Verifica que tengas permisos de escritura en la carpeta
- Ejecuta el servidor al menos una vez para inicializar la BD

## 👨‍💻 Desarrollo

Para añadir más productos de ejemplo, edita el archivo `app/database/db.py` en la función `init_db()`.

Para añadir nuevas rutas de API, crea nuevos routers en `app/routes/`.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

---

Desarrollado para la gestión eficiente de inventario de supermercados 🛒
