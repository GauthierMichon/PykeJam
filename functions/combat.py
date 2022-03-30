from classes.terrain import Terrain
from functions.choose_action import chooseAction
from functions.fight import fight


def combat(player, adversaire) :

    pokemonActualPlayerNumber = 0

    pokemonActualAdversNumber = 0

    terrain = Terrain(None, None, None, None, None, None, None, None, None)

    while True :
        if player.actionOblig == None :
            action, actionNum = chooseAction(player, adversaire, player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
        else : 
            action = player.actionOblig[0]
            actionNum = player.actionOblig[1]
        
        action_adversaire, actionNum_adversaire = 1, 1

        if action == 1 :
            #if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
            player.pokemons[pokemonActualAdversNumber], adversaire.pokemons[pokemonActualPlayerNumber], terrain, player = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                

        