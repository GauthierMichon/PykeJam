from classes.terrain import Terrain
from functions.adversaire_turn import AdversaireTurn
from functions.choose_action import chooseAction
from functions.choose_random_num import rand
from functions.combat_continue import CombatContinue
from functions.fight import fight
from functions.player_turn import PlayerTurn
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

        action_adversaire, actionNum_adversaire = 1, rand(1, 4)

        if action == 2 or action == 3 :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        elif action_adversaire == 2 or action_adversaire == 3 :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].priorityLevel > adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire - 1].priorityLevel :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].priorityLevel < adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire - 1].priorityLevel :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        elif player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        elif player.pokemons[pokemonActualPlayerNumber].Speed < adversaire.pokemons[pokemonActualAdversNumber].Speed :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        else :
            if rand(1, 2) == 1 :
                player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
            else :
                player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")

        
        """ if action == 1 :
            #if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
            player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], terrain, player = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)
                
        elif action == 2 :
            print("{} a été envoyé".format(player.pokemons[actionNum].name))
            player = Switch(player, pokemonActualPlayerNumber)
            pokemonActualPlayerNumber = actionNum

        elif action == 3 :
            print("item mais pas encore implémenté") """

        if not CombatContinue(player, adversaire) :
            boolean = False

    
        