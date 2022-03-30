from math import ceil
import random
from tkinter import E
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
    Attaque.puissance = 120
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

        if pokemon_defenseur.clone == False :
            pokemon_defenseur.PV -= ceil(degats)
        else :
            pokemon_defenseur.clonePV -= ceil(degats)
            if pokemon_defenseur.clonePV <= 0 :
                pokemon_defenseur.clone = False
                pokemon_defenseur.clonePV = None

    else :
        print("miss")
    
    return pokemon_defenseur

def Clairvoyance(pokemon_attaquant) :
    if pokemon_attaquant.accuracy < 0 :
        pokemon_attaquant.accuracy = 0
    pokemon_attaquant.accuracy += 2

    return pokemon_attaquant

def Clonage(pokemon_attaquant) :
    if pokemon_attaquant.PV > ceil(pokemon_attaquant.PV / 4) :
        pokemon_attaquant.PV -= ceil(pokemon_attaquant.PV / 4)
        pokemon_attaquant.clone = True
        pokemon_attaquant.clonePV = ceil(pokemon_attaquant.PV / 4)
    else :
        print("Clonage a échoué")

def CloseCombat(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    if pokemon_attaquant.DefBuff > -6 :
        pokemon_attaquant.DefBuff -= 1
    if pokemon_attaquant.DefSpeBuff > -6 :
        pokemon_attaquant.DefSpeBuff -= 1

    return pokemon_attaquant, pokemon_defenseur

def Colere(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    input("Use Colere")

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if dresseurPokemonAttaquant.actionOblig == None :
        dresseurPokemonAttaquant.actionOblig = [1, numAttaque]
        dresseurPokemonAttaquant.actionObligNbTour = rand(1, 2)
    elif dresseurPokemonAttaquant.actionObligNbTour == 1 :
        dresseurPokemonAttaquant.actionOblig = None
        dresseurPokemonAttaquant.actionObligNbTour = None
        pokemon_attaquant.confusion = True
    else :
        dresseurPokemonAttaquant.actionObligNbTour -= 1

    print(pokemon_defenseur.PV)

    return pokemon_attaquant, pokemon_defenseur, dresseurPokemonAttaquant

def Conversion(pokemon_attaquant) :
    pokemon_attaquant.Type = pokemon_attaquant.Attaques[0].Type
    print(pokemon_attaquant.Type)
    return pokemon_attaquant

def Damocles(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    pokemon_attaquant.PV = ceil((PVAvantAttaque - pokemon_defenseur.PV) / 3)

    return pokemon_attaquant, pokemon_defenseur

def DracoMeteore(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 130
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    
    pokemon_attaquant.AttSpeBuff -= 2
    if pokemon_attaquant.AttSpeBuff < -6 :
        pokemon_attaquant.AttSpeBuff = -6

    return pokemon_attaquant, pokemon_defenseur

def EclairFou(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 90
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    pokemon_attaquant.PV = ceil((PVAvantAttaque - pokemon_defenseur.PV) / 4)

    return pokemon_attaquant, pokemon_defenseur

def Effort(pokemon_attaquant, pokemon_defenseur) :
    if pokemon_defenseur.PV > pokemon_attaquant.PV :
        pokemon_defenseur.PV = pokemon_attaquant.PV
    else :
        print("PV de l'adversaire trop bas")

    return pokemon_defenseur

def Explosion(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 250
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    pokemon_attaquant.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def Facade(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    if pokemon_attaquant.statut == "Brûlure" :
        Attaque.puissance = 280
    elif pokemon_attaquant.statut == "Paralysie" and pokemon_attaquant.statut == "Empoisonnement"  :
        Attaque.puissance = 140
    else :
        Attaque.puissance = 70
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def FrappeAtlas(pokemon_defenseur) :
    pokemon_defenseur.PV -= 100
    return pokemon_defenseur

def GlasDeSoin(dresseurPokemonAttaquant) :
    for i in range(len(dresseurPokemonAttaquant.pokemons)) :
        dresseurPokemonAttaquant.pokemons[i].statut = None

def LanceSoleil(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque) :
    Attaque.puissance = 120
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    if dresseurPokemonAttaquant.actionOblig == None and terrain.climat != "Soleil" :
        input("Se charge")
        dresseurPokemonAttaquant.actionOblig = [1, numAttaque]
        dresseurPokemonAttaquant.actionObligNbTour = 1
    elif terrain.climat == "Soleil" :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif dresseurPokemonAttaquant.actionObligNbTour == 1 :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
        dresseurPokemonAttaquant.actionOblig = None
        dresseurPokemonAttaquant.actionObligNbTour = None

    return pokemon_defenseur, dresseurPokemonAttaquant

def Malediction(pokemon_attaquant, pokemon_defenseur) :
    if pokemon_attaquant.Type == "Spectre" or pokemon_attaquant.Type2 == "Spectre" :
        pokemon_attaquant.PV -= ceil(pokemon_attaquant.PVMax / 2)
        pokemon_defenseur.maudit = True

    else :
        if pokemon_attaquant.AttBuff < 6 :
            pokemon_attaquant.AttBuff += 1
        if pokemon_attaquant.DefBuff < 6 :
            pokemon_attaquant.DefBuff += 1
        if pokemon_attaquant.SpeedBuff > -6 :
            pokemon_attaquant.SpeedBuff -= 1

    return pokemon_attaquant, pokemon_defenseur

def Megaphone(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 100
    Attaque.physique = 1
    Attaque.special = 0
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if pokemon_attaquant.statut == "Brûlure" :
        pokemon_attaquant.Att = pokemon_attaquant.Att / 2

    if booleanAttaque :
        if Attaque.physique == 1 :
            degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * Attaque.puissance
            degats = degats / (pokemon_defenseur.Def * 50) + 2
        elif Attaque.special == 1 :
            degats = (100 * 0.4 + 2) * pokemon_attaquant.AttSpe * Attaque.puissance
            degats = degats / (pokemon_defenseur.DefSpe * 50) + 2

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

def NoeudHerbe(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    if pokemon_defenseur.Poids <= 10 :
        Attaque.puissance = 20
    elif pokemon_defenseur.Poids <= 25 :
        Attaque.puissance = 40
    elif pokemon_defenseur.Poids <= 50 :
        Attaque.puissance = 60
    elif pokemon_defenseur.Poids <= 100 :
        Attaque.puissance = 80
    elif pokemon_defenseur.Poids <= 200 :
        Attaque.puissance = 100
    else :
        Attaque.puissance = 120

    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def Picots(dresseurPokemonAttaquant, terrain) :
    if dresseurPokemonAttaquant.person == "player" :
        toChange = "Picots"
    else :
        toChange = "PicotsAdverse"
    
    initValue = getattr(terrain, toChange)


    if getattr(terrain, toChange) == None :
        setattr(terrain, toChange, 1)
    elif getattr(terrain, toChange) < 3 :
        setattr(terrain, toChange, initValue + 1)
    else :
        print("trop de picots")

    return terrain

def PicsToxik(dresseurPokemonAttaquant, terrain) :
    if dresseurPokemonAttaquant.person == "player" :
        toChange = "PicsToxik"
    else :
        toChange = "PicsToxikAdverse"
    
    if getattr(terrain, toChange) == None :
        setattr(terrain, toChange, 1)
    else :
        print("déjà des Pics Toxik")

    return terrain




