from math import ceil
from functions.boost_value import boost
from functions.choose_random_num import rand

def MissWork(pokemon_attaquant, Attaque) :    
    booleanAttaque = True
    if pokemon_attaquant.confusion :
        if rand(0,100) > 33 :
            if Attaque.accuracy == None :
                booleanAttaque = True
            else :
                randNum = rand(0, 100)
                acc = Attaque.accuracy * boost(pokemon_attaquant.accuracy)
                if acc >= randNum :
                    booleanAttaque = True
                else :
                    booleanAttaque = False
        else :
            booleanAttaque = False
            degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * 40
            degats = degats / (pokemon_attaquant.Def * 50) + 2
            pokemon_attaquant.PV -= ceil(degats)

    else : 
        if Attaque.accuracy == None :
            booleanAttaque = True
        else :
            randNum = rand(0, 100)
            acc = Attaque.accuracy * boost(pokemon_attaquant.accuracy)
            if acc >= randNum :
                booleanAttaque = True
            else :
                booleanAttaque = False

    return booleanAttaque