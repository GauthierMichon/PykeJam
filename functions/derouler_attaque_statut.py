from functions.attaque_miss_or_work import MissWork


def Statut(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if pokemon_defenseur.statut != None :
            print("Echec, le pokemon a déjà un statut")
            print(pokemon_defenseur.statut)
        elif pokemon_defenseur.clone == True :
            print("Il y a un clone")
        else :
            pokemon_defenseur.statut = Attaque.statut

    return pokemon_defenseur
