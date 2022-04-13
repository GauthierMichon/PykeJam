from classes.terrain import Terrain
from functions.choose_action import chooseAction
from functions.choose_random_num import rand
from functions.fight import fight
from functions.switch import Switch


def combat(player, adversaire) :

    pokemonActualPlayerNumber = 0

    pokemonActualAdversNumber = 0

    terrain = Terrain()

    boolean = True
    while boolean :
        if player.actionOblig == None :
            action, actionNum = chooseAction(player, adversaire, player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], player, pokemonActualPlayerNumber)
        else : 
            action = player.actionOblig[0]
            actionNum = player.actionOblig[1]

        action_adversaire, actionNum_adversaire = 1, 1

        if action == 2 or action == 3 :
            print("player begin")
        elif action_adversaire == 2 or action_adversaire == 3 :
            print("advers begin")
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum].priorityLevel > adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire].priorityLevel :
            print("player begin")
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum].priorityLevel < adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire].priorityLevel :
            print("advers begin")
        elif player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
            print("player begin")
        elif player.pokemons[pokemonActualPlayerNumber].Speed < adversaire.pokemons[pokemonActualAdversNumber].Speed :
            print("advers begin")
        else :
            if rand(1, 2) == 1 :
                print("player begin")
            else :
                print("advers begin")

        if action == 1 :
            #if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
            player.pokemons[pokemonActualAdversNumber], adversaire.pokemons[pokemonActualPlayerNumber], terrain, player = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                
        elif action == 2 :
            print("{} a été envoyé".format(player.pokemons[actionNum].name))
            player = Switch(player, pokemonActualPlayerNumber)
            pokemonActualPlayerNumber = actionNum

        elif action == 3 :
            print("item mais pas encore implémenté")

    
        