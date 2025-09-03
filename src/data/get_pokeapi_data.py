import requests

class get_pokeapi_data:
    @staticmethod
    def get_all_pokemon_names():
        """Fetches and returns a list of all Pokémon names from PokeAPI."""
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        params = {'limit': 2000}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            data = response.json()

            pokemon_names = [item['name'] for item in data['results']]
            return pokemon_names
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

if __name__ == "__main__":
    test = get_pokeapi_data()
    names = test.get_all_pokemon_names()
    if names:
        print("List of all Pokémon names:")
        for name in names:
            print(name)
        print(len(names))
    else:
        print("Could not retrieve Pokémon names.")