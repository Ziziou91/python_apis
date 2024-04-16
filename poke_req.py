import requests


def get_pokemon() -> dict:
    """Sends a get request to pokeapi.co/api/v2/pokemon and returns valid pokemon dict."""
    # Choose your Pokémon to battle with
    poke_req = {}

    valid_pokemon = False
    while not valid_pokemon:
        # Get a Pokémon from api.
        pokemon_name = input("Please enter a pokemon name: ").lower()
        poke_req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

        if poke_req.status_code == 200:
            valid_pokemon = True
        elif poke_req.status_code == 404:
            print(f"{'='*10}ERROR! {pokemon_name} is not a valid pokemon{'='*10}")
            print(f"API Status code: 404")
        elif poke_req.status_code == 500:
            print("API currently unavailable.")
            print(f"API Status code: 404")
        else:
            print(poke_req.status_code)

    return poke_req.json()


def get_pokemon_stats(pokemon: dict) -> dict:
    pokemon_stats = {
        "name": pokemon["name"]
    }
    for stat in pokemon["stats"]:
        # Get stat_name and stat_value
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        # Add key and value to pokemon_stats dict.
        pokemon_stats[stat_name] = stat_value

    return pokemon_stats
