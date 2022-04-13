from functions.choose_random_num import rand
from functions.fight import fight
from functions.switch import Switch
import functions.adversaire_turn as adv_turn


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
            player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], terrain, player = fight(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber], actionNum, terrain, player)
                #print("PV Après :", adversaire.pokemons[pokemonActualAdversNumber].PV)

        elif action == 2 :
            print("\nVous avez choisi de changer de pokemon")
            print("vous envoyé {}".format(player.pokemons[actionNum].name))
            player = Switch(player, pokemonActualPlayerNumber)
            pokemonActualPlayerNumber = actionNum

        elif action == 3 :
            print("item mais pas encore implémenté")

    if beginner == "player" :
        if adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            action_adversaire = 2
            if pokemonActualAdversNumber < 5 :
                actionNum_adversaire = pokemonActualAdversNumber + 1
        
        if pokemonActualAdversNumber == 5 and adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
        else :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = adv_turn.AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
    
            