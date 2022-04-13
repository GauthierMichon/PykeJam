from math import ceil
from functions.choose_pokemon_change import ChoosePokemon
from functions.switch import Switch
from functions.switch_adversaire import ChangeAdversaire


def EndTurn(dresseur, pokemonActualNumber) :
    if dresseur.pokemons[pokemonActualNumber].confusion :
        dresseur.pokemons[pokemonActualNumber].confusionNum -= 1
        if dresseur.pokemons[pokemonActualNumber].confusionNum == 0 :
            dresseur.pokemons[pokemonActualNumber].confusion = False
            dresseur.pokemons[pokemonActualNumber].confusionNum = None
    
    dresseur.pokemons[pokemonActualNumber].afraid = False
    dresseur.pokemons[pokemonActualNumber].abri = False

    if dresseur.pokemons[pokemonActualNumber].siphon :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)
        dresseur.pokemons[pokemonActualNumber].siphonNum -= 1
        if dresseur.pokemons[pokemonActualNumber].siphonNum == 0 :
            dresseur.pokemons[pokemonActualNumber].siphon = False
            dresseur.pokemons[pokemonActualNumber].siphonNum = None

    if dresseur.pokemons[pokemonActualNumber].maudit :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4)

    if dresseur.pokemons[pokemonActualNumber].requiem :
        dresseur.pokemons[pokemonActualNumber].requiemNum -= 1
        if dresseur.pokemons[pokemonActualNumber].requiemNum == 0 :
            dresseur.pokemons[pokemonActualNumber].PV = 0

    if dresseur.pokemons[pokemonActualNumber].statut == "Brûlure" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 16)

    if dresseur.pokemons[pokemonActualNumber].statut == "Empoisonnement" :
        dresseur.pokemons[pokemonActualNumber].PV -= ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8)

    if dresseur.pokemons[pokemonActualNumber].PV <= 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0
        if dresseur.person == "adversaire" :
            if dresseur.pokemons[0].PV > 0 or dresseur.pokemons[1].PV > 0 or dresseur.pokemons[2].PV > 0 or dresseur.pokemons[3].PV > 0 or dresseur.pokemons[4].PV > 0 or dresseur.pokemons[5].PV > 0 :
                dresseur = Switch(dresseur, pokemonActualNumber)
                pokemonActualNumber = ChangeAdversaire(dresseur, pokemonActualNumber)
                print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))
        else :
            if dresseur.pokemons[0].PV > 0 or dresseur.pokemons[1].PV > 0 or dresseur.pokemons[2].PV > 0 or dresseur.pokemons[3].PV > 0 or dresseur.pokemons[4].PV > 0 or dresseur.pokemons[5].PV > 0 :
                dresseur = Switch(dresseur, pokemonActualNumber)
                pokemonActualNumber = ChoosePokemon(dresseur, pokemonActualNumber)
                print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))

    return dresseur, pokemonActualNumber
