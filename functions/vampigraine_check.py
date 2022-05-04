from math import ceil
from graph.write_info import WriteInfo
from graph.reload_graph_pokemons import ReloadGraphPokemons

# Fonction qui vérifie si la vampigraine est sur le terrain
def VampigraineCheck(player, adversaire, pokemonActualPlayerNumber, pokemonActualAdversNumber, terrain) :
    # Si le joueur a utilisé vampigraine
    if terrain.Vampigraine :
        WriteInfo("Vampigraine draine les PV du pokémon adverse !")
        drainPV = ceil(adversaire.pokemons[pokemonActualAdversNumber].PVMax / 8)
        if drainPV > adversaire.pokemons[pokemonActualAdversNumber].PV :
            drainPV = adversaire.pokemons[pokemonActualAdversNumber].PV
        player.pokemons[pokemonActualPlayerNumber].PV += drainPV
        adversaire.pokemons[pokemonActualAdversNumber].PV -= drainPV

    # Si l'adversaire a utilisé vampigraine
    if terrain.VampigraineAdverse :
        WriteInfo("Vampigraine draine les PV de votre pokémon !")
        drainPV = ceil(player.pokemons[pokemonActualPlayerNumber].PVMax / 8)
        if drainPV > player.pokemons[pokemonActualPlayerNumber].PV :
            drainPV = player.pokemons[pokemonActualPlayerNumber].PV
        adversaire.pokemons[pokemonActualAdversNumber].PV += drainPV
        player.pokemons[pokemonActualPlayerNumber].PV -= drainPV

    ReloadGraphPokemons(player.pokemons[pokemonActualPlayerNumber], adversaire.pokemons[pokemonActualAdversNumber])
    return player, adversaire