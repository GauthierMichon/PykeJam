def ActionItemBuff(dresseur, item, pokemonActualPlayerNumber) :

    initStat = getattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Init"))
    nbBuffStat = getattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Buff"))

    if nbBuffStat == 6 :
        print("Vous avez déjà le maximum de buff sur ce stat !")
    else :
        print("stat boosté !")
        setattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Buff"), nbBuffStat + 1)
        setattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff), initStat * (nbBuffStat + 1))



    return dresseur