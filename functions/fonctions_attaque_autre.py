from math import ceil

from functions.derouler_attaque_offensive import Offensive


def Abri(pokemon_attaquant) :
    pokemon_attaquant.abri = True
    return pokemon_attaquant

def AntiBrume(terrain) :
    terrain.climat = None
    return terrain

def Balance(pokemon_attaquant, pokemon_defenseur) :
    newPV = ceil((pokemon_attaquant.PV + pokemon_defenseur.PV) / 2)
    if pokemon_attaquant.PVMax > newPV :
        pokemon_attaquant.PV = pokemon_attaquant.PVMax
    else :
        pokemon_attaquant.PV = newPV

    if pokemon_defenseur.PVMax > newPV :
        pokemon_defenseur.PV = pokemon_defenseur.PVMax
    else :
        pokemon_defenseur.PV = newPV

    return pokemon_attaquant, pokemon_defenseur

def BallMeteo(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    if terrain.climat is None :
        Attaque.Type = "Normal"
        Attaque.puissance = 50

    if terrain.climat == "Soleil" :
        Attaque.Type = "Feu"
        Attaque.puissance = 100

    if terrain.climat == "Pluie" :
        Attaque.Type = "Eau"
        Attaque.puissance = 100

    if terrain.climat == "Tempête de sable" :
        Attaque.Type = "Roche"
        Attaque.puissance = 100

    if terrain.climat == "Grêle" :
        Attaque.Type = "Glace"
        Attaque.puissance = 100

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    return pokemon_defenseur