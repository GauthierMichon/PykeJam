from functions.attaque_miss_or_work import MissWork
from functions.choose_random_num import rand
from functions.climat_attaque_offensive import Climat
from functions.critique import isCrit
from functions.effect_attaque_offensive import Effect
from functions.table_types import TableType
from math import *
from graph.write_info import WriteInfo

# Fonction qui gère les attaques offensives
def Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) :
    # Si l'attaque échoue
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    # Si le pokemon attaquant est brulé
    if pokemon_attaquant.statut == "Brûlure" :
        pokemon_attaquant.Att = pokemon_attaquant.Att / 2

    # Si l'adversaire a utilisé abri
    if pokemon_defenseur.abri :
        WriteInfo(pokemon_defenseur.name + " se protège, l'attaque est sans effet.")
        booleanAttaque = False

        print("Le Pokémon adverse se protège, l'attaque est sans effet.")

    elif booleanAttaque :
        # Si l'aatque est physique
        if Attaque.physique == 1 :
            # Calcul des dégats
            degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * Attaque.puissance
            degats = degats / (pokemon_defenseur.Def * 50) + 2
        # Si l'attaque est spéciale
        elif Attaque.special == 1 :
            # Calcul des dégats
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
            # Infilge les dégats
            pokemon_defenseur.PV -= int(ceil(degats))
            # Appelle la fonction d'effet de l'attaque
            pokemon_attaquant, pokemon_defenseur = Effect(pokemon_attaquant, pokemon_defenseur, Attaque)
        # Si le pokemon defenseur est caché derrière un clone
        else :
            # Le clone prend les dégats
            pokemon_defenseur.clonePV -= int(ceil(degats))
            # Si le clone est mort
            if pokemon_defenseur.clonePV <= 0 :
                pokemon_defenseur.clone = False
                pokemon_defenseur.clonePV = None

    else :
        print("miss")

    if pokemon_defenseur.PV < 0 :
        pokemon_defenseur.PV = 0
    
    return pokemon_defenseur

    


    