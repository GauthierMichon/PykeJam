from classes.terrain import Terrain
from functions.adversaire_turn import AdversaireTurn
from functions.choose_action import chooseAction
from functions.choose_random_num import rand
from functions.combat_continue import CombatContinue
from functions.end_turn import EndTurn
from functions.action_attaque import ActionAttaque
from functions.player_turn import PlayerTurn
from functions.switch import Switch
from functions.vampigraine_check import VampigraineCheck


def combat(player, adversaire) :

    # Initialisation des variables
    pokemonActualPlayerNumber = 0
    pokemonActualAdversNumber = 0
    terrain = Terrain()
    boolean = True

    while boolean :
        # Si le joueur peut choisir son action
        if player.actionOblig == None :
            # Le joueur choisi son action
            action, actionNum = chooseAction(player, adversaire, player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], player, pokemonActualPlayerNumber)
        # Si l'action du joueur est obligatoire
        else : 
            action = player.actionOblig[0]
            actionNum = player.actionOblig[1]

        # L'adversaire attaque et choisi une de ses 4 attaques au hasard
        action_adversaire, actionNum_adversaire = 1, rand(1, 4)

        # Si l'action du joueur est "Changer de pokemon" ou "Utiliser un objet"
        if action == 2 or action == 3 :
            # Le joueur joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        # Si l'action de l'adversaire est "Changer de pokemon" ou "Utiliser un objet"
        elif action_adversaire == 2 or action_adversaire == 3 :
            # L'adversaire joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        # Si le joueur utilise une attaque de priorité supérieure à l'adversaire
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].priorityLevel > adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire - 1].priorityLevel :
            # Le joueur joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        # Si l'adversaire utilise une attaque de priorité supérieure à le joueur
        elif player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].priorityLevel < adversaire.pokemons[pokemonActualAdversNumber].Attaques[actionNum_adversaire - 1].priorityLevel :
            # L'adversaire joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        # Si le pokemon du joueur est plus rapide que celui de l'adversaire
        elif player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
            # Le joueur joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
        # Si le pokemon de l'adversaire est plus rapide que le joueur
        elif player.pokemons[pokemonActualPlayerNumber].Speed < adversaire.pokemons[pokemonActualAdversNumber].Speed :
            # L'adversaire joue en premier
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")
        # Si les deux pokemons sont de même vitesse
        else :
            # La personne qui joue en premier est choisi aléatoirement
            if rand(1, 2) == 1 :
                player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "player")
            else :
                player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, "adversaire")

        # Vérification de la vampigraine sur le terrain
        player, adversaire = VampigraineCheck(player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain)

        # Fin du tour
        player, pokemonActualPlayerNumber = EndTurn(player, pokemonActualPlayerNumber, terrain)
        adversaire, pokemonActualAdversNumber = EndTurn(adversaire, pokemonActualAdversNumber, terrain)

        # Vérification si le combat est terminé
        if not CombatContinue(player, adversaire) :
            boolean = False

    
        