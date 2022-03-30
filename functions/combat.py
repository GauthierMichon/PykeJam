from classes.terrain import Terrain
from functions.choose_action import chooseAction
from functions.fight import fight


def combat(player, adversaire) :

    pokemonActualPlayerNumber = 0

    pokemonActualAdversNumber = 0

    terrain = Terrain(None, None, None, None, None, None, None, None, None)

    while True :
        action, actionNum = chooseAction(player, adversaire, player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
        
        action_adversaire, actionNum_adversaire = 1, 1

        if action == 1 :
            #if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
            player.pokemons[pokemonActualAdversNumber], adversaire.pokemons[pokemonActualPlayerNumber], terrain = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                

        