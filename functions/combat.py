from functions.choose_action import chooseAction


def combat(player, adversaire) :

    pokemon_actuel_player = player.pokemons[0]

    pokemon_actuel_adversaire = adversaire.pokemons[0]

    while True :
        action, actionNum = chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire)
        
        action_adversaire, actionNum_adversaire = 1, 1

        