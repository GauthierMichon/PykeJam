from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_statut import AttaqueStatut
from classes.attaque_autre import AttaqueAutre
from functions.derouler_attaque_buff import Buff
from functions.derouler_attaque_climat import Climat
from functions.derouler_attaque_offensive import Offensive


def fight(pokemon_attaquant, pokemon_defenseur, numAttaque, climat) :
    if type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueOffensive :
        degats = Offensive(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1], climat)
        pokemon_defenseur.PV -= degats
        return pokemon_attaquant, pokemon_defenseur, climat


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueBuff :
        pokemon_attaquant = Buff(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, climat


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueClimat :
        climat = Climat(pokemon_attaquant.Attaques[numAttaque-1], climat)
        return pokemon_attaquant, pokemon_defenseur, climat


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueHeal :
        print("heal")


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueStatut :
        print("statut")


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueAutre :
        print("autre")