from math import ceil
from graph.write_info import WriteInfo
from graph.reload_graph_pokemons import ReloadGraphPokemons

# Fonction qui vérifie si la vampigraine est sur le terrain
def VampigraineCheck(player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain) :
    # Si le joueur a utilisé vampigraine
    if terrain.Vampigraine :
        WriteInfo("Vampigraine draine les PV du pokémon adverse !")
        drainPV = int(ceil(adversaire.pokemons[pokemonActualAdversNumber].PVMax / 8))
        if drainPV > adversaire.pokemons[pokemonActualAdversNumber].PV :
            drainPV = adversaire.pokemons[pokemonActualAdversNumber].PV
        player.pokemons[pokemonActualPlayerNumber].PV += drainPV
        adversaire.pokemons[pokemonActualAdversNumber].PV -= drainPV
        if player.pokemons[pokemonActualAdversNumber].PV > player.pokemons[pokemonActualAdversNumber].PVMax :
            player.pokemons[pokemonActualAdversNumber].PV = player.pokemons[pokemonActualAdversNumber].PVMax

    # Si l'adversaire a utilisé vampigraine
    if terrain.VampigraineAdverse :
        WriteInfo("Vampigraine draine les PV de votre pokémon !")
        drainPV = int(ceil(player.pokemons[pokemonActualPlayerNumber].PVMax / 8))
        if drainPV > player.pokemons[pokemonActualPlayerNumber].PV :
            drainPV = player.pokemons[pokemonActualPlayerNumber].PV
        adversaire.pokemons[pokemonActualAdversNumber].PV += drainPV
        player.pokemons[pokemonActualPlayerNumber].PV -= drainPV
        if adversaire.pokemons[pokemonActualAdversNumber].PV > adversaire.pokemons[pokemonActualAdversNumber].PVMax :
            adversaire.pokemons[pokemonActualAdversNumber].PV = adversaire.pokemons[pokemonActualAdversNumber].PVMax

    ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
    return player, adversaire