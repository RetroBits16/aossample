from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sample, product_routes
from app.database.db import init_db

app = FastAPI(title="Sistema de Gestión de Supermercado")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar base de datos al arrancar
@app.on_event("startup")
async def startup_event():
    init_db()

# Include routers
app.include_router(sample.router, tags=["Sample Operations"])
app.include_router(product_routes.router, tags=["Products"])

@app.get("/")
def root():
    return {"message": "API de Gestión de Supermercado", "status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
