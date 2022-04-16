# Fonction qui permet de calculer le coefficient multiplicateur de l'attaque en fonction du climat
def Climat(climat, attaqueType) :
    if climat == "Soleil" :
        if attaqueType == "Feu" :
            return 1.5
        elif attaqueType == "Eau" :
            return 0.5

    elif climat == "Pluie" :
        if attaqueType == "Eau" :
            return 1.5
        elif attaqueType == "Feu" :
            return 0.5

    else :
        return 1    