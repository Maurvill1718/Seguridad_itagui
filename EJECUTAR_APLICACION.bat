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
echo ¡BUENAS NOTICIAS! Ya tienes una API Key configurada y funcionando.
echo Si quieres usar una diferente, puedes cambiarla aquí.
echo.
set /p API_KEY="¿Quieres usar una API Key diferente? (presiona Enter para usar la predeterminada): "
if "%API_KEY%"=="" (
    set GEMINI_API_KEY=AIzaSyAzhPbE9w4s2h790qG2rsc9MH5ULS2mmh8
    echo ✓ Usando API Key predeterminada (ya configurada y funcionando)
) else (
    set GEMINI_API_KEY=%API_KEY%
    echo ✓ Usando tu API Key personalizada
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