from functions.fight import fight
from functions.switch import Switch
import functions.adversaire_turn as adv_turn


def PlayerTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner):


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
                print("votre adversaire envoie {}".format(adversaire.pokemons[actionNum_adversaire].name))

        
        
        if pokemonActualAdversNumber == 5 and adversaire.pokemons[pokemonActualAdversNumber].PV <= 0 :
            return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
        else :
            player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain = adv_turn.AdversaireTurn(player, adversaire, action, actionNum, action_adversaire, actionNum_adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain, beginner)

    return player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain
    
            