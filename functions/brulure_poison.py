from math import ceil
from functions.choose_pokemon_change import ChoosePokemon

from functions.switch import Switch


def BrulurePoison(dresseur, pokemonActualNumber) :
    if dresseur.pokemons[pokemonActualNumber].statut == "Brûlure" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 16)

    if dresseur.pokemons[pokemonActualNumber].statut == "Empoisonnement" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)

    if dresseur.pokemons[pokemonActualNumber].PV <= 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0
        if pokemonActualNumber < 5 and dresseur.person == "adversaire" :
            dresseur = Switch(dresseur, pokemonActualNumber)
            pokemonActualNumber = pokemonActualNumber + 1
            print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))
        else :
            dresseur = Switch(dresseur, pokemonActualNumber)
            pokemonActualNumber = ChoosePokemon(dresseur, pokemonActualNumber)
            print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))
    return dresseur, pokemonActualNumber