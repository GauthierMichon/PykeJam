from functions.choose_item import ChooseItem
from functions.choose_pokemon_change import ChoosePokemon

# Fonction qui fait choisir au joueur l'action à effectuée
def chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire, dresseurPokemonSwitch, pokemonActualDresseurNum) :

    # On affiche les actions possibles
    action = input("Quelle action faire ? (1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item)  ")

    # Si l'action est 1, on lance une attaque
    if action == "1" :

        # On affiche les attaques possibles
        actionNum = ChoosePokemon(pokemon_actuel_player)

    # Si l'action est 2, on change de pokemon
    if action == "2" :

        # On appelle la fonction qui permet de choisir le pokemon
        actionNum = ChoosePokemon(player, pokemonActualDresseurNum)
    
    # Si l'action est 3, on utilise un item
    if action == "3" :

        actionNum = ChooseItem(player)

    return int(action), int(actionNum)

        