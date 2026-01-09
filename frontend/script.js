// API Base URL
const API_BASE_URL = 'http://127.0.0.1:8000';

// Tab Navigation
function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
}

// Notification System
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// Product Management
document.getElementById('product-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const category = document.getElementById('product-category').value;
    const description = document.getElementById('product-description').value;
    
    const product = {
        name: document.getElementById('product-name').value,
        price: parseFloat(document.getElementById('product-price').value),
        stock: parseInt(document.getElementById('product-stock').value),
        category: category || null,
        description: description || null
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/products`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(product)
        });
        
        if (response.ok) {
            const result = await response.json();
            showNotification('✅ Producto agregado exitosamente', 'success');
            document.getElementById('product-form').reset();
            loadProducts();
        } else {
            const error = await response.json();
            showNotification(`❌ Error: ${error.detail}`, 'error');
        }
    } catch (error) {
        showNotification('❌ Error de conexión con el servidor', 'error');
        console.error('Error:', error);
    }
});

// Load Products
async function loadProducts() {
    const container = document.getElementById('products-list');
    container.innerHTML = '<p class="loading">⏳ Cargando productos...</p>';
    
    try {
        const response = await fetch(`${API_BASE_URL}/products`);
        
        if (response.ok) {
            const products = await response.json();
            displayProducts(products);
            showNotification(`📦 ${products.length} productos cargados`, 'info');
        } else {
            container.innerHTML = '<p class="empty-message">❌ Error al cargar productos</p>';
            showNotification('Error al cargar productos', 'error');
        }
    } catch (error) {
        container.innerHTML = '<p class="empty-message">❌ Error de conexión con el servidor. Asegúrate de que el backend esté ejecutándose en http://127.0.0.1:8000</p>';
        showNotification('Error de conexión', 'error');
        console.error('Error:', error);
    }
}

// Display Products
function displayProducts(products) {
    const container = document.getElementById('products-list');
    
    if (products.length === 0) {
        container.innerHTML = '<p class="empty-message">📦 No hay productos disponibles. ¡Agrega el primero!</p>';
        return;
    }
    
    container.innerHTML = products.map(product => `
        <div class="product-card">
            <div class="product-category">${product.category || 'Sin categoría'}</div>
            <h3>${product.name}</h3>
            <div class="product-info">
                <span class="product-label">ID:</span>
                <span class="product-value product-id">#${product.id}</span>
            </div>
            <div class="product-info">
                <span class="product-label">Precio:</span>
                <span class="product-value product-price">${product.price.toFixed(2)}€</span>
            </div>
            <div class="product-info">
                <span class="product-label">Stock:</span>
                <span class="product-value product-stock ${product.stock < 20 ? 'low-stock' : ''}">${product.stock} unidades</span>
            </div>
            ${product.description ? `<div class="product-description">${product.description}</div>` : ''}
            <button class="btn btn-danger" onclick="deleteProduct(${product.id})">🗑️ Eliminar</button>
        </div>
    `).join('');
}

// Delete Product
async function deleteProduct(id) {
    if (!confirm('¿Estás seguro de eliminar este producto?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/products/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showNotification('🗑️ Producto eliminado', 'success');
            loadProducts();
        } else {
            showNotification('❌ Error al eliminar producto', 'error');
        }
    } catch (error) {
        showNotification('❌ Error de conexión', 'error');
        console.error('Error:', error);
    }
}

// Process Data (Sum)
document.getElementById('process-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        value1: parseInt(document.getElementById('value1').value),
        value2: parseInt(document.getElementById('value2').value)
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/process`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            const result = await response.json();
            const resultBox = document.getElementById('process-result');
            resultBox.innerHTML = `<strong>Resultado:</strong> ${data.value1} + ${data.value2} = <strong>${result.result}</strong>`;
            resultBox.classList.add('show');
        } else {
            showNotification('❌ Error al procesar datos', 'error');
        }
    } catch (error) {
        showNotification('❌ Error de conexión', 'error');
        console.error('Error:', error);
    }
});

// Concatenate Strings
document.getElementById('concat-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const param1 = document.getElementById('param1').value;
    const param2 = document.getElementById('param2').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/concat?param1=${encodeURIComponent(param1)}&param2=${encodeURIComponent(param2)}`);
        
        if (response.ok) {
            const result = await response.json();
            const resultBox = document.getElementById('concat-result');
            resultBox.innerHTML = `<strong>Resultado:</strong> "${param1}" + "${param2}" = <strong>"${result.result}"</strong>`;
            resultBox.classList.add('show');
        } else {
            showNotification('❌ Error al concatenar', 'error');
        }
    } catch (error) {
        showNotification('❌ Error de conexión', 'error');
        console.error('Error:', error);
    }
});

// String Length
document.getElementById('length-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const string = document.getElementById('string-input').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/length?string=${encodeURIComponent(string)}`);
        
        if (response.ok) {
            const result = await response.json();
            const resultBox = document.getElementById('length-result');
            resultBox.innerHTML = `<strong>Resultado:</strong> La longitud de "${string}" es <strong>${result.length}</strong> caracteres`;
            resultBox.classList.add('show');
        } else {
            showNotification('❌ Error al calcular longitud', 'error');
        }
    } catch (error) {
        showNotification('❌ Error de conexión', 'error');
        console.error('Error:', error);
    }
});

// Load products on page load
window.addEventListener('load', () => {
    loadProducts();
});
