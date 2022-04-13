from math import ceil


def BrulurePoison(dresseur, pokemonActualNumber) :
    if dresseur.pokemons[pokemonActualNumber].statut == "Brûlure" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 16)

    if dresseur.pokemons[pokemonActualNumber].statut == "Empoisonnement" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)

    if dresseur.pokemons[pokemonActualNumber].PV <= 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0
        if pokemonActualNumber < 5 :
                actionNum = pokemonActualNumber + 1
                print("vous envoyé {}".format(dresseur.pokemons[actionNum].name))

    return dresseur, pokemonActualNumber