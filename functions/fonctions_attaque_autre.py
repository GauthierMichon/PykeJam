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
from functions.boost_value import boost
from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.climat_attaque_offensive import Climat
from functions.critique import isCrit

from functions.derouler_attaque_offensive import Offensive
from functions.derouler_attaque_statut import Statut
from functions.derouler_attaque_heal import Heal
from functions.derouler_attaque_buff import Buff
from functions.initiation import initAttaque
import functions.derouler_attaque_autre as other
from functions.switch_adversaire import ChangeAdversaire
from functions.table_types import TableType
from graph.write_info import WriteInfo
from graph.change_pokemon_graph import ChangePokemonGraph


def Abri(pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :
        WriteInfo(pokemon_attaquant.name + " s'abrite !")
        pokemon_attaquant.abri = True
    
    return pokemon_attaquant

def AntiBrume(pokemon_attaquant, Attaque, terrain) :
    if MissWork(pokemon_attaquant, Attaque) :
        WriteInfo("Le terrain est nettoyé !")
        terrain.climat              = None
        terrain.Picots              = None
        terrain.PicsToxik           = None
        terrain.PiegeDeRoc          = None
        terrain.Vampigraine         = None
        terrain.PicotsAdverse       = None
        terrain.PicsToxikAdverse    = None
        terrain.PiegeDeRocAdverse   = None
        terrain.VampigraineAdverse  = None
    return terrain

def Balance(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :
        WriteInfo("Les PV des pokemons s'équilibre !")
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
    if pokemon_attaquant.statut == "Sommeil" :
        attaqueList = initAttaque()
        Attaque = attaqueList[random.randrange(0, len(attaqueList))]

        WriteInfo(pokemon_attaquant.name + " va lancer une attaque aléatoire !")
        WriteInfo(pokemon_attaquant.name + " utilise " + Attaque.name + " !")

        
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

    else :
        WriteInfo(pokemon_attaquant.name + " n'est pas endormi !")
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
        print("Coup ", i + 1)
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    print("Après :", pokemon_defenseur.PV)


    return pokemon_defenseur

def BouteFeu(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 1
    Attaque.probaEffect = 10

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    
    WriteInfo(pokemon_attaquant.name + " est bléssé par le contrecoup !")

    pokemon_attaquant.PV -= ceil((PVAvantAttaque - pokemon_defenseur.PV) / 3)
    if pokemon_attaquant.PV < 0 :
        pokemon_attaquant.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def CasseBrique(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 75
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def ChangeEclair(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseur, pokemonActuelNum) :
    Attaque.puissance = 70
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    WriteInfo(pokemon_attaquant.name + " va être remplacé par un autre pokémon !")

    if dresseur.person == "player" :
        newPokemonActuelNum = ChoosePokemon(dresseur, pokemonActuelNum)
    else :
        newPokemonActuelNum = ChangeAdversaire(dresseur, pokemonActuelNum)

    return pokemon_defenseur, newPokemonActuelNum

def ChocPsy(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 100
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if pokemon_defenseur.abri :
        WriteInfo(pokemon_defenseur.name + " se protège, l'attaque est sans effet.")
        booleanAttaque = False
        print("Le Pokémon adverse se protège, l'attaque est sans effet.")

    elif booleanAttaque :
        degats = (100 * 0.4 + 2) * pokemon_attaquant.AttSpe * Attaque.puissance
        degats = degats / (pokemon_defenseur.Def * 50) + 2

        #STAB
        if Attaque.Type == pokemon_attaquant.Type or Attaque.Type == pokemon_attaquant.Type2 :
            degats *= 1.5

        #Efficacité type
        eff = TableType(Attaque.Type, pokemon_defenseur.Type, pokemon_defenseur.Type2)
        if eff == 0 :
            WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
            print("inefficace")
        elif eff == 0.25 or eff == 0.5 :
            WriteInfo("Ce n'est pas très efficace !")
            print("peu efficace")
        elif eff == 1 :
            print("efficace")
        elif eff >= 2 :
            WriteInfo("C'est super efficace !")
            print("super efficace")
        else : 
            print("problème efficacité")

        degats *= eff

        #Crit
        if isCrit(Attaque) :
            WriteInfo("Coup Critique !")
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

def Clairvoyance(pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :
        if pokemon_attaquant.accuracy < 0 :
            pokemon_attaquant.accuracy = 0
        pokemon_attaquant.accuracy += 2
        WriteInfo("La Précision de " + pokemon_attaquant.name + " !")


    return pokemon_attaquant

def Clonage(pokemon_attaquant) :
    if pokemon_attaquant.PV > ceil(pokemon_attaquant.PV / 4) :
        pokemon_attaquant.PV -= ceil(pokemon_attaquant.PV / 4)
        pokemon_attaquant.clone = True
        pokemon_attaquant.clonePV = ceil(pokemon_attaquant.PV / 4)
        WriteInfo(pokemon_attaquant.name + " se cache derrière un clone !")
    else :
        WriteInfo(pokemon_attaquant.name + " n'a pas assez de PV pour utiliser clonage !")
        print("Clonage a échoué")

    return pokemon_attaquant

def CloseCombat(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    if pokemon_defenseur.PV != PVAvantAttaque :
        if pokemon_attaquant.DefBuff > -6 :
            WriteInfo("La Défense de " + pokemon_attaquant.name + " baisse !")
            pokemon_attaquant.DefBuff -= 1
        if pokemon_attaquant.DefSpeBuff > -6 :
            WriteInfo("La Défense Spéciale de " + pokemon_attaquant.name + " baisse !")
            pokemon_attaquant.DefSpeBuff -= 1
            
        pokemon_attaquant.Def = pokemon_attaquant.DefInit * boost(pokemon_attaquant.DefBuff)
        pokemon_attaquant.Def = pokemon_attaquant.DefSpeInit * boost(pokemon_attaquant.DefSpeBuff)


    return pokemon_attaquant, pokemon_defenseur

def Colere(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if dresseurPokemonAttaquant.actionOblig == None :
        dresseurPokemonAttaquant.actionOblig = [1, numAttaque]
        dresseurPokemonAttaquant.actionObligNbTour = rand(1, 2)
    elif dresseurPokemonAttaquant.actionObligNbTour == 1 :
        dresseurPokemonAttaquant.actionOblig = None
        dresseurPokemonAttaquant.actionObligNbTour = None
        pokemon_attaquant.confusion = True
        pokemon_attaquant.confusionNum = rand(1, 4)
    else :
        dresseurPokemonAttaquant.actionObligNbTour -= 1

    print(pokemon_defenseur.PV)
    if pokemon_defenseur.PV < 0 :
        pokemon_defenseur.PV = 0

    return pokemon_attaquant, pokemon_defenseur, dresseurPokemonAttaquant

def Conversion(pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :
        WriteInfo(pokemon_attaquant.name + " change de type !")
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

    WriteInfo(pokemon_attaquant.name + " est blessé par le contrecoup !")

    pokemon_attaquant.PV -= ceil((PVAvantAttaque - pokemon_defenseur.PV) / 3)
    if pokemon_attaquant.PV < 0 :
        pokemon_attaquant.PV = 0
    if pokemon_defenseur.PV < 0 :
        pokemon_defenseur.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def DemiTour(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseur, pokemonActuelNum) :
    Attaque.puissance = 70
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    if dresseur.person == "player" :
        WriteInfo(pokemon_attaquant.name + " est renvoyé !")
        newPokemonActuelNum = ChoosePokemon(dresseur, pokemonActuelNum)
    else :
        WriteInfo(pokemon_attaquant.name + " est renvoyé !")
        newPokemonActuelNum = ChangeAdversaire(dresseur, pokemonActuelNum)

    return pokemon_defenseur, newPokemonActuelNum

def DracoMeteore(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 130
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV


    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if pokemon_defenseur.PV != PVAvantAttaque :
        WriteInfo("L'Attaque Spécial de " + pokemon_attaquant.name + " baisse beaucoup !")
        pokemon_attaquant.AttSpeBuff -= 2
        if pokemon_attaquant.AttSpeBuff < -6 :
            pokemon_attaquant.AttSpeBuff = -6
        
        pokemon_attaquant.AttSpe = pokemon_attaquant.AttSpeInit * boost(pokemon_attaquant.AttSpeBuff)


    return pokemon_attaquant, pokemon_defenseur

def EclairFou(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 90
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    WriteInfo(pokemon_attaquant.name + " est bléssé par le contrecoup !")
    pokemon_attaquant.PV -= ceil((PVAvantAttaque - pokemon_defenseur.PV) / 4)
    if pokemon_attaquant.PV < 0 :
        pokemon_attaquant.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def Effort(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if pokemon_defenseur.PV > pokemon_attaquant.PV :
            WriteInfo("Les PV de " + pokemon_defenseur.name + " devienne égaux aux PV de " + pokemon_attaquant.PV + " !")
            pokemon_defenseur.PV = pokemon_attaquant.PV
        else :
            WriteInfo("Les PV de " + pokemon_defenseur.name + " sont trop bas !")
            print("PV de l'adversaire trop bas")

    return pokemon_defenseur

def Explosion(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    
    Attaque.puissance = 250
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    if pokemon_defenseur.PV != PVAvantAttaque :
        WriteInfo(pokemon_defenseur.name + " est K.O !")
        pokemon_attaquant.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def Facade(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    if pokemon_attaquant.statut == "Brûlure" :
        Attaque.puissance = 280
    elif pokemon_attaquant.statut == "Paralysie" or pokemon_attaquant.statut == "Empoisonnement" :
        Attaque.puissance = 140
    else :
        Attaque.puissance = 70
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def FrappeAtlas(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :
        pokemon_defenseur.PV -= 100
    return pokemon_defenseur

def GlasDeSoin(dresseurPokemonAttaquant) :
    if dresseurPokemonAttaquant.person == "player" :
        WriteInfo("Vos pokémons n'ont plus de problèmes de statut !")
    else :
        WriteInfo("Les pokémons de l'adversaire n'ont plus de problèmes de statut !")

    for i in range(len(dresseurPokemonAttaquant.pokemons)) :
        dresseurPokemonAttaquant.pokemons[i].statut = None

    return dresseurPokemonAttaquant

def LanceSoleil(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque) :
    Attaque.puissance = 120
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    if dresseurPokemonAttaquant.actionOblig == None and terrain.climat != "Soleil" :
        WriteInfo(pokemon_attaquant.name + " se charge !")
        dresseurPokemonAttaquant.actionOblig = [1, numAttaque]
        dresseurPokemonAttaquant.actionObligNbTour = 1
    elif terrain.climat == "Soleil" :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif dresseurPokemonAttaquant.actionObligNbTour == 1 :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
        dresseurPokemonAttaquant.actionOblig = None
        dresseurPokemonAttaquant.actionObligNbTour = None

    return pokemon_defenseur, dresseurPokemonAttaquant

def Malediction(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if pokemon_attaquant.Type == "Spectre" or pokemon_attaquant.Type2 == "Spectre" :
            WriteInfo(pokemon_attaquant.name + " perd la moitié de ses PV maximum !")
            pokemon_attaquant.PV -= ceil(pokemon_attaquant.PVMax / 2)
            WriteInfo(pokemon_defenseur.name + " est maudit !")
            pokemon_defenseur.maudit = True

        else :
            if pokemon_attaquant.AttBuff < 6 :
                WriteInfo("L'Attaque de " + pokemon_attaquant.name + " augmente !")
                pokemon_attaquant.AttBuff += 1
            if pokemon_attaquant.DefBuff < 6 :
                WriteInfo("La Défense de " + pokemon_attaquant.name + " augmente !")
                pokemon_attaquant.DefBuff += 1
            if pokemon_attaquant.SpeedBuff > -6 :
                WriteInfo("La Vitesse de " + pokemon_attaquant.name + " diminue !")
                pokemon_attaquant.SpeedBuff -= 1
                
            pokemon_attaquant.Att = pokemon_attaquant.AttInit * boost(pokemon_attaquant.AttBuff)
            pokemon_attaquant.Def = pokemon_attaquant.DefInit * boost(pokemon_attaquant.DefBuff)
            pokemon_attaquant.Speed = pokemon_attaquant.SpeedInit * boost(pokemon_attaquant.SpeedBuff)

    return pokemon_attaquant, pokemon_defenseur

def Megaphone(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 100
    Attaque.physique = 1
    Attaque.special = 0
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if pokemon_attaquant.statut == "Brûlure" :
        pokemon_attaquant.Att = pokemon_attaquant.Att / 2

    if pokemon_defenseur.abri :
        WriteInfo("Mégaphone passe outre le clone !")

    elif booleanAttaque :
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
            WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
            print("inefficace")
        elif eff == 0.25 or eff == 0.5 :
            WriteInfo("Ce n'est pas très efficace !")
            print("peu efficace")
        elif eff == 1 :
            print("efficace")
        elif eff >= 2 :
            WriteInfo("C'est super efficace !")
            print("super efficace")
        else : 
            print("problème efficacité")

        degats *= eff

        #Crit
        if isCrit(Attaque) :
            WriteInfo("Coup Critique !")
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

def Picots(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

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
            WriteInfo("Il y a déjà le nombre maximum de Picots !")
            print("trop de picots")

    return terrain

def PicsToxik(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if dresseurPokemonAttaquant.person == "player" :
            toChange = "PicsToxik"
        else :
            toChange = "PicsToxikAdverse"
        
        if getattr(terrain, toChange) == None :
            setattr(terrain, toChange, 1)
        else :
            WriteInfo("Il y a déjà les Pics Toxik !")
            print("déjà des Pics Toxik")

    return terrain

def PiedSaute(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 100
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    if not MissWork(pokemon_attaquant, Attaque) :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    elif pokemon_defenseur.Type == "Spectre" or pokemon_defenseur.Type2 == "Spectre" :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    elif pokemon_defenseur.abri :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo(pokemon_defenseur.name + " se protège, l'attaque est sans effet.")
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    else :
        if pokemon_attaquant.statut == "Brûlure" :
            pokemon_attaquant.Att = pokemon_attaquant.Att / 2

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
            WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
            print("inefficace")
        elif eff == 0.25 or eff == 0.5 :
            WriteInfo("Ce n'est pas très efficace !")
            print("peu efficace")
        elif eff == 1 :
            print("efficace")
        elif eff >= 2 :
            WriteInfo("C'est super efficace !")
            print("super efficace")
        else : 
            print("problème efficacité")

        degats *= eff

        #Crit
        if isCrit(Attaque) :
            WriteInfo("Coup Critique !")
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

    return pokemon_attaquant, pokemon_defenseur

def PiedVoltige(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 130
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    if not MissWork(pokemon_attaquant, Attaque) :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    elif pokemon_defenseur.Type == "Spectre" or pokemon_defenseur.Type2 == "Spectre" :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    elif pokemon_defenseur.abri :
        pokemon_attaquant.PV = ceil(pokemon_attaquant.PVMax / 2)
        WriteInfo(pokemon_defenseur.name + " se protège, l'attaque est sans effet.")
        WriteInfo(pokemon_attaquant.name + " se blesse dans sa chute !")
    else :
        if pokemon_attaquant.statut == "Brûlure" :
            pokemon_attaquant.Att = pokemon_attaquant.Att / 2

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
            WriteInfo("Cela n'affecte pas " + pokemon_defenseur.name + " !")
            print("inefficace")
        elif eff == 0.25 or eff == 0.5 :
            WriteInfo("Ce n'est pas très efficace !")
            print("peu efficace")
        elif eff == 1 :
            print("efficace")
        elif eff >= 2 :
            WriteInfo("C'est super efficace !")
            print("super efficace")
        else : 
            print("problème efficacité")

        degats *= eff

        #Crit
        if isCrit(Attaque) :
            WriteInfo("Coup Critique !")
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

    return pokemon_attaquant, pokemon_defenseur

def PiegeDeRoc(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if dresseurPokemonAttaquant.person == "player" :
            toChange = "PiegeDeRoc"
        else :
            toChange = "PiegeDeRocAdverse"
        
        if getattr(terrain, toChange) == None :
            setattr(terrain, toChange, 1)
        else :
            WriteInfo("Il y a déjà les Pièges de Roc !")
            print("déjà des pièges de Roc")

    return terrain

def Projection(dresseur, dresseurAdverse, pokemonActuelNum, pokemonActuelNumDresseurAdverse) :
    count = 0
    for i in range(len(dresseurAdverse.pokemons)) :
        if dresseurAdverse.pokemons[i].PV > 0 :
            count += 1
    if count > 1 :
        pokemonActuelNumDresseurAdverse = ChangeAdversaire(dresseurAdverse, pokemonActuelNumDresseurAdverse)
        if dresseur.person == "player" :
            ChangePokemonGraph(dresseur.pokemons[pokemonActuelNum], dresseurAdverse.pokemons[pokemonActuelNumDresseurAdverse])
        WriteInfo(dresseurAdverse.pokemons[pokemonActuelNumDresseurAdverse].name + " est envoyé !")
    else :
        WriteInfo("Pas assez de pokémon en vie pour forcer un changment de pokémon !")
        print("problème de projection")

    return pokemonActuelNumDresseurAdverse

def PuissanceCachee(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 60
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None
    if pokemon_attaquant.id == 2 or pokemon_attaquant.id == 4 or pokemon_attaquant.id == 18 or pokemon_attaquant.id == 42 :
        Attaque.Type = "Plante"
    elif pokemon_attaquant.id == 17 or pokemon_attaquant.id == 22 or pokemon_attaquant.id == 78 :
        Attaque.Type = "Glace"
    elif pokemon_attaquant.id == 40 or pokemon_attaquant.id == 43 or pokemon_attaquant.id == 49 or pokemon_attaquant.id == 60 :
        Attaque.Type = "Feu"
    elif pokemon_attaquant.id == 55 :
        Attaque.Type = "Spectre"
    else :
        print("probleme puissance cachee")
        Attaque.Type = "Normal"

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur
    
def Rapace(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    WriteInfo(pokemon_attaquant.name + " est bléssé par le contrecoup !")

    pokemon_attaquant.PV -= ceil((PVAvantAttaque - pokemon_defenseur.PV) / 3)
    if pokemon_attaquant.PV < 0 :
        pokemon_attaquant.PV = 0

    return pokemon_attaquant, pokemon_defenseur

def Repos(pokemon_attaquant) :
    if pokemon_attaquant.PV == pokemon_attaquant.PVMax :
        WriteInfo("Les PV de " + pokemon_attaquant.name + " son déjà au maximum !")

        print("La capacité échoue")
    else :
        WriteInfo(pokemon_attaquant.name + " s'endort !")
        pokemon_attaquant.statut = "Sommeil"
        pokemon_attaquant.PV = pokemon_attaquant.PVMax

    return pokemon_attaquant

def Requiem(pokemon_attaquant, pokemon_defenseur) :
    if pokemon_attaquant.requiem != True :
        WriteInfo(pokemon_attaquant.name + " sera K.O. dans 3 tours !")
        pokemon_attaquant.requiem = True
        pokemon_attaquant.requiemNum = 3

    if pokemon_defenseur.requiem != True :
        WriteInfo(pokemon_defenseur.name + " sera K.O. dans 3 tours !")
        pokemon_defenseur.requiem = True
        pokemon_defenseur.requiemNum = 3

    return pokemon_attaquant, pokemon_defenseur

def Sabotage(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 90
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def Siphon(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 35
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if PVAvantAttaque != pokemon_defenseur.PV :
        pokemon_defenseur.siphon = True
        pokemon_defenseur.siphonNum = rand(4,5)

    return pokemon_defenseur

def Souvenir(pokemon_attaquant, pokemon_defenseur) :
    pokemon_attaquant.PV = 0
    pokemon_defenseur.Att -= 2
    WriteInfo("L'Attaque de " + pokemon_defenseur.name + " baisse beaucoup !")
    pokemon_defenseur.AttSpe -= 2
    WriteInfo("L'Attaque Spéciale de " + pokemon_defenseur.name + " baisse beaucoup !")

    if pokemon_defenseur.AttBuff < -6 :
        pokemon_defenseur.AttBuff = -6
    if pokemon_defenseur.AttSpeBuff < -6 :
        pokemon_defenseur.AttSpeBuff = -6

    
    pokemon_defenseur.Att = pokemon_defenseur.AttInit * boost(pokemon_defenseur.AttBuff)
    pokemon_defenseur.AttSpe = pokemon_defenseur.AttSpeInit * boost(pokemon_defenseur.AttSpeBuff)

    return pokemon_attaquant, pokemon_defenseur

def Stalactite(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 30
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

def Surchauffe(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 130
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    if PVAvantAttaque != pokemon_defenseur.PV :        
        pokemon_attaquant.AttSpeBuff -= 2
        WriteInfo("L'Attaque Spécial de " + pokemon_attaquant.name + " baisse beaucoup !")
        if pokemon_attaquant.AttSpeBuff < -6 :
            pokemon_attaquant.AttSpeBuff = -6
        
        pokemon_attaquant.AttSpe = pokemon_attaquant.AttSpeInit * boost(pokemon_attaquant.AttSpeBuff)


    return pokemon_attaquant, pokemon_defenseur

def Surpuissance(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 120
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if PVAvantAttaque != pokemon_defenseur.PV :        
        if pokemon_attaquant.DefBuff > -6 :
            pokemon_attaquant.DefBuff -= 1
            WriteInfo("La Défense de " + pokemon_attaquant.name + " baisse !")
        if pokemon_attaquant.AttBuff > -6 :
            pokemon_attaquant.AttBuff -= 1
            WriteInfo("L'Attaque de " + pokemon_attaquant.name + " baisse !")
        
        pokemon_attaquant.Def = pokemon_attaquant.DefInit * boost(pokemon_attaquant.DefBuff)
        pokemon_attaquant.Att = pokemon_attaquant.AttInit * boost(pokemon_attaquant.AttBuff)



    return pokemon_attaquant, pokemon_defenseur

def Synthese(pokemon_attaquant, terrain) :
    WriteInfo(pokemon_attaquant.name + " se soigne !")
    if terrain.climat == None :
        pokemon_attaquant.PV += (pokemon_attaquant.PVMax / 2)
    elif terrain.climat == "Soleil" :
        pokemon_attaquant.PV += (2 * pokemon_attaquant.PVMax / 3)
    else :
        pokemon_attaquant.PV += (pokemon_attaquant.PVMax / 4)

    if pokemon_attaquant.PV > pokemon_attaquant.PVMax :
        pokemon_attaquant.PV = pokemon_attaquant.PVMax

    return pokemon_attaquant

def TourDeMagie(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 80
    Attaque.physique = 0
    Attaque.special = 1
    Attaque.effect = 0
    Attaque.probaEffect = None

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    return pokemon_defenseur

def TourRapide(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant) :
    Attaque.puissance = 50
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    if PVAvantAttaque != pokemon_defenseur.PV :
        if dresseurPokemonAttaquant.person == "player" :
            WriteInfo("Votre terrain a été nettoyé !")
            terrain.Picots = None
            terrain.PicsToxik = None
            terrain.PiegeDeRoc = None
            terrain.Vampigraine = None
        else :
            WriteInfo("Le terrain adverse a été nettoyé !")
            terrain.PicotsAdverse = None
            terrain.PicsToxikAdverse = None
            terrain.PiegeDeRocAdverse = None
            terrain.VampigraineAdverse = None

        if pokemon_attaquant.SpeedBuff < 6 :
            pokemon_attaquant.SpeedBuff += 1
            WriteInfo("La Vitesse de " + pokemon_attaquant.name + " augmente !")
        
        pokemon_attaquant.Speed = pokemon_attaquant.SpeedInit * boost(pokemon_attaquant.SpeedBuff)


    return pokemon_attaquant, pokemon_defenseur, terrain

def VampiPoing(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 75
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)

    pokemon_attaquant.PV += (ceil((PVAvantAttaque - pokemon_defenseur.PV) / 2))

    if pokemon_attaquant.PV > pokemon_attaquant.PVMax :
        pokemon_attaquant.PV = pokemon_attaquant.PVMax

    return pokemon_attaquant, pokemon_defenseur

def Vampigraine(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if dresseurPokemonAttaquant.person == "player" :
            toChange = "Vampigraine"
        else :
            toChange = "VampigraineAdverse"
        
        if getattr(terrain, toChange) == None :
            setattr(terrain, toChange, 1)
        else :
            print("déjà vampigraine")

    return terrain

def Vampirisme(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    Attaque.puissance = 80
    Attaque.physique = 1
    Attaque.special = 0
    Attaque.effect = 0
    Attaque.probaEffect = None

    PVAvantAttaque = pokemon_defenseur.PV

    pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    
    WriteInfo(pokemon_attaquant.name + " se soigne !")
    pokemon_attaquant.PV += (ceil((PVAvantAttaque - pokemon_defenseur.PV) / 2))
    if pokemon_attaquant.PV > pokemon_attaquant.PVMax :
        pokemon_attaquant.PV = pokemon_attaquant.PVMax

    return pokemon_attaquant, pokemon_defenseur

def VentArriere(dresseurPokemonAttaquant, pokemon_attaquant, Attaque) :
    if MissWork(pokemon_attaquant, Attaque) :

        if dresseurPokemonAttaquant.person == "player" :
            WriteInfo("La Vitesse de toute votre équipe augmente beaucoup !")
        else :
            WriteInfo("La Vitesse de toute l'équipe adverse augmente beaucoup !")

    
        dresseurPokemonAttaquant.pokemons[0].SpeedBuff += 2
        dresseurPokemonAttaquant.pokemons[1].SpeedBuff += 2
        dresseurPokemonAttaquant.pokemons[2].SpeedBuff += 2
        dresseurPokemonAttaquant.pokemons[3].SpeedBuff += 2
        dresseurPokemonAttaquant.pokemons[4].SpeedBuff += 2
        dresseurPokemonAttaquant.pokemons[5].SpeedBuff += 2

        if dresseurPokemonAttaquant.pokemons[0].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[0].SpeedBuff = 6
        if dresseurPokemonAttaquant.pokemons[1].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[1].SpeedBuff = 6
        if dresseurPokemonAttaquant.pokemons[2].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[2].SpeedBuff = 6
        if dresseurPokemonAttaquant.pokemons[3].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[3].SpeedBuff = 6
        if dresseurPokemonAttaquant.pokemons[4].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[4].SpeedBuff = 6
        if dresseurPokemonAttaquant.pokemons[5].SpeedBuff > 6 :
            dresseurPokemonAttaquant.pokemons[5].SpeedBuff = 6

        dresseurPokemonAttaquant.pokemons[0].Speed = dresseurPokemonAttaquant.pokemons[0].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[0].SpeedBuff)
        dresseurPokemonAttaquant.pokemons[1].Speed = dresseurPokemonAttaquant.pokemons[1].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[1].SpeedBuff)
        dresseurPokemonAttaquant.pokemons[2].Speed = dresseurPokemonAttaquant.pokemons[2].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[2].SpeedBuff)
        dresseurPokemonAttaquant.pokemons[3].Speed = dresseurPokemonAttaquant.pokemons[3].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[3].SpeedBuff)
        dresseurPokemonAttaquant.pokemons[4].Speed = dresseurPokemonAttaquant.pokemons[4].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[4].SpeedBuff)
        dresseurPokemonAttaquant.pokemons[5].Speed = dresseurPokemonAttaquant.pokemons[5].SpeedInit * boost(dresseurPokemonAttaquant.pokemons[5].SpeedBuff)
        

    return dresseurPokemonAttaquant
        
def Voeu(pokemon_attaquant, Attaque, terrain, dresseurPokemonAttaquant) :
    if MissWork(pokemon_attaquant, Attaque) :

        if dresseurPokemonAttaquant.person == "player" :
            toChange = "VoeuNbTour"
            toChange2 = "VoeuPVHeal"
        else :
            toChange = "VoeuAdverseNbTour"
            toChange2 = "VoeuAdversePVHeal"
        
        if getattr(terrain, toChange) == None :
            WriteInfo(pokemon_attaquant.name + " sera soigné dans 2 tours !")

            setattr(terrain, toChange, 2)
            setattr(terrain, toChange2, ceil(pokemon_attaquant.PVMax / 2))

        else :
            print("vous avez déjà fait un voeu")

    return terrain

def VoleForce(pokemon_attaquant, Attaque, pokemon_defenseur) :
    if MissWork(pokemon_attaquant, Attaque) :

        if pokemon_defenseur.AttBuff > -6 :
            pokemon_defenseur.AttBuff -= 1
            WriteInfo(pokemon_attaquant.name + " vole la force de " + pokemon_defenseur.name + " !")
            pokemon_defenseur.Att = pokemon_defenseur.AttInit * boost(pokemon_defenseur.AttBuff)

            pokemon_attaquant.PV += pokemon_defenseur.Att
            if pokemon_attaquant.PV > pokemon_attaquant.PVMax :
                pokemon_attaquant.PV = pokemon_attaquant.PVMax
        
        else :
            WriteInfo(pokemon_defenseur.name + " est trop faible !")
            print("le pokemon est trop faible")

    return pokemon_attaquant, pokemon_defenseur
