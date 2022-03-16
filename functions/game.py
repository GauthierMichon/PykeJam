from functions.combat import combat
from functions.initiation import init


def game() :
    
    pokemonList = init()

    pseudo      = input('Quel est votre pseudo de dresseur ?')

    pokemon_1   = input('Id de votre premier pokemon : ')
    pokemon_2   = input('Id de votre deuxième pokemon : ')
    pokemon_3   = input('Id de votre troisième pokemon : ')
    pokemon_4   = input('Id de votre quatrième pokemon : ')
    pokemon_5   = input('Id de votre cinquième pokemon : ')
    pokemon_6   = input('Id de votre dernier pokemon : ')

    pokemon_1 = pokemonList[int(pokemon_1) - 1]
    pokemon_2 = pokemonList[int(pokemon_2) - 1]
    pokemon_3 = pokemonList[int(pokemon_3) - 1]
    pokemon_4 = pokemonList[int(pokemon_4) - 1]
    pokemon_5 = pokemonList[int(pokemon_5) - 1]
    pokemon_6 = pokemonList[int(pokemon_6) - 1]


    combat()

