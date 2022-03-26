from functions.boost_value import boost
from functions.choose_random_num import rand

def MissWork(pokemon_attaquant, Attaque) :    
    booleanAttaque = True
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