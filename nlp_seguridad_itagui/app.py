from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Configurar Google Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def analizar_con_gemini(testimonio):
    """Analizar testimonio usando Google Gemini"""
    prompt = f"""Analiza este testimonio de seguridad en Itagüí con detalle profesional:

Testimonio: "{testimonio}"

ANÁLISIS REQUERIDO:

1. EMOCIÓN: Identifica la emoción principal y explica POR QUÉ
   - Enojo: Para casos de abuso/violencia
   - Miedo: Para amenazas/peligros
   - Alegría: Para experiencias positivas
   - Preocupación: Para rumores/incertidumbre
   - Neutral: Para información objetiva

2. VERACIDAD: Evalúa la credibilidad y explica POR QUÉ
   - Verdadero: Experiencias reales con detalles específicos
   - Falso: Elementos imposibles, exagerados o irreales
   - Rumor: Información de segunda mano
   - Incierto: Información ambigua

3. RESUMEN: Resumen profesional con contexto

IMPORTANTE: 
- Genera porcentajes de confianza coherentes (60-95%)
- Para elementos obviamente falsos: 85-95% de confianza
- Para casos reales: 70-85% de confianza
- Para casos inciertos: 60-75% de confianza

Responde EXACTAMENTE en este formato:
EMOCIÓN: [emoción] ([porcentaje]% de confianza) - [explicación detallada del por qué]
VERACIDAD: [veracidad] ([porcentaje]% de confianza) - [análisis detallado del por qué]
RESUMEN: [resumen profesional completo]"""

    print(f"🔍 Conectando con Google Gemini...")
    print(f"🔑 API Key configurada: {'Sí' if GEMINI_API_KEY else 'No'}")
    
    try:
        if not GEMINI_API_KEY:
            raise Exception("API Key de Google Gemini no configurada")
        
        # Usar Google Gemini API
        headers = {"Content-Type": "application/json"}
        
        # URL de Gemini API - usando el modelo estable
        API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        print(f"📤 Enviando prompt a Google Gemini...")
        response = requests.post(API_URL, headers=headers, json=payload)
        
        print(f"📡 Status Code: {response.status_code}")
        print(f"📡 Response Text: {response.text[:200]}...")
        
        if response.status_code != 200:
            raise Exception(f"Error HTTP {response.status_code}: {response.text}")
        
        result = response.json()
        
        if 'candidates' in result and len(result['candidates']) > 0:
            contenido = result['candidates'][0]['content']['parts'][0]['text']
            print(f"✅ Respuesta recibida de Google Gemini")
            print(f"📝 Respuesta completa: {contenido}")
            return contenido
        else:
            raise Exception("No se recibió respuesta válida de Gemini")
        
    except Exception as e:
        print(f"❌ Error con Google Gemini: {e}")
        import traceback
        traceback.print_exc()
        return None

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    """Analiza el testimonio usando Hugging Face"""
    try:
        # Obtener el testimonio
        if request.is_json:
            data = request.get_json()
            testimonio = data.get('testimonio', '').strip()
        else:
            testimonio = request.form.get('testimonio', '').strip()
        
        if not testimonio:
            return jsonify({'error': 'Por favor, escribe un testimonio para analizar'}), 400
        
        # Usar Google Gemini para análisis
        resultado_texto = analizar_con_gemini(testimonio)
        
        if not resultado_texto:
            return jsonify({'error': 'Google Gemini no está disponible. Verifica tu API key.'}), 500
        
        # Parsear la respuesta de Google Gemini
        lineas = resultado_texto.split('\n')
        emocion = "Neutral"
        veracidad = "Incierto"
        resumen = testimonio[:100] + "..." if len(testimonio) > 100 else testimonio
        explicacion_emocion = "Análisis de inteligencia artificial"
        explicacion_veracidad = "Análisis de inteligencia artificial"
        
        # Variables para porcentajes de Hugging Face
        confianza_emocion_hf = None
        confianza_veracidad_hf = None
        
        for linea in lineas:
            if linea.startswith('EMOCIÓN:'):
                emocion_completa = linea.replace('EMOCIÓN:', '').strip()
                if ' - ' in emocion_completa:
                    emocion_part, explicacion_emocion = emocion_completa.split(' - ', 1)
                    emocion_part = emocion_part.strip()
                    explicacion_emocion = explicacion_emocion.strip()
                    
                    if '(' in emocion_part:
                        emocion = emocion_part.split('(')[0].strip()
                        porcentaje_match = emocion_part.split('(')[1].split('%')[0] if '%' in emocion_part else None
                        if porcentaje_match and porcentaje_match.isdigit():
                            confianza_emocion_hf = int(porcentaje_match)
                    else:
                        emocion = emocion_part
                else:
                    emocion_part = emocion_completa
                    if '(' in emocion_part:
                        emocion = emocion_part.split('(')[0].strip()
                    else:
                        emocion = emocion_part
                        
            elif linea.startswith('VERACIDAD:'):
                veracidad_completa = linea.replace('VERACIDAD:', '').strip()
                if ' - ' in veracidad_completa:
                    veracidad_part, explicacion_veracidad = veracidad_completa.split(' - ', 1)
                    veracidad_part = veracidad_part.strip()
                    explicacion_veracidad = explicacion_veracidad.strip()
                    
                    if '(' in veracidad_part:
                        veracidad = veracidad_part.split('(')[0].strip()
                        porcentaje_match = veracidad_part.split('(')[1].split('%')[0] if '%' in veracidad_part else None
                        if porcentaje_match and porcentaje_match.isdigit():
                            confianza_veracidad_hf = int(porcentaje_match)
                    else:
                        veracidad = veracidad_part
                else:
                    veracidad_part = veracidad_completa
                    if '(' in veracidad_part:
                        veracidad = veracidad_part.split('(')[0].strip()
                    else:
                        veracidad = veracidad_part
                        
            elif linea.startswith('RESUMEN:'):
                resumen = linea.replace('RESUMEN:', '').strip()
        
        # Asegurar que tenemos explicaciones detalladas
        if not explicacion_emocion or explicacion_emocion == "Análisis de inteligencia artificial":
            if emocion == "Alegría":
                explicacion_emocion = "El testimonio expresa alegría por la experiencia positiva descrita"
            elif emocion == "Enojo":
                explicacion_emocion = "El testimonio refleja enojo debido a la situación de abuso o violencia"
            elif emocion == "Miedo":
                explicacion_emocion = "El testimonio muestra miedo ante la amenaza o peligro percibido"
            elif emocion == "Preocupación":
                explicacion_emocion = "El testimonio expresa preocupación por la incertidumbre de la situación"
            else:
                explicacion_emocion = f"El testimonio muestra {emocion.lower()} basado en el análisis del contenido"
        
        if not explicacion_veracidad or explicacion_veracidad == "Análisis de inteligencia artificial":
            if veracidad == "Falso":
                explicacion_veracidad = "El testimonio contiene elementos imposibles o exagerados que contradicen la realidad"
            elif veracidad == "Verdadero":
                explicacion_veracidad = "El testimonio presenta detalles específicos y coherentes que sugieren autenticidad"
            elif veracidad == "Rumor":
                explicacion_veracidad = "El testimonio contiene información de segunda mano sin verificación directa"
            else:
                explicacion_veracidad = f"El testimonio es clasificado como {veracidad.lower()} debido a la ambigüedad de la información"
        
        print(f"🎯 Emoción detectada: {emocion}")
        print(f"🎯 Veracidad detectada: {veracidad}")
        
        # Usar porcentajes de Gemini si están disponibles, sino usar valores coherentes
        if confianza_emocion_hf:
            confianza_final_emocion = confianza_emocion_hf
        else:
            # Porcentajes coherentes por defecto
            if emocion == "Alegría":
                confianza_final_emocion = 85.0
            elif emocion == "Enojo":
                confianza_final_emocion = 80.0
            elif emocion == "Miedo":
                confianza_final_emocion = 75.0
            elif emocion == "Preocupación":
                confianza_final_emocion = 70.0
            else:
                confianza_final_emocion = 75.0
        
        if confianza_veracidad_hf:
            confianza_final_veracidad = confianza_veracidad_hf
        else:
            # Porcentajes coherentes por defecto
            if veracidad == "Falso":
                confianza_final_veracidad = 90.0  # Alta confianza para elementos obviamente falsos
            elif veracidad == "Verdadero":
                confianza_final_veracidad = 80.0  # Confianza media para casos reales
            elif veracidad == "Rumor":
                confianza_final_veracidad = 75.0  # Confianza media para rumores
            else:
                confianza_final_veracidad = 65.0  # Baja confianza para casos inciertos
        
        # Preparar respuesta para el frontend
        resultado = {
            'emocion': {
                'tipo': emocion,
                'confianza': confianza_final_emocion,
                'explicacion': explicacion_emocion
            },
            'veracidad': {
                'tipo': veracidad,
                'confianza': confianza_final_veracidad,
                'explicacion': explicacion_veracidad
            },
            'resumen': resumen,
            'testimonio_original': testimonio,
            'analisis_completo': resultado_texto
        }
        return jsonify(resultado)
                
    except Exception as e:
        print(f"❌ Error en análisis: {str(e)}")
        return jsonify({'error': f'Ocurrió un error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
