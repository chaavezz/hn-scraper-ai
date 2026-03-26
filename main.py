import requests
import datetime
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
fecha = datetime.date.today()
nombre_de_archivo= f"hn_headlines_{fecha}.txt"

def main():
    try:
        respuesta = requests.get(url, timeout=10)
        soup = BeautifulSoup(respuesta.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Error en la petición:", e)
        return
        
    links = soup.find_all("span", class_="titleline")

    with open(nombre_de_archivo, "w") as f:
        f.write("HACKER NEWS HEADLINES\n")
        f.write(f"FECHA: {fecha}\n")
        f.write(f"FUENTE: {url}\n")
        f.write("---------------------------------------\n")
        for i, link in enumerate(links, start=1):
            titulo = link.find("a")
            f.write(f"{i}. {titulo.text}\n")
    print(f"Archivo generado: {nombre_de_archivo}")
    print(f"Titulares guardados: {len(links)}")

if __name__ == "__main__":
    main()