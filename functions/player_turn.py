import time
from graph.reload_graph_pokemons import ReloadGraphPokemons
from functions.action_item import ActionItem
from functions.after_switch import AfterSwitch
from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.action_attaque import ActionAttaque
from functions.switch import Switch
import functions.adversaire_turn as adv_turn
from functions.switch_adversaire import ChangeAdversaire
from graph.write_info import WriteInfo
from graph.change_pokemon_graph import ChangePokemonGraph

# Fonction du tour du joueur
def PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):
    
    ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
    
    # Si boolAttaque est True, l'attaque est effectuée
    boolAttaque = True
    
    # Si l'action est "Attaquer"
    if action == 1 :
        # Si le pokemon du joueur est gelé
        if player.pokemons[pokemonActualPlayerNumber].statut == "Gel" :
            # On fait un random entre 1 et 5
            if rand(1, 5) == 1 :
                ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus gelé !")
                # Le pokemon n'est plus gelé
                player.pokemons[pokemonActualPlayerNumber].statut = None
                print(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus gelé !")
            else :
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " est gelé ! Il ne peut pas attaquer !")
                # Le pokemon reste gelé et il n'attaque pas
                boolAttaque = False
                print(player.pokemons[pokemonActualPlayerNumber].name + " est gelé ! Il ne peut pas attaquer !")

        # Si le pokemon du joueur est endormi
        elif player.pokemons[pokemonActualPlayerNumber].statut == "Sommeil" and player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum-1].id != 12 :
            # On fait un random entre 1 et 5
            if rand(1, 5) == 1 :
                ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus endormi !")
                # Le pokemon n'est plus endormi
                player.pokemons[pokemonActualPlayerNumber].statut = None
                print(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus endormi !")
            else :
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " est endormi ! Il ne peut pas attaquer !")

                # Le pokemon reste endormi et il n'attaque pas
                boolAttaque = False
                print(player.pokemons[pokemonActualPlayerNumber].name + " est endormi ! Il ne peut pas attaquer !")

        # Si le pokemon du joueur est paralysé
        elif player.pokemons[pokemonActualPlayerNumber].statut == "Paralysie" :
            # On fait un random entre 1 et 4
            if rand(1, 4) == 1 :
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " est paralysé ! Il ne peut pas attaquer !")
                # Le pokemon souffre de la paralysie et il n'attaque pas
                boolAttaque = False
                print(player.pokemons[pokemonActualPlayerNumber].name + " est paralysé ! Il ne peut pas attaquer !")

        # Si boolAttaque est True, l'attaque est effectuée
        if boolAttaque :
            print("\nVous avez choisi de faire une attaque")
            print(player.pokemons[pokemonActualPlayerNumber].name)
            print(player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].name)
            # On appelle la fonction ActionAttaque
            player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], terrain, player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber = ActionAttaque(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber)
            ChangePokemonGraph(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])

    # Si l'action est "Changer de Pokemon"
    elif action == 2 :
        print("\nVous avez choisi de changer de pokemon")
        ChangePokemonGraph(player.pokemons[actionNum], adversaire.pokemons[pokemonActualAdversNumber])
        WriteInfo("Vous envoyez {}".format(player.pokemons[actionNum].name))
        

        # On appelle la fonction Switch qui réinitialise certaines données du pokemon actuel du joueur
        player = Switch(player, pokemonActualPlayerNumber)
        # Le pokemon adverse change
        pokemonActualPlayerNumber = actionNum
        # On appelle la fonction AfterSwitch qui effectue des actions en fontions du terrain
        player = AfterSwitch(player, pokemonActualPlayerNumber, terrain)
        # Si le pokemon du joueur est K.O.
        if player.pokemons[pokemonActualPlayerNumber].PV <= 0 :
            player.pokemons[pokemonActualPlayerNumber].PV = 0
            # Le joueur choisi un nouveau pokemon
            actionNum = ChoosePokemon(player, pokemonActualPlayerNumber)
            # Le joueur change de pokemon
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    # Si l'action est "Utiliser un objet"
    elif action == 3 :
        print("\nVous avez choisi d'utiliser un objet")
        print(player.inventaire[actionNum - 1].name)
        WriteInfo(player.inventaire[actionNum - 1].name + " est utilisé")
        player = ActionItem(player, actionNum - 1, pokemonActualPlayerNumber)
        print(player.inventaire, len(player.inventaire))

    # Si le joueur a joué en premier
    if beginner == "player" :
        # Si le pokemon de l'adversaire est K.O.
        if adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            # S'il reste au moins un pokemon à l'adversaire
            if adversaire.pokemons[0].PV > 0 or adversaire.pokemons[1].PV > 0 or adversaire.pokemons[2].PV > 0 or adversaire.pokemons[3].PV > 0 or adversaire.pokemons[4].PV > 0 or adversaire.pokemons[5].PV > 0 :
                
                ChangePokemonGraph(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                (player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " est K.O.")
                # L'adversaire choisi un nouveau pokemon
                action_adversaire = 2
                actionNum_adversaire = ChangeAdversaire(adversaire, pokemonActualAdversNumber)
                adversaire.actionOblig = None
                adversaire.actionOblig = None

        
            else :
                # L'adversaire perd
                return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain

        # Tour de l'adversaire
        player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = adv_turn.AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
    
            