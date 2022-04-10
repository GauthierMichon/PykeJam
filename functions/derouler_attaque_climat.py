from functions.attaque_miss_or_work import MissWork


def Climat(pokemon_attaquant, Attaque, terrain) :
    if MissWork(pokemon_attaquant, Attaque) :

        terrain.climat = Attaque.climat
    
    return terrain