from functions.attaque_miss_or_work import MissWork

# Fonction qui gère les attaques de statut
def Statut(pokemon_attaquant, pokemon_defenseur, Attaque) :
    # Si l'attaque réussit
    if MissWork(pokemon_attaquant, Attaque) :
        # Si le pokemon defenseur a déjà un statut
        if pokemon_defenseur.statut != None :
            print("Echec, le pokemon a déjà un statut")
            print(pokemon_defenseur.statut)
        # Si le pokemon defenseur est caché derrière un clone
        elif pokemon_defenseur.clone == True :
            print("Il y a un clone")
        # Sinon
        else :
            pokemon_defenseur.statut = Attaque.statut

    return pokemon_defenseur
