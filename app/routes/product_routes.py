from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.database import db

router = APIRouter()

@router.post("/products", response_model=Product)
def add_product(product: Product):
    """Agregar un nuevo producto"""
    try:
        new_product = db.insert_product(
            name=product.name,
            price=product.price,
            stock=product.stock,
            category=product.category,
            description=product.description
        )
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/products")
def get_products():
    """Obtener todos los productos"""
    try:
        products = db.get_all_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Obtener un producto específico por ID"""
    product = db.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    """Actualizar un producto existente"""
    existing = db.get_product_by_id(product_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    try:
        updated = db.update_product(
            product_id=product_id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            category=product.category,
            description=product.description
        )
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Eliminar un producto"""
    success = db.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente", "id": product_id}
