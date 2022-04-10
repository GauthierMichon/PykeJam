from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_statut import AttaqueStatut
from classes.attaque_autre import AttaqueAutre
from functions.derouler_attaque_buff import Buff
from functions.derouler_attaque_climat import Climat
from functions.derouler_attaque_heal import Heal
from functions.derouler_attaque_statut import Statut
from functions.derouler_attaque_offensive import Offensive
import functions.derouler_attaque_autre as other


def fight(pokemon_attaquant, pokemon_defenseur, numAttaque, terrain, dresseurPokemonAttaquant) :
    if type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueOffensive :
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1], terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueBuff :
        pokemon_attaquant = Buff(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueClimat :
        terrain = Climat(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1], terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueHeal :
        pokemon_attaquant = Heal(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueStatut :        
        pokemon_defenseur = Statut(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueAutre :
        other.Autres(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1], terrain, dresseurPokemonAttaquant, numAttaque)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant
