import requests
import datetime
from bs4 import BeautifulSoup
import json

base_url = "https://news.ycombinator.com/"

def main():
    
    today = datetime.date.today()
    txt_filename= f"hn_headlines_{today}.txt"
    json_filename = f"hn_headlines_{today}.json"
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return
        
    links = soup.find_all("span", class_="titleline")
    data = []
    for link in links:
        title = link.find("a")
        link_url = title["href"]
        item = {
            "title": title.text,
            "url": link_url
            }
        data.append(item)
    with open(json_filename, "w") as f:
        json.dump(data,f, indent=4)

    with open(txt_filename, "w") as f:
        f.write("HACKER NEWS HEADLINES\n")
        f.write(f"SOURCE: {base_url}\n")
        f.write(f"DATE: {today}\n")
        f.write("--------------------------\n\n")

        for i, item in enumerate(data, start=1):
            f.write(f"{i}. {item['title']}\n")
            f.write(f"{item['url']}\n\n")
            
            
    print(f"JSON file generated: {json_filename}")
    print(f"TXT file generated: {txt_filename}")
    print(f"Total headlines: {len(data)}")

if __name__ == "__main__":
    main()