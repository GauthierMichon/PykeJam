from math import ceil
from functions.boost_value import boost
from functions.choose_random_num import rand
from graph.write_info import WriteInfo

# Fonction pour savoir si l'attaque est réussi ou échoue
def MissWork(pokemon_attaquant, Attaque) :    
    booleanAttaque = True
    #############################################################################
    ########### Pour l'instant la confusion ne fait pas de dégats ###############
    #############################################################################
    # Si le pokemon attaquant est confus
    if pokemon_attaquant.confusion :
        # 2/3 que l'attaque réussisse
        if rand(0,100) > 33 :
            # Si l'attaque ne peut pas échouer
            if Attaque.accuracy == None :
                booleanAttaque = True
            # Si l'attaque peut échouer
            else :
                # Nombre random entre 0 et 100
                randNum = rand(0, 100)
                # Calcul de la probabilité de réussir
                acc = Attaque.accuracy * boost(pokemon_attaquant.accuracy)
                # Si l'attaque réussit
                if acc >= randNum :
                    booleanAttaque = True
                else :
                    WriteInfo(pokemon_attaquant.name + " est confus, il ne peut pas attaquer !")

                    booleanAttaque = False
        else :
            WriteInfo(pokemon_attaquant.name + " est confus, il ne peut pas attaquer !")

            booleanAttaque = False
            degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * 40
            degats = degats / (pokemon_attaquant.Def * 50) + 2
            pokemon_attaquant.PV -= int(ceil(degats))

    else : 
        # Si l'attaque ne peut pas échouer
        if Attaque.accuracy == None :
            booleanAttaque = True
        # Si l'attaque peut échouer
        else :
            # Nombre random entre 0 et 100
            randNum = rand(0, 100)
            # Calcul de la probabilité de réussir
            acc = Attaque.accuracy * boost(pokemon_attaquant.accuracy)
            # Si l'attaque réussit
            if acc >= randNum :
                booleanAttaque = True
            else :
                WriteInfo(pokemon_attaquant.name + " rate son attaque !")

                booleanAttaque = False

    return booleanAttaque