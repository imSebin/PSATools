from bs4 import BeautifulSoup
import json, requests, pprint

class GenerateExpansionFrame:
    def __init__(self, url, language):
        self.url = url
        self.language = language
        poke_html = requests.get(f'{self.url}/sets').text
        self.soup = BeautifulSoup(poke_html, 'lxml')

        self.data = {}
        self.output_file = "./res/data/identifiers/series.json"


    def parse_series(self):
        series = {}
        series_box = self.soup.find_all('h1', class_='icon set')
        series_content_box = self.soup.find_all('div', class_=f'content buttonlisting {self.language}')
        assert len(series_box) == len(series_content_box)
        num_series = len(series_box)
        for i in range(num_series):
            dct = {}
            for expansion in series_content_box[i].find_all('a', class_='button'):
                dct[expansion.text] = {
                    "url": f'{self.url}{expansion["href"]}',
                    "splash": expansion.find_all('img')[0]['src'],
                    "symbol": expansion.find_all('img')[1]['src'] if len(expansion.find_all('img')) > 1 else None
                }
            data = {
                "logo": series_box[i].find('img')['src'],
                "expansions": dict(reversed(dct.items()))
            }
            series[series_box[i].text] = data
        self.data = dict(reversed(series.items()))

    def export(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.data, f, indent=4)


if __name__ == '__main__':
    LANG = {
        "ENG": {"subdir": 'www', "class": 'english'},
        "JP": {"subdir": 'jp', "class": 'japanese'}
    }

    app = GenerateExpansionFrame(f'https://{LANG["ENG"]["subdir"]}.pokellector.com', LANG["ENG"]["class"])
    app.parse_series()
    # pprint.pprint(app.data, sort_dicts=False)
    app.export()
