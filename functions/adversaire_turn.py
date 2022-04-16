from functions.after_switch import AfterSwitch
from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.fight import fight
from functions.switch import Switch
import functions.player_turn as player_turn
from functions.switch_adversaire import ChangeAdversaire

# Fonction du tour de l'adversaire
def AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):
    # Si boolAttaque est True, l'attaque est effectuée
    boolAttaque = True
    # Si le pokemon adverse est gelé
    if adversaire.pokemons[pokemonActualAdversNumber].statut == "Gel" :
        # On fait un random entre 1 et 5
        if rand(1, 5) == 1 :
            # Le pokemon n'est plus gelé
            adversaire.pokemons[pokemonActualAdversNumber].statut = None
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus gelé !")
        else :
            # Le pokemon reste gelé et il n'attaque pas
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est gelé ! Il ne peut pas attaquer !")

    # Si le pokemon adverse est endormi
    elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Sommeil" :
        # On fait un random entre 1 et 5
        if rand(1, 5) == 1 :
            # Le pokemon n'est plus endormi
            adversaire.pokemons[pokemonActualAdversNumber].statut = None
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus endormi !")
        else :
            # Le pokemon reste endormi et il n'attaque pas
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est endormi ! Il ne peut pas attaquer !")
        
    # Si le pokemon adverse est paralysé
    elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Paralysie" :
        # On fait un random entre 1 et 4
        if rand(1, 4) == 1 :
            # Le pokemon souffre de la paralysie et il n'attaque pas
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est paralysé ! Il ne peut pas attaquer !")

    # Si boolAttaque est True, l'attaque est effectuée
    if boolAttaque :
        # Si l'action est "Attaquer"
        if action_adversaire == 1 :
            # On appelle la fonction fight
            adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], terrain, adversaire, pokemonActualAdversNumber = fight(adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], actionNum_adversaire, terrain, adversaire, pokemonActualAdversNumber)

        # Si l'action est "Changer de Pokemon"
        elif action_adversaire == 2 :
            print("votre adversaire envoie {}".format(adversaire.pokemons[actionNum_adversaire].name))
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
                # Le joueur choisi un nouveau pokemon
                action = 2
                actionNum = ChoosePokemon(player, pokemonActualPlayerNumber)
                print("vous envoyé {}".format(player.pokemons[actionNum].name))
                
            else :
                # Le joueur perd
                return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain

        # Tour du joueur
        player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = player_turn.PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
            