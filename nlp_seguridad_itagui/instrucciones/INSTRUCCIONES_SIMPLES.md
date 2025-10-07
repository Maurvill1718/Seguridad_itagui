# 🛡️ Análisis de Seguridad en Itagüí - Instrucciones para Usar

## 📋 ¿Qué es esto?
Esta es una aplicación web que analiza testimonios sobre seguridad en Itagüí usando inteligencia artificial (Google Gemini).

## 🚀 Instrucciones SÚPER SIMPLES

### Paso 1: Descargar el proyecto
1. Ve a GitHub (si te pasaron el enlace)
2. Haz clic en el botón verde "Code"
3. Selecciona "Download ZIP"
4. Extrae la carpeta en tu escritorio

### Paso 2: Instalar Python (si no lo tienes)
1. Ve a https://www.python.org/downloads/
2. Descarga Python (botón amarillo grande)
3. Instálalo marcando "Add Python to PATH"
4. Reinicia tu computadora

### Paso 3: Obtener API Key de Google Gemini
1. Ve a https://aistudio.google.com/
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Get API Key" → "Create API Key"
4. Copia la clave que empieza con "AIza..."

### Paso 4: Abrir la aplicación
1. Ve a la carpeta del proyecto en tu escritorio
2. Haz clic derecho en un espacio vacío
3. Selecciona "Abrir en Terminal" (Windows) o "Abrir Terminal aquí"
4. Copia y pega estos comandos uno por uno:

```
pip install -r requirements.txt
```

```
set GEMINI_API_KEY=TU_API_KEY_AQUI
```

```
python app.py
```

### Paso 5: Usar la aplicación
1. Abre tu navegador (Chrome, Firefox, etc.)
2. Ve a: http://localhost:5000
3. Escribe un testimonio sobre seguridad
4. Haz clic en "Analizar Testimonio"
5. ¡Listo! Verás el análisis

## 🔑 ¿Cómo conseguir la API Key?
1. Ve a https://aistudio.google.com/
2. Inicia sesión con tu cuenta de Google
3. Ve a "Get API Key" → "Create API Key"
4. Copia la clave que aparece
5. Reemplaza "TU_API_KEY_AQUI" con esa clave

## ❓ ¿Qué hacer si algo no funciona?

### Si aparece error de "pip":
- Abre PowerShell como administrador
- Ejecuta: `python -m pip install --upgrade pip`

### Si aparece error de "python":
- Reinstala Python marcando "Add to PATH"

### Si la página no carga:
- Asegúrate de que la terminal esté abierta y ejecutándose
- NO cierres la terminal mientras uses la aplicación

### Si aparece error de API Key:
- Verifica que copiaste bien la clave
- Asegúrate de que la cuenta esté activa

## 📞 ¿Necesitas ayuda?
Contacta a Mauricio para ayuda técnica.

---
**¡Esperamos que te sea útil para analizar la seguridad en Itagüí!** 🛡️
