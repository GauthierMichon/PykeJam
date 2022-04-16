def ActionItemHeal(dresseur, item) :
    
    pokemonNum = ChoosePokemonToHeal(dresseur)
    dresseur.pokemons[pokemonNum].PV += item.PVHeal
    if dresseur.pokemons[pokemonNum].PV > dresseur.pokemons[pokemonNum].PVMax :
        dresseur.pokemons[pokemonNum].PV = dresseur.pokemons[pokemonNum].PVMax

    return dresseur

def ChoosePokemonToHeal(dresseur) :
    pokemonNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
        dresseur.pokemons[0].name,
        dresseur.pokemons[1].name,
        dresseur.pokemons[2].name,
        dresseur.pokemons[3].name,
        dresseur.pokemons[4].name,
        dresseur.pokemons[5].name,
    ))
    pokemonNum = int(pokemonNum) - 1

    return pokemonNum