class Trainer:
    pokemon = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon in Trainer.pokemon:
            return "This pokemon is already caught"
        Trainer.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = [p for p in Trainer.pokemon if p.name == pokemon_name][0]
            Trainer.pokemon.remove(pokemon)
            return f"You have released {pokemon_name}"
        except IndexError:
            return "Pokemon is not caught"


    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            result += f'- {p.pokemon_details()}\n'
        return result