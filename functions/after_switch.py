from math import ceil
from functions.table_types import TableType


def AfterSwitch(dresseur, pokemonActualNumber, terrain) :
    if dresseur.person == "player" :
        if terrain.PiegeDeRocAdverse != None and dresseur.pokemons[pokemonActualNumber].Type != "Vol" and dresseur.pokemons[pokemonActualNumber].Type2 != "Vol"  :
            eff = TableType("Roche", dresseur.pokemons[pokemonActualNumber].Type, dresseur.pokemons[pokemonActualNumber].Type2)
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax * eff / 8)

        if terrain.PicotsAdverse == 1 :
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)
        elif terrain.PicotsAdverse == 2 :
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 6)
        elif terrain.PicotsAdverse == 3 :
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4)

        if terrain.PicsToxikAdverse != None and dresseur.pokemons[pokemonActualNumber].statut == None and dresseur.pokemons[pokemonActualNumber].Type != "Poison" and dresseur.pokemons[pokemonActualNumber].Type2 != "Poison" :
            dresseur.pokemons[pokemonActualNumber].statut = "Empoisonnement"

    elif dresseur.person == "adversaire" :
        if terrain.PiegeDeRoc != None and dresseur.pokemons[pokemonActualNumber].Type != "Vol" and dresseur.pokemons[pokemonActualNumber].Type2 != "Vol"  :
            eff = TableType("Roche", dresseur.pokemons[pokemonActualNumber].Type, dresseur.pokemons[pokemonActualNumber].Type2)
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax * eff / 8)
        
        if terrain.Picots == 1 :
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)
        elif terrain.Picots == 2 : 
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 6)
        elif terrain.Picots == 3 :
            dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4)

        if terrain.PicsToxik != None and dresseur.pokemons[pokemonActualNumber].statut == None and dresseur.pokemons[pokemonActualNumber].Type != "Poison" and dresseur.pokemons[pokemonActualNumber].Type2 != "Poison" :
            dresseur.pokemons[pokemonActualNumber].statut = "Empoisonnement"
    
    if dresseur.pokemons[pokemonActualNumber].PV < 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0

    return dresseur
            