#!/bin/bash

echo "🛒 Iniciando Sistema de Gestión de Supermercado"
echo "=============================================="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 no está instalado. Por favor instala Python 3.7 o superior."
    exit 1
fi

echo "✅ Python encontrado"

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "❌ pip3 no está instalado. Por favor instala pip."
    exit 1
fi

echo "✅ pip encontrado"

# Instalar dependencias si no están instaladas
echo ""
echo "📦 Verificando dependencias..."
pip3 install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ Dependencias instaladas correctamente"
else
    echo "❌ Error al instalar dependencias"
    exit 1
fi

echo ""
echo "🚀 Iniciando servidor backend..."
echo "📍 URL: http://127.0.0.1:8000"
echo "📖 Documentación API: http://127.0.0.1:8000/docs"
echo ""
echo "⚠️  Para abrir el frontend, abre el archivo frontend/index.html en tu navegador"
echo "   O ejecuta: cd frontend && python3 -m http.server 8080"
echo ""
echo "⏹️  Presiona Ctrl+C para detener el servidor"
echo ""

# Iniciar el servidor
python3 main.py
