from math import ceil
import random
from classes.attaque_autre import AttaqueAutre
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_statut import AttaqueStatut
from functions.attaque_miss_or_work import MissWork
from functions.choose_random_num import rand
from functions.climat_attaque_offensive import Climat
from functions.critique import isCrit

from functions.derouler_attaque_offensive import Offensive
from functions.derouler_attaque_statut import Statut
from functions.derouler_attaque_heal import Heal
from functions.derouler_attaque_buff import Buff
from functions.initiation import initAttaque
import functions.derouler_attaque_autre as other
from functions.table_types import TableType


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

def BlablaDodo(pokemon_attaquant, pokemon_defenseur, terrain) :
    attaqueList = initAttaque()
    Attaque = attaqueList[random.randrange(0, len(attaqueList))]
    
    if type(Attaque) is AttaqueOffensive :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain


    elif type(Attaque) is AttaqueBuff :
        pokemon_attaquant = Buff(pokemon_attaquant, Attaque)
        return pokemon_attaquant, pokemon_defenseur, terrain


    elif type(Attaque) is AttaqueClimat :
        terrain = Climat(Attaque, terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain


    elif type(Attaque) is AttaqueHeal :
        pokemon_attaquant = Heal(pokemon_attaquant, Attaque)
        return pokemon_attaquant, pokemon_defenseur, terrain


    elif type(Attaque) is AttaqueStatut :        
        pokemon_defenseur = Statut(pokemon_defenseur, Attaque)
        return pokemon_attaquant, pokemon_defenseur, terrain


    elif type(Attaque) is AttaqueAutre :
        other.Autres(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain

def BouleRoc(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 25
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    nombreCoup = 0
    rand = random.randrange(0,101)
    if rand < 38 :
        nombreCoup = 2
    elif rand < 76 :
        nombreCoup = 3
    elif rand < 89 :
        nombreCoup = 4
    else :
        nombreCoup = 5

    print("Avant :", pokemon_defenseur.PV)
    for i in range(nombreCoup) :
        print("Coup ", i)
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    print("Après :", pokemon_defenseur.PV)


    return pokemon_defenseur

def BouteFeu(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 25
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 1
    Attaque.probaEffect = 10
    Attaque.EffectName = "Brûlure"

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    pokemon_attaquant.PV = ceil((PVAvantAttaque - pokemon_defenseur.PV) / 3)

    return pokemon_attaquant, pokemon_defenseur

def CasseBrique(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 75
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def ChocPsy(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 100
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if booleanAttaque :
        degats = (100 * 0.4 + 2) * pokemon_attaquant.AttSpe * Attaque.puissance
        degats = degats / (pokemon_defenseur.Def * 50) + 2

        #STAB
        if Attaque.Type == pokemon_attaquant.Type or Attaque.Type == pokemon_attaquant.Type2 :
            degats *= 1.5

        #Efficacité type
        eff = TableType(Attaque.Type, pokemon_defenseur.Type, pokemon_defenseur.Type2)
        if eff == 0 :
            print("inefficace")
        elif eff == 0.25 or eff == 0.5 :
            print("peu efficace")
        elif eff == 1 :
            print("efficace")
        elif eff >= 2 :
            print("super efficace")
        else : 
            print("problème efficacité")

        degats *= eff

        #Crit
        if isCrit() :
            print("Coup Critique")
            degats *= 2

        #Climat
        degats *= Climat(terrain, Attaque.Type)


        #Random num entre 0.85 et 1
        degats *= (rand(85, 100) / 100)

        pokemon_defenseur.PV -= ceil(degats)

    else :
        print("miss")
    
    return pokemon_defenseur
