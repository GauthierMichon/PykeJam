from functions.choose_action import chooseAction
from functions.fight import fight


def combat(player, adversaire) :

    pokemon_actuel_player = player.pokemons[0]

    pokemon_actuel_adversaire = adversaire.pokemons[0]

    climat = None

    while True :
        action, actionNum = chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire)
        
        action_adversaire, actionNum_adversaire = 1, 1

        if action == 1 :
            if pokemon_actuel_player.Speed > pokemon_actuel_adversaire.Speed :
                fight(pokemon_actuel_player, pokemon_actuel_adversaire, actionNum, climat)

        