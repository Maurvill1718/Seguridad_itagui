@echo off
title Analizador de Seguridad Itagui

echo.
echo ========================================
echo    ANALIZADOR DE SEGURIDAD ITAGUI
echo ========================================
echo.

REM --- PASO 1: Navegar a la carpeta correcta ---
echo [1/3] Navegando a la carpeta del proyecto...
cd /d "%~dp0"
echo ✓ Carpeta encontrada
echo.

REM --- PASO 2: Configurar la API Key de Google Gemini ---
echo [2/3] Configurando la API Key de Google Gemini...
echo.
echo Para que funcione la inteligencia artificial, necesitas una API Key de Google.
echo Es GRATUITA y muy fácil de obtener.
echo.
echo Si no tienes una API Key:
echo 1. Ve a: https://aistudio.google.com/
echo 2. Inicia sesión con tu cuenta de Google
echo 3. Haz clic en "Get API Key" → "Create API Key"
echo 4. Copia la clave que empieza con "AIza..."
echo.
set /p API_KEY="Pega tu API Key aquí y presiona Enter: "
if "%API_KEY%"=="" (
    echo.
    echo ❌ ERROR: Necesitas una API Key para continuar.
    echo Ve a https://aistudio.google.com/ y obtén una gratis.
    echo.
    pause
    exit
) else (
    set GEMINI_API_KEY=%API_KEY%
    echo ✓ API Key configurada correctamente
)
echo.

REM --- PASO 3: Iniciando la aplicación ---
echo [3/3] Iniciando la aplicación...
echo.
echo 🚀 ¡La aplicación se está iniciando!
echo.
echo Cuando veas "Accede a: http://localhost:5000" en esta ventana,
echo se abrirá automáticamente tu navegador.
echo.
echo ⚠️  IMPORTANTE: NO CIERRES esta ventana mientras uses la aplicación.
echo.
echo ========================================
echo.

REM Configurar la variable de entorno
setx GEMINI_API_KEY "%GEMINI_API_KEY%" > NUL 2>&1

REM Iniciar la aplicación
python app.py

echo.
echo ========================================
echo La aplicación se ha cerrado.
echo Presiona cualquier tecla para salir...
pause > NUL