from math import ceil

from functions.attaque_miss_or_work import MissWork

# Fonction qui gère les attaques de soin
def Heal(pokemon_attaquant, Attaque) :
    # Si l'attaque réussit
    if MissWork(pokemon_attaquant, Attaque) :
        # On calcule les PV soignés
        recupPV = ceil(Attaque.PVHeal * pokemon_attaquant.PVMax / 100)
        if recupPV + pokemon_attaquant.PV > pokemon_attaquant.PVMax :
            pokemon_attaquant.PV = pokemon_attaquant.PVMax
        else :
            pokemon_attaquant.PV = pokemon_attaquant.PV + recupPV

    return pokemon_attaquant