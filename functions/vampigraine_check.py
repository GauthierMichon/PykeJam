from math import ceil

# Fonction qui vérifie si la vampigraine est sur le terrain
def VampigraineCheck(player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain) :
    # Si le joueur a utilisé vampigraine
    if terrain.Vampigraine :
        drainPV = ceil(adversaire.pokemons[pokemonActualAdversNumber].PVMax / 8)
        if drainPV > adversaire.pokemons[pokemonActualAdversNumber].PV :
            drainPV = adversaire.pokemons[pokemonActualAdversNumber].PV
        player.pokemons[pokemonActualPlayerNumber].PV += drainPV
        adversaire.pokemons[pokemonActualAdversNumber].PV -= drainPV

    # Si l'adversaire a utilisé vampigraine
    if terrain.VampigraineAdverse :
        drainPV = ceil(player.pokemons[pokemonActualPlayerNumber].PVMax / 8)
        if drainPV > player.pokemons[pokemonActualPlayerNumber].PV :
            drainPV = player.pokemons[pokemonActualPlayerNumber].PV
        adversaire.pokemons[pokemonActualAdversNumber].PV += drainPV
        player.pokemons[pokemonActualPlayerNumber].PV -= drainPV

    return player, adversaire