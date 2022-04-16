from functions.attaque_miss_or_work import MissWork

# Fonction gère les attaques climatiques
def Climat(pokemon_attaquant, Attaque, terrain) :
    # Si l'attaque réussit
    if MissWork(pokemon_attaquant, Attaque) :
        # Change le climat
        terrain.climat = Attaque.climat
    
    return terrain