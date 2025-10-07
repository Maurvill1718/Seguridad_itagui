# 🛡️ Análisis de Seguridad en Itagüí con IA

Una aplicación web profesional que analiza testimonios de seguridad ciudadana en Itagüí usando **Google Gemini** para detectar emociones, veracidad y generar explicaciones detalladas.

## 🚀 Características Principales

- **🧠 Análisis Emocional**: Detecta alegría, enojo, miedo, preocupación con IA avanzada
- **✅ Análisis de Veracidad**: Evalúa verdadero, falso, rumor o incierto con explicaciones
- **📋 Explicaciones Detalladas**: Resúmenes contextuales profesionales
- **🎨 Interfaz Moderna**: Diseño profesional con colores dinámicos y gradientes
- **⚡ Tiempo Real**: Análisis instantáneo con Google Gemini API

## 🛠️ Tecnologías

- **Backend**: Python + Flask
- **IA**: Google Gemini API
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Estilos**: Diseño responsivo con gradientes

## 📚 Documentación Completa

- **`GUIA_COMPLETA_PARA_AMIGO.md`**: Guía súper detallada paso a paso para usuarios sin conocimientos técnicos
- **`instrucciones/GUIA_SUPER_SIMPLE.md`**: Instrucciones básicas
- **`instrucciones/INSTRUCCIONES_GEMINI.md`**: Guía específica para Gemini

## 🚀 Instalación Súper Fácil

### Método Automático (Recomendado) ⭐
1. **Descarga desde GitHub**: https://github.com/Maurvill1718/Seguridad_itagui
2. **Extrae la carpeta** en tu escritorio
3. **Doble clic** en `EJECUTAR_APLICACION.bat`
4. **Pega tu API Key** de Google Gemini
5. **¡Listo!** Se abre automáticamente en tu navegador

### Método Manual
```bash
# 1. Clonar repositorio
git clone https://github.com/Maurvill1718/Seguridad_itagui.git
cd Seguridad_itagui

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API Key
set GEMINI_API_KEY=tu_api_key_aqui

# 4. Ejecutar aplicación
python nlp_seguridad_itagui/app.py
```

## 🎯 Uso

1. **Abrir aplicación** en navegador: `http://localhost:5000`
2. **Escribir testimonio** en el campo de texto
3. **Hacer clic** en "🔍 Analizar Testimonio"
4. **Revisar resultados**:
   - Emoción detectada con porcentaje de confianza
   - Veracidad evaluada con análisis detallado
   - Explicación contextual de la situación

## 📊 Ejemplos de Análisis

### Testimonio Positivo
```
Input: "Estoy muy feliz con las nuevas instalaciones del parque"
Output: 
- Emoción: Alegría (85% confianza)
- Veracidad: Verdadero (80% confianza)
- Explicación: Experiencia positiva con mejoras urbanas
```

### Testimonio Falso
```
Input: "Ayer nos encontramos 1 millon de dolares"
Output:
- Emoción: Alegría (85% confianza)  
- Veracidad: Falso (90% confianza)
- Explicación: Elementos imposibles que contradicen la realidad
```

### Testimonio de Rumor
```
Input: "Dicen que hay una banda nueva operando"
Output:
- Emoción: Preocupación (75% confianza)
- Veracidad: Rumor (75% confianza)
- Explicación: Información de segunda mano sin verificación
```

## 🔑 Configuración de API

### Variables de Entorno
```bash
# Windows
set GEMINI_API_KEY=tu_api_key_aqui

# Linux/Mac
export GEMINI_API_KEY=tu_api_key_aqui
```

### Límites de API
- **Plan Gratuito**: 15 requests/minuto
- **Sin límite diario** estricto
- **Manejo de errores** integrado

## 🎨 Personalización

### Colores por Tipo
- **Verdadero**: Verde (`#2ed573`)
- **Falso**: Rojo (`#ff4757`)
- **Rumor**: Rojo claro (`#ff6b6b`)
- **Incierto**: Naranja (`#ffa502`)

### Emojis por Estado
- **✅ Verdadero**: Checkmark verde
- **❌ Falso**: X roja
- **⚠️ Rumor**: Advertencia
- **❓ Incierto**: Interrogación

## 🚨 Solución de Problemas

### Error 429 - Límite Excedido
```
Solución: Esperar unos minutos o crear nueva API Key
```

### Error 404 - Modelo No Encontrado
```
Solución: Verificar que se use gemini-2.5-flash
```

### Error de Conexión
```
Solución: Verificar conexión a internet y API Key válida
```

## 📈 Mejoras Futuras

- [ ] Análisis de múltiples testimonios
- [ ] Exportación de reportes
- [ ] Dashboard de estadísticas
- [ ] Integración con bases de datos
- [ ] Análisis de imágenes

## 👥 Contribuciones

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama de feature
3. Commit de cambios
4. Pull request

## 📄 Licencia

Proyecto desarrollado para la comunidad de Itagüí, Antioquia.

## 📞 Soporte

Para soporte técnico, contactar a Mauricio.

---

**Desarrollado con ❤️ para la seguridad ciudadana de Itagüí**
