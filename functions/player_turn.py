from functions.after_switch import AfterSwitch
from functions.choose_pokemon_change import ChoosePokemon
from functions.choose_random_num import rand
from functions.fight import fight
from functions.switch import Switch
import functions.adversaire_turn as adv_turn
from functions.switch_adversaire import ChangeAdversaire


def PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):
    boolAttaque = True
    if player.pokemons[pokemonActualPlayerNumber].statut == "Gel" :
        if rand(1, 5) == 1 :
            player.pokemons[pokemonActualPlayerNumber].statut = None
            print(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus gelé !")
        else :
            boolAttaque = False
            print(player.pokemons[pokemonActualPlayerNumber].name + " est gelé ! Il ne peut pas attaquer !")

    elif player.pokemons[pokemonActualPlayerNumber].statut == "Sommeil" :
        if rand(1, 5) == 1 :
            player.pokemons[pokemonActualPlayerNumber].statut = None
            print(player.pokemons[pokemonActualPlayerNumber].name + " n'est plus endormi !")
        else :
            boolAttaque = False
            print(player.pokemons[pokemonActualPlayerNumber].name + " est endormi ! Il ne peut pas attaquer !")
    elif player.pokemons[pokemonActualPlayerNumber].statut == "Paralysie" :
        if rand(1, 4) == 1 :
            boolAttaque = False
            print(player.pokemons[pokemonActualPlayerNumber].name + " est paralysé ! Il ne peut pas attaquer !")
        

    if boolAttaque :
        if action == 1 :
            print("\nVous avez choisi de faire une attaque")
            print(player.pokemons[pokemonActualPlayerNumber].name)
            print(player.pokemons[pokemonActualPlayerNumber].Attaques[actionNum - 1].name)
            #if player.pokemons[pokemonActualPlayerNumber].Speed > adversaire.pokemons[pokemonActualAdversNumber].Speed :
                #print("PV Avant :", adversaire.pokemons[pokemonActualAdversNumber].PV)
            player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], terrain, player, pokemonActualPlayerNumber = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player, pokemonActualPlayerNumber)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)

        elif action == 2 :
            print("\nVous avez choisi de changer de pokemon")
            print("vous envoyé {}".format(player.pokemons[actionNum].name))
            player = Switch(player, pokemonActualPlayerNumber)
            pokemonActualPlayerNumber = actionNum
            player = AfterSwitch(player, pokemonActualPlayerNumber, terrain)
            if player.pokemons[pokemonActualPlayerNumber].PV <= 0 :
                player.pokemons[pokemonActualPlayerNumber].PV = 0
                actionNum = ChoosePokemon(player, pokemonActualPlayerNumber)
                player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

        elif action == 3 :
            print("item mais pas encore implémenté")

    if beginner == "player" :
        if adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            if adversaire.pokemons[0].PV > 0 or adversaire.pokemons[1].PV > 0 or adversaire.pokemons[2].PV > 0 or adversaire.pokemons[3].PV > 0 or adversaire.pokemons[4].PV > 0 or adversaire.pokemons[5].PV > 0 :
                action_adversaire = 2
                actionNum_adversaire = ChangeAdversaire(adversaire, pokemonActualAdversNumber)
        
            else :
                return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain

        player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = adv_turn.AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
    
            