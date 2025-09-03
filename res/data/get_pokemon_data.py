import pokebase as pb
from tqdm import tqdm
import time
import json

class pokeAPI_handler:
    def __init__(self):
        self.all_pokemon = pb.APIResourceList('pokemon')
        self.pokemon_data = {}

    def fill_data(self):
        count = 0
        for p in tqdm(self.all_pokemon, desc="Fetching Pokémon data"):
            if count >= 25:
                dct = self.import_json("database.json")
                print(list(dct.keys()))
                self.pokemon_data.update(dct)
                self.export_json("database.json")
                self.pokemon_data = {}
                count = 0
            else:
                count += 1
            try:
                poke = pb.pokemon(p['name'])  # Base info
                species = pb.pokemon_species(poke.id)  # Species info
                evo_chain = pb.evolution_chain(species.evolution_chain.id) # Evolution info

                # Build evolution list
                evolution_chain = self.extract_evolution_chain(evo_chain.chain)

                # Populate entry
                self.pokemon_data[p['name']] = {
                    'pokedex_number': species.id,
                    'generation': species.generation.name,
                    'evolution_chain': evolution_chain,
                    'base_stats': self.get_base_stats(poke),
                    'types': [t.type.name for t in poke.types],
                    'height': poke.height,
                    'weight': poke.weight,
                    'sprites': {}
                }
                # self.export_json(f"test\\{p['name']}.json")
                time.sleep(0.1)  # Respect rate limits

            except Exception as e:
                print(f"Error fetching {p['name']}: {e}")
                continue

    def extract_evolution_chain(self, chain_node):
        result = [chain_node.species.name]
        for evo in chain_node.evolves_to:
            result.extend(self.extract_evolution_chain(evo))
        return result

    def get_base_stats(self, poke):
        stats = {}
        for stat in poke.stats:
            stats[stat.stat.name] = stat.base_stat
        return stats

    def get_all_sprites(self, poke):
        pass

    def import_json(self, filename):
        with open(filename, "r") as f:
            return json.load(f)

    def export_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.pokemon_data, f, indent=2)


if __name__ == '__main__':
    API_class = pokeAPI_handler()
    API_class.fill_data()