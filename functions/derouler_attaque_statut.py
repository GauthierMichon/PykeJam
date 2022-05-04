from functions.attaque_miss_or_work import MissWork
from graph.write_info import WriteInfo

# Fonction qui gère les attaques de statut
def Statut(pokemon_attaquant, pokemon_defenseur, Attaque) :
    # Si l'attaque réussit
    if MissWork(pokemon_attaquant, Attaque) :
        # Si le pokemon defenseur a déjà un statut
        if pokemon_defenseur.statut != None :
            WriteInfo(pokemon_defenseur.name + " a déjà un statut !")

            print("Echec, le pokemon a déjà un statut")
            print(pokemon_defenseur.statut)
        # Si le pokemon defenseur est caché derrière un clone
        elif pokemon_defenseur.clone == True :
            WriteInfo(pokemon_defenseur.name + " est caché derrière un clone !")
            print("Il y a un clone")
        # Sinon
        else :
            WriteInfo(pokemon_defenseur.name + " est affecté par " + Attaque.statut + " !")
            pokemon_defenseur.statut = Attaque.statut

    return pokemon_defenseur
