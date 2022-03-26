from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_statut import AttaqueStatut
from classes.attaque_autre import AttaqueAutre
from functions.derouler_attauqe_offensive import Offensive


def fight(pokemon_attaquant, pokemon_defenseur, numAttaque) :
    print(type(pokemon_attaquant.Attaques[numAttaque-1]))
    if type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueOffensive) :
        Offensive(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1])
    elif type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueBuff) :
        print("buff")
    elif type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueClimat) :
        print("climat")
    elif type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueHeal) :
        print("heal")
    elif type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueStatut) :
        print("statut")
    elif type(pokemon_attaquant.Attaques[numAttaque-1] == AttaqueAutre) :
        print("autre")