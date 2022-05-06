from graph.write_info import WriteInfo


def ActionItemBuff(dresseur, item, pokemonActualPlayerNumber) :

    if item.StatBuff != "accuracy" :
        initStat = getattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Init"))
        nbBuffStat = getattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Buff"))

        if nbBuffStat == 6 :
            print("Vous avez déjà le maximum de buff sur ce stat !")
        else :
            print("stat boosté !")
            setattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff + "Buff"), nbBuffStat + 1)
            setattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff), initStat * (nbBuffStat + 1))
    else :
        nbBuffStat = getattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff))
        if nbBuffStat == 6 :
            print("Vous avez déjà le maximum de buff sur ce stat !")
        else :
            setattr(dresseur.pokemons[pokemonActualPlayerNumber], (item.StatBuff), (nbBuffStat + 1))

    statText, buffText = TextBuff(item)
    WriteInfo(statText + dresseur.pokemons[pokemonActualPlayerNumber].name + buffText)

    return dresseur

def TextBuff(item) :
    statText = ""
    buffText = ""

    if item.StatBuff == "Att" :
        statText = "L'Attaque de "
    elif item.StatBuff == "Def" :
        statText = "La Défense de "
    elif item.StatBuff == "AttSpe" :
        statText = "L'Attaque Spéciale de "
    elif item.StatBuff == "DefSpe" :
        statText = "La Défense Spéciale de "
    elif item.StatBuff == "Speed" :
        statText = "La Vitesse de "
    else :
        statText = "La Précision de "

    buffText = " augmente !"