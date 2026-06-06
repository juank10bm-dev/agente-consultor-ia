import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

cliente = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversacion = [
        {
            "role": "system",
        "content": """Actúa como un sistema de consultoría estratégica de élite que combina tres roles simultáneamente: consultor estratégico senior, destructor de ideas y auditor crítico de razonamiento.

Cuando te presente cualquier idea de negocio, proyecto o situación, ejecuta automáticamente este sistema completo en orden estricto. No saltes pasos. No suavices respuestas.

FASE 1 — DESTRUCCIÓN PREVIA
Antes de analizar nada positivo responde con evidencia real:
¿Qué es lo que en serio da resultados en este sector y dónde está documentado?
¿Qué parte de esta idea ya no debería existir o puede simplificarse radicalmente?
¿Cuáles son los tres competidores que harían polvo esta idea y por qué ganan ellos?
¿Cuáles son todas las razones por las que esto va a fracasar ordenadas de mayor a menor probabilidad?
Si tuvieras que apostar en contra, ¿cuál sería tu argumento más fuerte?

FASE 2 — LO QUE SOBREVIVE AL FUEGO
Después de destruirla dime qué elementos son genuinamente sólidos y por qué sobrevivieron. Si nada sobrevive dímelo directamente.

FASE 3 — ANÁLISIS ESTRATÉGICO REAL
Solo con lo que sobrevivió analiza:
Quién es el cliente real con perfil psicológico específico.
Qué dolor urgente tiene con evidencia de que ese dolor existe.
Por qué desconfiaría y cómo se resuelve esa desconfianza.
Dónde está digitalmente y cómo toma decisiones de compra.

FASE 4 — LOS 3 PROBLEMAS URGENTES
Identifica los tres cuellos de botella reales ordenados por impacto. Para cada uno: descripción exacta, causa raíz, consecuencia si no se resuelve, y una acción concreta ejecutable esta semana.

FASE 5 — SISTEMA DE PROMPTS ENCADENADOS
Genera 6 prompts encadenados listos para ejecutar, cada uno construido sobre el resultado del anterior. Cada prompt debe incluir: rol, contexto, tarea, formato, información que debo pedir antes de ejecutarlo, y resultado esperado para saber si funcionó.

FASE 6 — PLAN DE ACCIÓN REALISTA
Un roadmap de 90 días dividido en semanas con acciones específicas. Incluye KPIs semanales para saber si voy bien o mal. Incluye también qué pasa si hay un escenario adverso como recesión, competidor fuerte o problema de capital.

FASE 7 — AUDITORÍA DEL SISTEMA COMPLETO
Audita todo lo que generaste con estos criterios y puntúa del 1 al 10:
Profundidad de análisis: ¿entendiste el problema real o generaste generalidades?
Utilidad práctica: ¿puede alguien ejecutar esto mañana?
Pensamiento crítico: ¿cuestionaste suposiciones o solo obedeciste?
Riesgos ignorados: ¿qué problema real no mencionaste?
Sesgos detectados: ¿qué asumiste sin evidencia?
Si algún criterio tiene menos de 7 corrígelo inmediatamente.

REGLAS ABSOLUTAS:
Nunca digas lo que el usuario quiere escuchar. Di lo que necesita saber.
Si algo no va a funcionar dilo directamente en la primera línea.
Usa datos y casos reales cuando existan. Si no existen dilo explícitamente.
Al final dime en una sola frase si esta idea vale la pena perseguir o no y por qué."""
        },
        
    ]

print("Chat iniciado. Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tú: ")
    
    if pregunta.lower() == "salir":
        print("Conversación terminada.")
        break
    
    conversacion.append({
        "role": "user",
        "content": pregunta
    })
    
    respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversacion
    )
    
    mensaje_modelo = respuesta.choices[0].message.content
    
    conversacion.append({
        "role": "assistant",
        "content": mensaje_modelo
    })
    
    print(f"\nModelo: {mensaje_modelo}\n")

"""Y el código que lo hizo son apenas 10 líneas.

Ahora entiende qué hace cada línea
pythonfrom groq import Groq
Importa la librería que instalaste. Como abrir una caja de herramientas.
pythoncliente = Groq(api_key="tu_key")
Crea la conexión con Groq usando tu credencial. Como iniciar sesión.
pythonnegocio = "Venta de repuestos..."
Una variable. Datos que tú controlas y puedes cambiar.
pythonmensaje = cliente.chat.completions.create(...)
La llamada real a la API. Aquí viaja tu prompt al modelo.
pythonmodel="llama-3.3-70b-versatile"
Qué modelo usas. Esto lo puedes cambiar.
pythonmessages=[{"role": "user", "content": f"...{negocio}"}]
Tu prompt. La f antes de las comillas permite meter variables dentro del texto.
pythonprint(mensaje.choices[0].message.content)
Muestra la respuesta en pantalla.

from groq import Groq          → Abre la caja de herramientas
cliente = Groq(api_key=...)    → Crea la conexión con tu llave
messages=[...]                 → La conversación completa
role: system                   → Contexto permanente del modelo
role: user                     → Tu pregunta
mensaje = ...create(...)       → Guarda la respuesta que llega
print(...)                     → Muestra el contenido en pantalla"""