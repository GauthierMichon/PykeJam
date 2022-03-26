from functions.choose_action import chooseAction
from functions.fight import fight


def combat(player, adversaire) :

    pokemonActualPlayerNumber = 0

    pokemonActualAdversNumber = 0

    climat = None

    while True :
        action, actionNum = chooseAction(player, adversaire, player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
        
        action_adversaire, actionNum_adversaire = 1, 1

        if action == 1 :
            if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                adversaire.pokemons[pokemonActualAdversNumber] = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, climat)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                

        