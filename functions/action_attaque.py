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
from graph.write_info import WriteInfo

# Fonction qui appelle la fonction correspondant au type d'attaque
def ActionAttaque(pokemon_attaquant, pokemon_defenseur, numAttaque, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur) :
    if dresseurPokemonAttaquant.person == "player" :
        WriteInfo(pokemon_attaquant.name + " utilise " + pokemon_attaquant.Attaques[numAttaque-1].name + " !")
    else :
        WriteInfo(pokemon_attaquant.name + " ennemi utilise " + pokemon_attaquant.Attaques[numAttaque-1].name + " !")
        
    if type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueOffensive :
        print("Attaque offensive")
        pokemon_defenseur = Offensive(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1], terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueBuff :
        print("Attaque buff")
        pokemon_attaquant = Buff(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueClimat :
        print("Attaque climat")
        terrain = Climat(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1], terrain)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueHeal :
        print("Attaque heal")
        pokemon_attaquant = Heal(pokemon_attaquant, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueStatut : 
        print("Attaque statut")       
        pokemon_defenseur = Statut(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1])
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur


    elif type(pokemon_attaquant.Attaques[numAttaque-1]) is AttaqueAutre :
        print("Attaque autre")
        pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur = other.Autres(pokemon_attaquant, pokemon_defenseur, pokemon_attaquant.Attaques[numAttaque-1], terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, numAttaque, pokemonActuelNum, pokemonActuelNumDresseurDefenseur)
        return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, dresseurPokemonDefenseur, pokemonActuelNum, pokemonActuelNumDresseurDefenseur
