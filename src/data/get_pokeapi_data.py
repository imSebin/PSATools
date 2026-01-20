import requests, json

class GetPokeAPIData:
    @staticmethod
    def get_all_pokemon():
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        params = {'limit': 2000}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data['results']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

if __name__ == "__main__":
    MAX_POKEMON = 1025
    info = {}

    app = GetPokeAPIData()
    pokemon = app.get_all_pokemon()
    for i in range(MAX_POKEMON):
        info[str(i)] = {
            "name": pokemon[i]['name'],
            "url": pokemon[i]['url']
        }
    with open('res/data/identifiers/pokemon.json', 'w') as f:
        json.dump(info, f, indent=4)