# 🚀 GUÍA SÚPER SIMPLE - CÓMO USAR LA APLICACIÓN

## 📋 **¿QUÉ ES ESTO?**
Esta aplicación analiza testimonios de seguridad en Itagüí usando inteligencia artificial. Te dice:
- 😊 **Qué emoción** tiene el testimonio
- ✅ **Si es verdadero o falso**
- 📋 **Explicación detallada** de la situación

---

## 🎯 **PASO 1: DESCARGAR TODO**

1. **Descarga la carpeta completa** del proyecto
2. **Guárdala en tu escritorio** (o donde quieras)
3. **NO cambies nombres** de archivos ni carpetas

---

## 🎯 **PASO 2: INSTALAR PYTHON**

### **¿Qué es Python?**
Es un programa que necesita tu computadora para que funcione la aplicación.

### **Cómo instalarlo:**
1. Ve a: **https://www.python.org/downloads/**
2. Haz clic en **"Download Python"** (botón amarillo grande)
3. **Ejecuta el archivo** que se descargó
4. **IMPORTANTE**: Marca la casilla **"Add Python to PATH"** ✅
5. Haz clic en **"Install Now"**
6. Espera a que termine
7. Haz clic en **"Close"**

### **¿Cómo saber si se instaló?**
1. Presiona **Windows + R**
2. Escribe: `cmd`
3. Presiona **Enter**
4. Escribe: `python --version`
5. Si aparece algo como "Python 3.x.x" ✅ **¡Está instalado!**

---

## 🎯 **PASO 3: OBTENER API KEY DE GOOGLE**

### **¿Qué es una API Key?**
Es como una "llave" que permite usar la inteligencia artificial de Google.

### **Cómo obtenerla:**
1. Ve a: **https://aistudio.google.com/**
2. **Inicia sesión** con tu cuenta de Google (si no tienes, créala)
3. Haz clic en **"Get API Key"**
4. Haz clic en **"Create API Key"**
5. **COPIA la clave** que aparece (empieza con "AIza...")
6. **Guárdala** en un archivo de texto

---

## 🎯 **PASO 4: EJECUTAR LA APLICACIÓN**

### **Opción A: Método Fácil (Recomendado)**
1. **Doble clic** en el archivo `EJECUTAR_APLICACION.bat`
2. **Pega tu API Key** cuando te la pida
3. **Presiona Enter**
4. **¡Listo!** Se abrirá automáticamente en tu navegador

### **Opción B: Método Manual**
1. Presiona **Windows + R**
2. Escribe: `cmd`
3. Presiona **Enter**
4. Escribe estos comandos **uno por uno**:

```bash
cd C:\Users\[TU_USUARIO]\Desktop\[NOMBRE_DE_LA_CARPETA]
set GEMINI_API_KEY=tu_api_key_aqui
python app.py
```

**Reemplaza:**
- `[TU_USUARIO]` = tu nombre de usuario de Windows
- `[NOMBRE_DE_LA_CARPETA]` = nombre de la carpeta del proyecto
- `tu_api_key_aqui` = la API key que copiaste

---

## 🎯 **PASO 5: USAR LA APLICACIÓN**

1. **Se abrirá tu navegador** automáticamente
2. **Escribe un testimonio** en el cuadro de texto
3. Haz clic en **"🔍 Analizar Testimonio"**
4. **Espera unos segundos**
5. **¡Ve los resultados!**

### **Ejemplos de testimonios para probar:**
- "Ayer nos encontramos 1 millon de dolares con unos amigos"
- "Me robaron el celular en el parque principal"
- "Dicen que hay una banda nueva operando en el centro comercial"
- "Estoy muy feliz con las nuevas instalaciones del parque"

---

## 🚨 **SOLUCIÓN DE PROBLEMAS**

### **❌ "No se puede acceder a este sitio"**
- **Solución**: Espera unos segundos y recarga la página
- **O**: Cierra la ventana negra y vuelve a ejecutar `EJECUTAR_APLICACION.bat`

### **❌ "Error del servidor: 500"**
- **Solución**: Verifica que tu API Key sea correcta
- **O**: Espera unos minutos y vuelve a intentar

### **❌ "Has excedido el límite de análisis"**
- **Solución**: Espera unas horas y vuelve a intentar
- **O**: Crea una nueva cuenta de Google y obtén otra API Key

### **❌ "python no se reconoce como comando"**
- **Solución**: Python no está instalado o no está en el PATH
- **Reinstala Python** marcando "Add Python to PATH"

---

## 📞 **¿NECESITAS AYUDA?**

Si algo no funciona:
1. **Contacta a Mauricio**
2. **Toma una captura de pantalla** del error
3. **Explica qué estabas haciendo** cuando pasó

---

## 🎉 **¡LISTO!**

**¡Ya sabes cómo usar la aplicación!** 

**Recuerda:**
- ✅ Instalar Python
- ✅ Obtener API Key de Google
- ✅ Ejecutar `EJECUTAR_APLICACION.bat`
- ✅ ¡Disfrutar del análisis!

**¡Es súper fácil una vez que lo haces la primera vez!** 🚀
