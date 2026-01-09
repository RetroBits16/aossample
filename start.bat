@echo off
echo 🛒 Iniciando Sistema de Gestión de Supermercado
echo ==============================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado. Por favor instala Python 3.7 o superior.
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Instalar dependencias
echo 📦 Instalando dependencias...
pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    echo ❌ Error al instalar dependencias
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas correctamente
echo.

REM Iniciar el servidor
echo 🚀 Iniciando servidor backend...
echo 📍 URL: http://127.0.0.1:8000
echo 📖 Documentación API: http://127.0.0.1:8000/docs
echo.
echo ⚠️  Para abrir el frontend, abre el archivo frontend\index.html en tu navegador
echo.
echo ⏹️  Presiona Ctrl+C para detener el servidor
echo.

python main.py
