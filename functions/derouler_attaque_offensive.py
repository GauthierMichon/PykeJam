from functions.attaque_miss_or_work import MissWork
from functions.choose_random_num import rand
from functions.climat_attaque_offensive import Climat
from functions.critique import isCrit
from functions.effect_attaque_offensive import Effect
from functions.table_types import TableType
from math import *


def Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if pokemon_attaquant.statut == "Brûlure" :
        pokemon_attaquant.Att = pokemon_attaquant.Att / 2

    if pokemon_defenseur.abri :
        print("Le Pokémon adverse se protège, l'attaque est sans effet.")

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
        if isCrit(Attaque) :
            print("Coup Critique")
            degats *= 2

        #Climat
        degats *= Climat(terrain, Attaque.Type)


        #Random num entre 0.85 et 1
        degats *= (rand(85, 100) / 100)

        if pokemon_defenseur.clone == False :
            pokemon_defenseur.PV -= ceil(degats)
            pokemon_attaquant, pokemon_defenseur = Effect(pokemon_attaquant, pokemon_defenseur, Attaque)
        else :
            pokemon_defenseur.clonePV -= ceil(degats)
            if pokemon_defenseur.clonePV <= 0 :
                pokemon_defenseur.clone = False
                pokemon_defenseur.clonePV = None

    else :
        print("miss")
    
    return pokemon_defenseur

    


    