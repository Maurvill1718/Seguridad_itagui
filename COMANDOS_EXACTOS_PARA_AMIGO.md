# 🖥️ COMANDOS EXACTOS PARA EJECUTAR LA APLICACIÓN

## 📋 **¿QUÉ NECESITAS HACER?**

Una vez que descargues la carpeta desde GitHub, necesitas ejecutar estos comandos **exactos** en tu computadora.

---

## 🎯 **PASO 1: ABRIR LA TERMINAL**

### **En Windows:**
1. **Presiona** `Windows + R`
2. **Escribe**: `cmd`
3. **Presiona Enter**
4. **Se abrirá una ventana negra** (esa es la terminal)

---

## 🎯 **PASO 2: NAVEGAR A LA CARPETA**

### **Comando exacto:**
```bash
cd C:\Users\[TU_USUARIO]\Desktop\Seguridad_itagui
```

**⚠️ IMPORTANTE**: Reemplaza `[TU_USUARIO]` con tu nombre de usuario de Windows.

### **¿Cómo saber tu nombre de usuario?**
1. **Presiona** `Windows + R`
2. **Escribe**: `whoami`
3. **Presiona Enter**
4. **Copia el nombre** que aparece (sin el dominio)

### **Ejemplo:**
Si tu usuario es `juan`, el comando sería:
```bash
cd C:\Users\juan\Desktop\Seguridad_itagui
```

---

## 🎯 **PASO 3: INSTALAR DEPENDENCIAS**

### **Comando exacto:**
```bash
pip install -r requirements.txt
```

**¿Qué hace esto?**
- Instala todas las librerías que necesita la aplicación
- Puede tardar 1-2 minutos
- **NO cierres la ventana** hasta que termine

---

## 🎯 **PASO 4: CONFIGURAR API KEY**

### **Comando exacto:**
```bash
set GEMINI_API_KEY=tu_api_key_aqui
```

**⚠️ IMPORTANTE**: Reemplaza `tu_api_key_aqui` con tu API Key real de Google Gemini.

### **Ejemplo:**
```bash
set GEMINI_API_KEY=AIzaSyAzhPbE9w4s2h790qG2rsc9MH5ULS2mmh8
```

**🎉 ¡BUENAS NOTICIAS!** Ya tienes una API Key configurada. Puedes usar esta directamente:
```bash
set GEMINI_API_KEY=AIzaSyAzhPbE9w4s2h790qG2rsc9MH5ULS2mmh8
```

---

## 🎯 **PASO 5: EJECUTAR LA APLICACIÓN**

### **Comando exacto:**
```bash
python nlp_seguridad_itagui/app.py
```

**¿Qué hace esto?**
- Inicia el servidor de la aplicación
- Verás mensajes como "Iniciando aplicación..."
- **NO cierres esta ventana** mientras uses la app

---

## 🎯 **PASO 6: ABRIR EN EL NAVEGADOR**

1. **Abre tu navegador** (Chrome, Firefox, Edge, etc.)
2. **Ve a**: `http://localhost:5000`
3. **¡Listo!** Ya puedes usar la aplicación

---

## 📋 **SECUENCIA COMPLETA DE COMANDOS**

### **Copia y pega estos comandos uno por uno:**

```bash
cd C:\Users\[TU_USUARIO]\Desktop\Seguridad_itagui
pip install -r requirements.txt
set GEMINI_API_KEY=AIzaSyAzhPbE9w4s2h790qG2rsc9MH5ULS2mmh8
python nlp_seguridad_itagui/app.py
```

**⚠️ RECUERDA**: 
- Cambiar `[TU_USUARIO]` por tu usuario real
- **¡La API Key ya está lista!** No necesitas cambiarla

---

## 🚨 **SI ALGO SALE MAL**

### **❌ "python no se reconoce como comando"**
**Solución**: Python no está instalado
1. Ve a: https://www.python.org/downloads/
2. Instala Python
3. **IMPORTANTE**: Marca "Add Python to PATH"

### **❌ "pip no se reconoce como comando"**
**Solución**: Mismo problema que arriba
1. Reinstala Python
2. Marca "Add Python to PATH"

### **❌ "No se puede acceder a este sitio"**
**Solución**: 
1. Verifica que el comando `python nlp_seguridad_itagui/app.py` esté corriendo
2. Espera unos segundos
3. Recarga la página

### **❌ "Error del servidor: 500"**
**Solución**: 
1. Verifica que tu API Key sea correcta
2. Asegúrate de que el comando `set GEMINI_API_KEY=...` se ejecutó bien

---

## 🎯 **MÉTODO ALTERNATIVO MÁS FÁCIL**

### **Si los comandos te dan miedo:**

1. **Ve a la carpeta** `Seguridad_itagui`
2. **Busca el archivo** `EJECUTAR_APLICACION.bat`
3. **Haz doble clic** en ese archivo
4. **Pega tu API Key** cuando te la pida
5. **Presiona Enter**
6. **¡Listo!** Se abre automáticamente

---

## 📞 **¿NECESITAS AYUDA?**

Si algo no funciona:
1. **Contacta a Mauricio** 📱
2. **Toma captura de pantalla** del error 📸
3. **Explica qué comando estabas ejecutando** 📝

---

## 🎉 **¡LISTO!**

**¡Ya sabes exactamente qué comandos ejecutar!** 

**¡Es súper fácil una vez que lo haces la primera vez!** 🚀
