# PSATools
Pokemon Trading Card Game & Graded Cards : Information Warehouse + Management System

## Data Formatting Rules and Guidelines:

### Sample Entry:
```
"base holo": {
    "expansion": "Pokemon EX Ruby & Sapphire",
    "language": "English",
    "released": "2003",
    "number": "7/109",
    "rarity": "Rare Holo",
    "psa_10_pop": "18",
    "cert_number": "25032566",
    "obtained": "False",
    "authenticator": "N/A",
    "grade": "N/A",
    "img": "100.jpg",
    "id": "1.0.0"
}
```

### Primary Key:
- All key items must be separated by spaces
- First key item is the short form of the card's release (e.g. base, steam-siege, etc.)
- Second key item is the card's holo-type (e.g. holo, cosmos-holo, etc.)
- Following key items can be any specialties of the card (e.g. world-championships, promo, etc.)

### Expansion:
- The expansion is the ARTWORK's original expansion (e.g. Pokémon EX Ruby & Sapphire)
- Any artwork that is different but based on another expansion will encompass said expansion as its own

### Certification Number:
- If the card is obtained, then use its certification number
- If not, use a sample PSA 10's image available on the PSA database's number
- If neither option is available (i.e. card is too rare) use "UNRECOVERABLE" until found

### Image:
- It should contain the filename for the corresponding image
- EVERY entry should have its own image, even if some are absolutely identical and only differentiable through non-visual details

### ID:
- Formatting:

| Digits | Bit 1: Pokemon |      Bit 2: Expansion      |
|-------:|:--------------:|:--------------------------:|
|      1 |   Gardevoir    |     EX Ruby & Sapphire     |
|      2 |    Sylveon     |        EX Sandstorm        |
|      3 |    Vaporeon    |         EX Dragon          |
|      4 |    Glaceon     | EX Team Magma vs Team Aqua |
|      5 |    Umbreon     |     EX Hidden Legends      |
|      6 |     Espeon     |   EX FireRed & LeafGreen   |
|      7 |    Leafeon     |   EX Team Rocket Returns   |
|      8 |    Flareon     |         EX Deoxys          |
|      9 |    Jolteon     |         EX Emerald         |
|     10 |     Eevee      |      EX Unseen Forces      |
|     11 |    Meloetta    |      EX Delta Species      |
|     12 |   Lilligant    |      EX Legend Maker       |
|     13 |    Milotic     |                            |
|     14 |    Lopunny     |                            |
|     15 |    Tsareena    |                            |
|     16 |  Meowscarada   |                            |
|     17 |    Roserade    |                            |
|     18 |   Pheromosa    |                            |
|     19 |    Roserade    |                            |
|     20 |     Celebi     |                            |
|     21 |   Primarina    |                            |
|     22 |    Diancie     |                            |
|     23 |   Hatterene    |                            |
|     24 |    Alcremie    |                            |
|     25 |    Magearna    |                            |
|     26 |    Lurantis    |                            |
|     27 |    Fennekin    |                            |
|     28 |   Gothitelle   |                            |
|     29 |    Zoroark     |                            |
|     30 |    Cinccino    |                            |
|     31 |   Serperior    |                            |
|     32 |   Cresselia    |                            |
|     33 |   Frosslass    |                            |
|     34 |    Alteria     |                            |
|     35 |     Mawile     |                            |
|     36 |    Salazzle    |                            |


