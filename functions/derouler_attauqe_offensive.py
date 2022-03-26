from functions.attaque_miss_or_work import MissWork
from functions.derouler_attaque_phy import AttaquePhy
from functions.derouler_attaque_spe import AttaqueSpe


def Offensive(pokemon_attaquant, pokemon_defenseur, Attaque, climat) :
    booleanAttaque = MissWork(pokemon_attaquant, Attaque)

    if booleanAttaque :
        print("that work")
        if Attaque.physique == 1 :
            AttaquePhy(pokemon_attaquant, pokemon_defenseur, Attaque, climat)
        elif Attaque.special == 1 :
            AttaqueSpe(pokemon_attaquant, pokemon_defenseur, Attaque, climat)








    else :
        print("that don't work")

    


    