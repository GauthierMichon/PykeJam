from math import ceil


def ActionItemRes(dresseur, item) :

    pokemonNum = ChoosePokemonToRes(dresseur)
    dresseur.pokemons[pokemonNum].PV = ceil(dresseur.pokemons[pokemonNum].PVMax * item.PV)

    return dresseur




def ChoosePokemonToRes(dresseur) :
    pokemonNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
        dresseur.pokemons[0].name,
        dresseur.pokemons[1].name,
        dresseur.pokemons[2].name,
        dresseur.pokemons[3].name,
        dresseur.pokemons[4].name,
        dresseur.pokemons[5].name,
    ))
    pokemonNum = int(pokemonNum) - 1
    if dresseur.pokemons[pokemonNum].PV > 0 :
        print("Ce pokemon n'est pas K.O.")
        return ChoosePokemonToRes(dresseur)
    

    return pokemonNum