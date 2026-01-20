import pprint

from PIL.ImageOps import expand
from bs4 import BeautifulSoup
from tqdm import tqdm

import requests, json

class FillExpansionData:
    def __init__(self, expansion_info: dict):
        self.expansion_info = expansion_info
        poke_html = requests.get(self.expansion_info["url"]).text
        self.soup = BeautifulSoup(poke_html, 'lxml')

        self.data = {
            "ID": str(self.expansion_info["id"]),
            "Released": "",
            "Cards": {
                "Official": "",
                "Secret": "",
                "Extra": "",
                "Total": ""
            },
            "Splash": "",
            "Icon": ""
        }

        self.parse_basic_info()
        self.parse_card_counts()
        self.parse_images()

    def parse_basic_info(self):
        banner = self.soup.find('div', class_='content setinfo')
        date_box = banner.find('div', class_=None)
        date_element = date_box.get_text().split('\n')
        date = f"{date_element[2].strip()}, {date_element[3].strip()}"
        self.data["Released"] = date

    def parse_card_counts(self):
        banner = self.soup.find('div', class_='content setinfo')
        count_box = banner.find('div', class_='cards')
        count_element = count_box.get_text().split('\n')
        c = self.soup.find('div', class_='content cardlisting small')
        card_box = self.soup.find('div', class_='content cardlisting') if c is None else c
        cards = {
            "Official": count_element[2],
            "Secret": count_element[3].lstrip("+")[:-7] if count_element[3] != "" else "0",
            "Extra": "",
            "Total": str(len(card_box.find_all('div', class_='card')))
        }
        cards["Extra"] = str(max(0, int(cards["Total"]) - int(cards["Official"]) - int(cards["Secret"])))
        self.data["Cards"] = cards

    def parse_images(self):
        splash = self.soup.find('h1', class_='icon set')
        symbol = self.soup.find('h1', class_='icon symbol')
        self.data["Splash"] = splash.find('img')['src']
        self.data["Icon"] = symbol.find('img')['src']

if __name__ == '__main__':
    with open('res/data/identifiers/series.json', 'r') as file:
        data = json.load(file)
    info = {}
    count = 1
    for series in tqdm(data.keys()):
    # for series in list(reversed(data.keys())):
        info[series] = {}
        for expansion in data[series]["expansions"].keys():
            tqdm.write(f"Processing: {expansion}")
            expansion_url = data[series]["expansions"][expansion]["url"]
            app = FillExpansionData({
                "url" : expansion_url,
                "id": count,
                "expansion": expansion,
                "series": series
            })
            info[series][expansion] = app.data
            count += 1
    with open('res/data/identifiers/expansion.json', 'w') as f:
        json.dump(info, f, indent=4)
