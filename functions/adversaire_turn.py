from functions.after_switch import AfterSwitch
from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.action_attaque import ActionAttaque
from functions.switch import Switch
import functions.player_turn as player_turn
from functions.switch_adversaire import ChangeAdversaire
from graph.reload_graph_pokemons import ReloadGraphPokemons
from graph.write_info import WriteInfo
import time
from graph.change_pokemon_graph import ChangePokemonGraph

# Fonction du tour de l'adversaire
def AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):
    ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
    
    # Si boolAttaque est True, l'attaque est effectuée
    boolAttaque = True
    
    # Si l'action est "Attaquer"
    if action_adversaire == 1 :
        # Si le pokemon adverse est gelé
        if adversaire.pokemons[pokemonActualAdversNumber].statut == "Gel" :
            # On fait un random entre 1 et 5
            if rand(1, 5) == 1 :
                ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus gelé !")
                # Le pokemon n'est plus gelé
                adversaire.pokemons[pokemonActualAdversNumber].statut = None
                print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus gelé !")
            else :
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " est gelé ! Il ne peut pas attaquer !")
                # Le pokemon reste gelé et il n'attaque pas
                boolAttaque = False
                print(adversaire.pokemons[pokemonActualAdversNumber].name + " est gelé ! Il ne peut pas attaquer !")

        # Si le pokemon adverse est endormi
        elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Sommeil" :
            # On fait un random entre 1 et 5
            if rand(1, 5) == 1 :
                ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus endormi !")
                # Le pokemon n'est plus endormi
                adversaire.pokemons[pokemonActualAdversNumber].statut = None
                print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus endormi !")
            else :
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " est endormi ! Il ne peut pas attaquer !")
                # Le pokemon reste endormi et il n'attaque pas
                boolAttaque = False
                print(adversaire.pokemons[pokemonActualAdversNumber].name + " est endormi ! Il ne peut pas attaquer !")
            
        # Si le pokemon adverse est paralysé
        elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Paralysie" :
            # On fait un random entre 1 et 4
            if rand(1, 4) == 1 :
                WriteInfo(adversaire.pokemons[pokemonActualAdversNumber].name + " est paralysé ! Il ne peut pas attaquer !")
                # Le pokemon souffre de la paralysie et il n'attaque pas
                boolAttaque = False
                print(adversaire.pokemons[pokemonActualAdversNumber].name + " est paralysé ! Il ne peut pas attaquer !")

        # Si boolAttaque est True, l'attaque est effectuée
        if boolAttaque :
            # On appelle la fonction ActionAttaque
            adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], terrain, adversaire, player, pokemonActualAdversNumber, pokemonActualPlayerNumber = ActionAttaque(adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], actionNum_adversaire, terrain, adversaire, player, pokemonActualAdversNumber, pokemonActualPlayerNumber)
            ChangePokemonGraph(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])

    # Si l'action est "Changer de Pokemon"
    elif action_adversaire == 2 :
        WriteInfo("Votre adversaire envoie {}".format(adversaire.pokemons[actionNum_adversaire].name))
        ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
        # On appelle la fonction Switch qui réinitialise certaines données du pokemon actuel adverse
        adversaire = Switch(adversaire, pokemonActualAdversNumber)
        # Le pokemon adverse change
        pokemonActualAdversNumber = actionNum_adversaire
        # On appelle la fonction AfterSwitch qui effectue des actions en fontions du terrain
        adversaire = AfterSwitch(adversaire, pokemonActualAdversNumber, terrain)
        # Si le pokemon adverse est K.O.
        if adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            adversaire.pokemons[pokemonActualAdversNumber].PV = 0
            # On appelle la fonction ChangeAdversaire qui choisi un nouveau pokemon adverse
            actionNum = ChangeAdversaire(adversaire, pokemonActualAdversNumber)
            # L'adversaire change de pokemon
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    # Si l'action est "Utiliser un objet"
    elif action_adversaire == 3 :
        print("item mais pas encore implémenté")

    # Si l'adversaire a joué en premier
    if beginner == "adversaire" :
        # Si le pokemon du joueur est K.O.
        if player.pokemons[pokemonActualPlayerNumber].PV <= 0 :
            # S'il reste au moins un pokemon au joueur
            if player.pokemons[0].PV > 0 or player.pokemons[1].PV > 0 or player.pokemons[2].PV > 0 or player.pokemons[3].PV > 0 or player.pokemons[4].PV > 0 or player.pokemons[5].PV > 0 :
                ChangePokemonGraph(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
                WriteInfo(player.pokemons[pokemonActualPlayerNumber].name + " est K.O.")
                # Le joueur choisi un nouveau pokemon
                action = 2
                actionNum = ChoosePokemon(player, pokemonActualPlayerNumber)
                print("vous envoyé {}".format(player.pokemons[actionNum].name))
                player.actionOblig = None
                player.actionOblig = None
                
            else :
                # Le joueur perd
                return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain

        # Tour du joueur
        player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = player_turn.PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
            