def Switch(dresseurPokemonSwitch, pokemonActualDresseurNum) :
    booleanSwitch = True
    while booleanSwitch :
        newPokemonNum = input("Entrez le numéro du pokemon que vous voulez utiliser : ")
        if newPokemonNum == pokemonActualDresseurNum :
            print("Vous ne pouvez pas utiliser le pokemon actuel")
        elif dresseurPokemonSwitch[newPokemonNum].PV <= 0 :
            print("Vous ne pouvez pas utiliser ce pokemon, il est K.O.")
        else :
            print("{} a été envoyé".format(dresseurPokemonSwitch[newPokemonNum].name))
            booleanSwitch = False

    
    return newPokemonNum