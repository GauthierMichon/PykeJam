from math import ceil
from functions.after_switch import AfterSwitch
from functions.choose_pokemon_change import ChoosePokemon
from functions.switch import Switch
from functions.switch_adversaire import ChangeAdversaire
from graph.write_info import WriteInfo

# Fonction qui gère la fin de tour d'un joueur
def EndTurn(dresseur, pokemonActualNumber, terrain) :
    # Si le pokemon est confus
    if dresseur.pokemons[pokemonActualNumber].confusion :
        # On diminue le temps de confusion
        dresseur.pokemons[pokemonActualNumber].confusionNum -= 1
        if dresseur.pokemons[pokemonActualNumber].confusionNum == 0 :
            dresseur.pokemons[pokemonActualNumber].confusion = False
            dresseur.pokemons[pokemonActualNumber].confusionNum = None
    
    # Le pokemon n'a plus peur et n'est plus protégé par abri
    dresseur.pokemons[pokemonActualNumber].afraid = False
    dresseur.pokemons[pokemonActualNumber].abri = False

    # Si le pokemon est soumis à l'attaque siphon
    if dresseur.pokemons[pokemonActualNumber].siphon :
        WriteInfo("Siphon fait perdre des PV à {} !".format(dresseur.pokemons[pokemonActualNumber].name))

        # Le pokemon perd 1/8 de ses PV maximum
        dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8))
        # On diminue le temps de l'attaque siphon
        dresseur.pokemons[pokemonActualNumber].siphonNum -= 1
        if dresseur.pokemons[pokemonActualNumber].siphonNum == 0 :
            dresseur.pokemons[pokemonActualNumber].siphon = False
            dresseur.pokemons[pokemonActualNumber].siphonNum = None

    # Si le pokemon est maudit 
    if dresseur.pokemons[pokemonActualNumber].maudit :
        WriteInfo("{} perd des PV à cause de la malédiction !".format(dresseur.pokemons[pokemonActualNumber].name))
        # Le pokemon perd 1/4 de ses PV maximum
        dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 4))

    # Si le pokemon soumis à l'attque requiem
    if dresseur.pokemons[pokemonActualNumber].requiem :
        # On diminue le temps de l'attaque requiem
        dresseur.pokemons[pokemonActualNumber].requiemNum -= 1
        # Si le temps est écoulé
        if dresseur.pokemons[pokemonActualNumber].requiemNum == 0 :
            WriteInfo("Le requiem arrive à son terme, {} est mis K.O. !".format(dresseur.pokemons[pokemonActualNumber].name))
            # Le pokemon est mis K.O.
            dresseur.pokemons[pokemonActualNumber].PV = 0

    # Si le pokemon est brulé
    if dresseur.pokemons[pokemonActualNumber].statut == "Brûlure" :
        WriteInfo("{} perd des PV à cause de sa brûlure !".format(dresseur.pokemons[pokemonActualNumber].name))
        # Le pokemon perd 1/16 de ses PV maximum
        dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 16))

    # Si le pokemon est empoisonné
    if dresseur.pokemons[pokemonActualNumber].statut == "Empoisonnement" :
        WriteInfo("{} perd des PV à cause de son empoisonnement !".format(dresseur.pokemons[pokemonActualNumber].name))
        # Le pokemon perd 1/8 de ses PV maximum
        dresseur.pokemons[pokemonActualNumber].PV -= int(ceil(dresseur.pokemons[pokemonActualNumber].PVMax / 8))

    # Si le pokemon est K.O.
    if dresseur.pokemons[pokemonActualNumber].PV <= 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0
        # Si le dresseur est l'adversaire
        if dresseur.person == "adversaire" :
            # S'il possède au moins un pokemon en vie
            if dresseur.pokemons[0].PV > 0 or dresseur.pokemons[1].PV > 0 or dresseur.pokemons[2].PV > 0 or dresseur.pokemons[3].PV > 0 or dresseur.pokemons[4].PV > 0 or dresseur.pokemons[5].PV > 0 :
                # Il change de pokemon
                dresseur = Switch(dresseur, pokemonActualNumber)
                pokemonActualNumber = ChangeAdversaire(dresseur, pokemonActualNumber)
                print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))
                dresseur = AfterSwitch(dresseur, pokemonActualNumber, terrain)
        # Si le dresseur est le joueur
        else :
            # S'il possède au moins un pokemon en vie
            if dresseur.pokemons[0].PV > 0 or dresseur.pokemons[1].PV > 0 or dresseur.pokemons[2].PV > 0 or dresseur.pokemons[3].PV > 0 or dresseur.pokemons[4].PV > 0 or dresseur.pokemons[5].PV > 0 :
                # Il change de pokemon
                dresseur = Switch(dresseur, pokemonActualNumber)
                pokemonActualNumber = ChoosePokemon(dresseur, pokemonActualNumber)
                print("vous envoyé {}".format(dresseur.pokemons[pokemonActualNumber].name))
                dresseur = AfterSwitch(dresseur, pokemonActualNumber, terrain)

    # Si le pokemon est K.O.
    if dresseur.pokemons[pokemonActualNumber].PV <= 0 :
        dresseur.pokemons[pokemonActualNumber].PV = 0
        """ dresseur, pokemonActualNumber = EndTurn(dresseur, pokemonActualNumber, terrain) """

    return dresseur, pokemonActualNumber
