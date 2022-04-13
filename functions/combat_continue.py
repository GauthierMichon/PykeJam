def CombatContinue(player, adversaire) :
    if player.pokemons[0].PV <= 0 and player.pokemons[1].PV <= 0 and player.pokemons[2].PV <= 0 and player.pokemons[3].PV <= 0 and player.pokemons[4].PV <= 0 and player.pokemons[5].PV <= 0 :
        print("Vous avez perdu")
        return False
    elif adversaire.pokemons[0].PV <= 0 and adversaire.pokemons[1].PV <= 0 and adversaire.pokemons[2].PV <= 0 and adversaire.pokemons[3].PV <= 0 and adversaire.pokemons[4].PV <= 0 and adversaire.pokemons[5].PV <= 0 :
        print("Vous avez gagné")
        return False
    else :
        return True