from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.fight import fight
from functions.switch import Switch
import functions.player_turn as player_turn


def AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):

    boolAttaque = True
    if adversaire.pokemons[pokemonActualAdversNumber].statut == "Gel" :
        if rand(1, 5) == 1 :
            adversaire.pokemons[pokemonActualAdversNumber].statut = None
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus gelé !")
        else :
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est gelé ! Il ne peut pas attaquer !")

    elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Sommeil" :
        if rand(1, 5) == 1 :
            adversaire.pokemons[pokemonActualAdversNumber].statut = None
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " n'est plus endormi !")
        else :
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est endormi ! Il ne peut pas attaquer !")
        
    elif adversaire.pokemons[pokemonActualAdversNumber].statut == "Paralysie" :
        if rand(1, 4) == 1 :
            boolAttaque = False
            print(adversaire.pokemons[pokemonActualAdversNumber].name + " est paralysé ! Il ne peut pas attaquer !")


    if boolAttaque :
        if action_adversaire == 1 :
            adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], terrain, adversaire, pokemonActualAdversNumber = fight(adversaire.pokemons[pokemonActualAdversNumber], player.pokemons[pokemonActualPlayerNumber], actionNum_adversaire, terrain, adversaire, pokemonActualAdversNumber)

        elif action_adversaire == 2 :
            print("votre adversaire envoie {}".format(adversaire.pokemons[actionNum_adversaire].name))
            adversaire = Switch(adversaire, pokemonActualAdversNumber)
            pokemonActualAdversNumber = actionNum_adversaire

        elif action_adversaire == 3 :
            print("item mais pas encore implémenté")

    if beginner == "adversaire" :
        if player.pokemons[pokemonActualPlayerNumber].PV <= 0 :
            if player.pokemons[0].PV > 0 or player.pokemons[1].PV > 0 or player.pokemons[2].PV > 0 or player.pokemons[3].PV > 0 or player.pokemons[4].PV > 0 or player.pokemons[5].PV > 0 :
                action = 2
                actionNum = ChoosePokemon(player, pokemonActualPlayerNumber)
                print("vous envoyé {}".format(player.pokemons[actionNum].name))

            else :
                return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain

        player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = player_turn.PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
            