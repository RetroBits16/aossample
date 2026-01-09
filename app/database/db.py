import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "supermercado.db")

def get_connection():
    """Obtiene una conexión a la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa la base de datos con la tabla de productos y datos de ejemplo"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Crear tabla de productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            category TEXT,
            description TEXT
        )
    ''')
    
    # Verificar si ya hay datos
    cursor.execute('SELECT COUNT(*) FROM products')
    count = cursor.fetchone()[0]
    
    # Si no hay datos, insertar productos de ejemplo
    if count == 0:
        sample_products = [
            ("Leche Entera Pascual 1L", 1.20, 150, "Lácteos", "Leche entera fresca de alta calidad"),
            ("Pan de Molde Bimbo", 1.50, 80, "Panadería", "Pan de molde blanco 680g"),
            ("Coca-Cola 2L", 2.10, 200, "Bebidas", "Refresco de cola 2 litros"),
            ("Aceite de Oliva Carbonell 1L", 5.50, 60, "Aceites", "Aceite de oliva virgen extra"),
            ("Arroz Integral SOS 1kg", 1.80, 120, "Cereales", "Arroz integral de grano largo"),
            ("Tomate Frito Orlando 400g", 0.95, 180, "Conservas", "Tomate frito casero en lata"),
            ("Pasta Gallo Macarrones 500g", 1.30, 150, "Pasta", "Macarrones de sémola de trigo"),
            ("Yogur Natural Danone Pack 8", 2.40, 100, "Lácteos", "Yogures naturales sin azúcar"),
            ("Huevos Camperos Docena", 3.20, 90, "Huevos", "Huevos de gallinas camperas talla L"),
            ("Atún en Aceite Calvo Pack 3", 4.50, 110, "Conservas", "Atún claro en aceite de oliva"),
            ("Agua Mineral Bezoya 6L", 1.80, 200, "Bebidas", "Agua mineral natural pack 6 botellas"),
            ("Cerveza Mahou 5 Estrellas Pack 6", 3.90, 85, "Bebidas", "Cerveza rubia 6 latas de 33cl"),
            ("Galletas María Fontaneda 800g", 1.65, 95, "Galletas", "Galletas María clásicas"),
            ("Zumo de Naranja Don Simón 1L", 1.45, 130, "Bebidas", "Zumo de naranja exprimida"),
            ("Café Marcilla Natural 250g", 3.80, 75, "Cafés", "Café molido natural"),
            ("Patatas Fritas Lays Original 160g", 1.95, 140, "Snacks", "Patatas fritas con sal"),
            ("Chocolate Milka 125g", 1.70, 110, "Chocolates", "Chocolate con leche alpino"),
            ("Jamón Cocido Campofrío 180g", 2.80, 65, "Embutidos", "Jamón cocido extra en lonchas"),
            ("Tomate Natural 1kg", 2.30, 100, "Frutas y Verduras", "Tomates frescos de la huerta"),
            ("Plátanos de Canarias 1kg", 1.60, 120, "Frutas y Verduras", "Plátanos maduros de Canarias")
        ]
        
        cursor.executemany('''
            INSERT INTO products (name, price, stock, category, description)
            VALUES (?, ?, ?, ?, ?)
        ''', sample_products)
        
        conn.commit()
        print(f"✅ Base de datos inicializada con {len(sample_products)} productos")
    else:
        print(f"ℹ️ Base de datos ya contiene {count} productos")
    
    conn.close()

def get_all_products():
    """Obtiene todos los productos"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products ORDER BY id')
    products = cursor.fetchall()
    conn.close()
    return [dict(row) for row in products]

def get_product_by_id(product_id):
    """Obtiene un producto por ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return dict(product) if product else None

def insert_product(name, price, stock, category=None, description=None):
    """Inserta un nuevo producto"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price, stock, category, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, price, stock, category, description))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return get_product_by_id(product_id)

def update_product(product_id, name, price, stock, category=None, description=None):
    """Actualiza un producto existente"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products 
        SET name = ?, price = ?, stock = ?, category = ?, description = ?
        WHERE id = ?
    ''', (name, price, stock, category, description, product_id))
    conn.commit()
    conn.close()
    return get_product_by_id(product_id)

def delete_product(product_id):
    """Elimina un producto"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
