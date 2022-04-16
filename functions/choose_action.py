from functions.choose_pokemon_change import ChoosePokemon

# Fonction qui fait choisir au joueur l'action à effectuée
def chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire, dresseurPokemonSwitch, pokemonActualDresseurNum) :

    # On affiche les actions possibles
    action = input("Quelle action faire ? (1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item)  ")

    # Si l'action est 1, on lance une attaque
    if action == "1" :

        # On affiche les attaques possibles
        actionNum = input("Quelle Attaque utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3})  ".format(
            pokemon_actuel_player.Attaques[0].name,
            pokemon_actuel_player.Attaques[1].name,
            pokemon_actuel_player.Attaques[2].name,
            pokemon_actuel_player.Attaques[3].name
        ))

    # Si l'action est 2, on change de pokemon
    if action == "2" :

        # On appelle la fonction qui permet de choisir le pokemon
        actionNum = ChoosePokemon(player, pokemonActualDresseurNum)
    
    # Si l'action est 3, on utilise un item
    if action == "3" :

        print("item")

    return int(action), int(actionNum)

        