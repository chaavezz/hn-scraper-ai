import json
from openai import OpenAI
import datetime
archivo = "hn_headlines_2026-03-27.json"
texto_titulares = ""

with open(archivo, "r") as f:
    datos = json.load(f)

for i, noticia in enumerate(datos, start=1):
    texto_titulares += f"{i}. {noticia['Titulo']}\n"


def generar_prompt(texto):
    pregunta = (
        "Resume estos titulares de forma clara y estructurada.\n"
        "Incluye:\n"
        "- Un resumen general breve\n"
        "- 5-7 ideas clave\n"
        "- Tendencias principales\n"
        "Sé conciso y evita redundancias."
    )
    prompt = f"{pregunta}\n\n{texto}"
    return prompt
def preguntar_a_la_ia(prompt):
    try:
        client = OpenAI()

        response = client.responses.create(
            model="gpt-5.4",
            input=prompt
        )
        return response.output_text
    except Exception as e:

        return f"Error al consultar a la IA: {e}"
    

prompt = generar_prompt(texto_titulares)
respuesta = preguntar_a_la_ia(prompt)
fecha = datetime.date.today()
nombre_summary = f"hn_summary_{fecha}.txt"
with open(nombre_summary, "w") as f:
    f.write(respuesta)

print(f"Archivo resumen generado: {nombre_summary}")
