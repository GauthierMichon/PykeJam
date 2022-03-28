from functions.boost_value import boost


def Buff(pokemon_attaquant, Attaque) :

    for i in range(len(Attaque.statBuff)) :
        # On récupère la statistique de base
        initStat = getattr(pokemon_attaquant, (Attaque.statBuff[i] + "Init"))
        # On récupère le nombre de buff actuel de la statistique
        buff = getattr(pokemon_attaquant, (Attaque.statBuff[i] + "Buff"))
        # On ajoute le nombre de buff qu'apporte l'attaque
        buff += Attaque.nombreBuff[i]
        # On vérifie si le nombre de buff ne dépasse pas 6 ou n'est pas inférieur à -6
        if buff > 6 :
            buff = 6
        elif buff < -6 :
            buff = -6
        # On recalcul la statistique
        newStat = initStat * boost(buff)
        # On set les nouvelles valeurs
        setattr(pokemon_attaquant, Attaque.statBuff[i], newStat)
        setattr(pokemon_attaquant, (Attaque.statBuff[i] + "Buff"), buff)


    return pokemon_attaquant