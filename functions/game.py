from copy import deepcopy
from classes.dresseur import Dresseur
from functions.choose_random_num import rand
from functions.combat import combat
from random import randint
from functions.initiation import init


def game() :
    
    pokemonList = init()

    pseudo      = input('Quel est votre pseudo de dresseur ? ')

    pokemon_1   = input('Id de votre premier pokemon : ')
    pokemon_2   = input('Id de votre deuxième pokemon : ')
    pokemon_3   = input('Id de votre troisième pokemon : ')
    pokemon_4   = input('Id de votre quatrième pokemon : ')
    pokemon_5   = input('Id de votre cinquième pokemon : ')
    pokemon_6   = input('Id de votre dernier pokemon : ')

    pokemon_1 = deepcopy(pokemonList[int(pokemon_1) - 1])
    pokemon_2 = deepcopy(pokemonList[int(pokemon_2) - 1])
    pokemon_3 = deepcopy(pokemonList[int(pokemon_3) - 1])
    pokemon_4 = deepcopy(pokemonList[int(pokemon_4) - 1])
    pokemon_5 = deepcopy(pokemonList[int(pokemon_5) - 1])
    pokemon_6 = deepcopy(pokemonList[int(pokemon_6) - 1])

    adversaire = 'quentin'

    adversaire_1 = deepcopy(pokemonList[randint(0, 77)])
    adversaire_2 = deepcopy(pokemonList[randint(0, 77)])    
    adversaire_3 = deepcopy(pokemonList[randint(0, 77)]) 
    adversaire_4 = deepcopy(pokemonList[randint(0, 77)])  
    adversaire_5 = deepcopy(pokemonList[randint(0, 77)])
    adversaire_6 = deepcopy(pokemonList[randint(0, 77)])

    allPokemonChoose = [pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6, adversaire_1, adversaire_2, adversaire_3, adversaire_4, adversaire_5, adversaire_6]
    for i in range(len(allPokemonChoose)) :
        if rand(1, 100) == 1 :
            allPokemonChoose[i].sprite += "_shiny"
            allPokemonChoose[i].spriteDos += "_shiny"
            allPokemonChoose[i].PV *= 1.10
            allPokemonChoose[i].PVMax *= 1.10
            allPokemonChoose[i].Att *= 1.10
            allPokemonChoose[i].AttInit *= 1.10
            allPokemonChoose[i].Def *= 1.10
            allPokemonChoose[i].DefInit *= 1.10
            allPokemonChoose[i].AttSpe *= 1.10
            allPokemonChoose[i].AttSpeInit *= 1.10
            allPokemonChoose[i].DefSpe *= 1.10
            allPokemonChoose[i].DefSpeInit *= 1.10
            allPokemonChoose[i].Speed *= 1.10
            allPokemonChoose[i].SpeedInit *= 1.10

    player = Dresseur(pseudo, [pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6], "player")
    adversaire = Dresseur(adversaire, [adversaire_1, adversaire_2, adversaire_3, adversaire_4, adversaire_5, adversaire_6], "adversaire")
        
    
    combat(player, adversaire)
