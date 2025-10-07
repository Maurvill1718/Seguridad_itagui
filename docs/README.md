# 🛡️ Analizador de Seguridad Itagüí

Sistema de análisis de testimonios de seguridad ciudadana utilizando inteligencia artificial (Google Gemini).

## 🚀 Características

- **Análisis Emocional**: Detecta emociones (Alegría, Enojo, Miedo, Preocupación, etc.)
- **Análisis de Veracidad**: Evalúa credibilidad (Verdadero, Falso, Rumor, Incierto)
- **Explicación Detallada**: Proporciona análisis contextual completo
- **Interfaz Intuitiva**: Diseño moderno y fácil de usar
- **Tiempo Real**: Análisis instantáneo con IA

## 🛠️ Tecnologías

- **Backend**: Python + Flask
- **IA**: Google Gemini API
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Estilos**: Diseño responsivo con gradientes

## 📁 Estructura del Proyecto

```
nlp_seguridad_itagui/
├── app.py                          # Aplicación principal
├── EJECUTAR_APLICACION.bat         # Script de ejecución automática
├── requirements.txt                # Dependencias Python
├── templates/
│   └── index.html                  # Interfaz web
├── static/
│   └── style.css                   # Estilos CSS
├── instrucciones/
│   └── GUIA_SUPER_SIMPLE.md        # Guía para usuarios no técnicos
├── docs/
│   └── README.md                   # Documentación técnica
└── archivos_antiguos/              # Archivos obsoletos
```

## 🔧 Instalación

### Requisitos
- Python 3.8+
- Cuenta de Google (para API Key)
- Navegador web moderno

### Pasos
1. **Clonar/Descargar** el proyecto
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Obtener API Key** de Google Gemini:
   - Ir a: https://aistudio.google.com/
   - Crear API Key gratuita
4. **Ejecutar aplicación**:
   ```bash
   python app.py
   ```
   O usar: `EJECUTAR_APLICACION.bat`

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

Para soporte técnico, contactar al desarrollador principal.

---

**Desarrollado con ❤️ para la seguridad ciudadana de Itagüí**
