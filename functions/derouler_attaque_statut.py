def Statut(pokemon_defenseur, Attaque) :
    if pokemon_defenseur.statut != None :
        print("Echec, le pokemon a déjà un statut")
        print(pokemon_defenseur.statut)
    else :
        pokemon_defenseur.statut = Attaque.statut

    return pokemon_defenseur
