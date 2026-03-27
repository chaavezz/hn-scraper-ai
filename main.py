import requests
import datetime
from bs4 import BeautifulSoup
import json

base_url = "https://news.ycombinator.com/"
fecha = datetime.date.today()
nombre_txt= f"hn_headlines_{fecha}.txt"
nombre_json = f"hn_headlines_{fecha}.json"

def main():
    try:
        respuesta = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(respuesta.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Error en la petición:", e)
        return
        
    links = soup.find_all("span", class_="titleline")
    datos = []
    for link in links:
        titulo = link.find("a")
        link_url = titulo["href"]
        noticia = {
            "Titulo": titulo.text,
            "url": link_url
            }
        datos.append(noticia)
    with open(nombre_json, "w") as f:
        json.dump(datos,f, indent=4)

    with open(nombre_txt, "w") as f:
        f.write("HACKER NEWS HEADLINES\n")
        f.write(f"FUENTE: {base_url}\n")
        f.write(f"FECHA: {fecha}\n")
        f.write("--------------------------\n\n")

        for i, noticia in enumerate(datos, start=1):
            f.write(f"{i}. {noticia['Titulo']}\n")
            f.write(f"{noticia['url']}\n\n")
            
            
    print(f"Archivo JSON generado: {nombre_json}")
    print(f"Archivo TXT generado: {nombre_txt}")
    print(f"Titulares guardados: {len(links)}")

if __name__ == "__main__":
    main()