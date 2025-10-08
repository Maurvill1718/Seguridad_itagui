# 🚀 GUÍA COMPLETA PARA TU AMIGO - DESDE CERO HASTA FUNCIONANDO

## 📋 **¿QUÉ ES ESTO?**
Esta es una aplicación súper profesional que analiza testimonios de seguridad en Itagüí usando inteligencia artificial de Google. 

**¿Qué hace?**
- 😊 **Detecta emociones** (alegría, enojo, miedo, etc.)
- ✅ **Analiza si es verdadero o falso** 
- 📋 **Da explicaciones detalladas** de por qué
- 🎯 **Todo con porcentajes de confianza**

---

## 🎯 **PASO 1: DESCARGAR DESDE GITHUB**

### **¿Qué es GitHub?**
Es como una "nube" donde está guardado el proyecto. Es gratis y seguro.

### **Cómo descargarlo:**
1. **Ve a esta página**: https://github.com/Maurvill1718/Seguridad_itagui
2. **Haz clic en el botón verde** que dice **"Code"**
3. **Haz clic en "Download ZIP"**
4. **Se descargará un archivo** llamado `Seguridad_itagui-main.zip`
5. **Haz clic derecho** en el archivo descargado
6. **Selecciona "Extraer aquí"** o "Extract here"
7. **Se creará una carpeta** llamada `Seguridad_itagui-main`
8. **Renómbrala** a `Seguridad_itagui` (más fácil)

---

## 🎯 **PASO 2: INSTALAR PYTHON**

### **¿Qué es Python?**
Es un programa que necesita tu computadora para que funcione la aplicación.

### **Cómo instalarlo:**
1. **Ve a**: https://www.python.org/downloads/
2. **Haz clic en "Download Python"** (botón amarillo grande)
3. **Ejecuta el archivo** que se descargó
4. **IMPORTANTE**: Marca la casilla **"Add Python to PATH"** ✅
5. **Haz clic en "Install Now"**
6. **Espera** a que termine (puede tardar unos minutos)
7. **Haz clic en "Close"**

### **¿Cómo saber si se instaló?**
1. **Presiona Windows + R**
2. **Escribe**: `cmd`
3. **Presiona Enter**
4. **Escribe**: `python --version`
5. **Si aparece algo como "Python 3.x.x"** ✅ **¡Está instalado!**

---

## 🎯 **PASO 3: OBTENER API KEY DE GOOGLE**

### **¿Qué es una API Key?**
Es como una "llave" que permite usar la inteligencia artificial de Google. Es **GRATIS**.

### **Cómo obtenerla:**
1. **Ve a**: https://aistudio.google.com/
2. **Inicia sesión** con tu cuenta de Google (si no tienes, créala)
3. **Haz clic en "Get API Key"**
4. **Haz clic en "Create API Key"**
5. **COPIA la clave** que aparece (empieza con "AIza...")
6. **Guárdala** en un archivo de texto para no perderla

---

## 🎯 **PASO 4: EJECUTAR LA APLICACIÓN**

### **Opción A: Método SÚPER FÁCIL (Recomendado)**
1. **Ve a la carpeta** `Seguridad_itagui` que descargaste
2. **Busca el archivo** `EJECUTAR_APLICACION.bat`
3. **Haz doble clic** en ese archivo
4. **Presiona Enter** (ya tiene API Key configurada)
5. **¡Listo!** Se abrirá automáticamente en tu navegador

### **Opción B: Método Manual (Si el anterior no funciona)**
1. **Presiona Windows + R**
2. **Escribe**: `cmd`
3. **Presiona Enter**
4. **Escribe estos comandos uno por uno**:

```bash
cd C:\Users\[TU_USUARIO]\Desktop\Seguridad_Antioquia\nlp_seguridad_itagui
set GEMINI_API_KEY=AIzaSyAzhPbE9w4s2h790qG2rsc9MH5ULS2mmh8
python app.py
```

**Reemplaza:**
- `[TU_USUARIO]` = tu nombre de usuario de Windows (ver cómo obtenerlo abajo)
- **¡La API Key ya está configurada!** No necesitas cambiarla

### **¿Cómo saber tu nombre de usuario?**
1. **Presiona** `Windows + R`
2. **Escribe**: `whoami`
3. **Presiona Enter**
4. **Copia el nombre** que aparece (sin el dominio)

### **Ejemplo paso a paso:**
1. **Presiona** `Windows + R` (se abre "Ejecutar")
2. **Escribe**: `whoami`
3. **Presiona Enter**
4. **Verás algo como**: `DESKTOP-ABC123\juan` o `juan`
5. **Tu usuario es**: `juan` (la parte después de la barra `\`)

### **Si no funciona el comando `whoami`:**
**Método alternativo:**
1. **Presiona** `Windows + R`
2. **Escribe**: `cmd`
3. **Presiona Enter**
4. **En la ventana negra, escribe**: `echo %USERNAME%`
5. **Presiona Enter**
6. **Verás tu nombre de usuario**

### **Ejemplo:**
Si tu usuario es `juan`, el comando sería:
```bash
cd C:\Users\juan\Desktop\Seguridad_Antioquia\nlp_seguridad_itagui
```

---

## 🎯 **PASO 5: USAR LA APLICACIÓN**

1. **Se abrirá tu navegador** automáticamente en `http://localhost:5000`
2. **Escribe un testimonio** en el cuadro de texto grande
3. **Haz clic en "🔍 Analizar Testimonio"**
4. **Espera unos segundos** (la IA está analizando)
5. **¡Ve los resultados!** 🎉

### **Ejemplos de testimonios para probar:**
- "Ayer nos encontramos 1 millón de dólares con unos amigos"
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

### **❌ "No se encuentra el archivo"**
- **Solución**: Asegúrate de estar en la carpeta correcta
- **Verifica** que descargaste todo desde GitHub

---

## 📞 **¿NECESITAS AYUDA?**

Si algo no funciona:
1. **Contacta a Mauricio** 📱
2. **Toma una captura de pantalla** del error 📸
3. **Explica qué estabas haciendo** cuando pasó 📝

---

## 🎉 **¡LISTO!**

**¡Ya sabes cómo usar la aplicación!** 

**Recuerda:**
- ✅ Descargar desde GitHub
- ✅ Instalar Python
- ✅ Obtener API Key de Google
- ✅ Ejecutar `EJECUTAR_APLICACION.bat`
- ✅ ¡Disfrutar del análisis!

**¡Es súper fácil una vez que lo haces la primera vez!** 🚀

---

## 🔗 **ENLACES ÚTILES**

- **GitHub del proyecto**: https://github.com/Maurvill1718/Seguridad_itagui
- **Descargar Python**: https://www.python.org/downloads/
- **Obtener API Key**: https://aistudio.google.com/

**¡Que disfrutes usando la aplicación!** 🎊
