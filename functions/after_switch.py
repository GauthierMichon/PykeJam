from math import ceil
from functions.table_types import TableType
from graph.write_info import WriteInfo


def AfterSwitch(dresseur, pokemonActualNumber, terrain) :
    # Si le dresseur qui a changé de pokemon est le joueur
    if dresseur.person == "player" :
        # Si les pièges de rocs adverse sont activés et que le pokemon n'est pas de type vol
        if terrain.PiegeDeRocAdverse != None and dresseur.pokemons[pokemonActualNumber].Type != "Vol" and dresseur.pokemons[pokemonActualNumber].Type2 != "Vol"  :
            WriteInfo("{} est bléssé par les Pièges de Roc".format(dresseur.pokemons[pokemonActualNumber].name))
            # Inflige des dégâts en fonction de la faiblesse au type roche
            eff = TableType("Roche", dresseur.pokemons[pokemonActualNumber].Type, dresseur.pokemons[pokemonActualNumber].Type2)
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax * eff / 8))

        # Si les picots adverses sont activés
        # 1 fois
        if terrain.PicotsAdverse == 1 :
            WriteInfo("{} est bléssé par les Picots".format(dresseur.pokemons[pokemonActualNumber].name))
            # Inflige 12.5% des PV max du pokemon
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8))
        # 2 fois
        elif terrain.PicotsAdverse == 2 :
            WriteInfo("{} est bléssé par les Picots".format(dresseur.pokemons[pokemonActualNumber].name))
            # Inflige 16.66% des PV max du pokemon
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 6))
        # 3 fois
        elif terrain.PicotsAdverse == 3 :
            WriteInfo("{} est bléssé par les Picots".format(dresseur.pokemons[pokemonActualNumber].name))
            # Inflige 25% des PV max du pokemon
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4))

        # Si les pics toxik adverses sont activés, qu'il n'a pas de problème de statut et qu'il n'est pas de type poison
        if terrain.PicsToxikAdverse != None and dresseur.pokemons[pokemonActualNumber].statut == None and dresseur.pokemons[pokemonActualNumber].Type != "Poison" and dresseur.pokemons[pokemonActualNumber].Type2 != "Poison" :
            WriteInfo("{} est empoisonné par les Pics Toxik".format(dresseur.pokemons[pokemonActualNumber].name))
            dresseur.pokemons[pokemonActualNumber].statut = "Empoisonnement"

    # Si le dresseur qui a changé de pokemon est l'adversaire
    elif dresseur.person == "adversaire" :
        # Si les pièges de rocs du joueur sont activés et que le pokemon n'est pas de type vol
        if terrain.PiegeDeRoc != None and dresseur.pokemons[pokemonActualNumber].Type != "Vol" and dresseur.pokemons[pokemonActualNumber].Type2 != "Vol"  :
            WriteInfo("{} ennemi est bléssé par les picots".format(dresseur.pokemons[pokemonActualNumber].name))
            eff = TableType("Roche", dresseur.pokemons[pokemonActualNumber].Type, dresseur.pokemons[pokemonActualNumber].Type2)
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax * eff / 8))
        
        # Si les picots du joueur sont activés
        # 1 fois
        if terrain.Picots == 1 :
            WriteInfo("{} ennemi est bléssé par les picots".format(dresseur.pokemons[pokemonActualNumber].name))
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8))
        # 2 fois
        elif terrain.Picots == 2 : 
            WriteInfo("{} ennemi est bléssé par les picots".format(dresseur.pokemons[pokemonActualNumber].name))
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 6))
        # 3 fois
        elif terrain.Picots == 3 :
            WriteInfo("{} ennemi est bléssé par les picots".format(dresseur.pokemons[pokemonActualNumber].name))
            dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4))

        # Si les pics toxik du joueur sont activés, qu'il n'a pas de problème de statut et qu'il n'est pas de type poison
        if terrain.PicsToxik != None and dresseur.pokemons[pokemonActualNumber].statut == None and dresseur.pokemons[pokemonActualNumber].Type != "Poison" and dresseur.pokemons[pokemonActualNumber].Type2 != "Poison" :
            WriteInfo("{} ennemi est empoisonné par les Pics Toxik".format(dresseur.pokemons[pokemonActualNumber].name))
            dresseur.pokemons[pokemonActualNumber].statut = "Empoisonnement"
    
    if dresseur.pokemons[pokemonActualNumber].PV < 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0

    return dresseur
            