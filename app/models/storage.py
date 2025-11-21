# Almacenamiento temporal en memoria
products = []
next_id = 1

def insert_product(product):
    global next_id
    product.id = next_id
    next_id += 1
    products.append(product)
    return product

def get_all_products():
    return products

