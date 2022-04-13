def ChoosePokemon(player, pokemonActualDresseurNum) :
    booleanSwitch = True
    while booleanSwitch :
        pokemonNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
            player.pokemons[0].name,
            player.pokemons[1].name,
            player.pokemons[2].name,
            player.pokemons[3].name,
            player.pokemons[4].name,
            player.pokemons[5].name,
        ))
        pokemonNum = int(pokemonNum) - 1
        if pokemonNum == pokemonActualDresseurNum :
            print("Vous ne pouvez pas utiliser le pokemon actuel")
        elif player.pokemons[pokemonNum].PV <= 0 :
            print("Vous ne pouvez pas utiliser ce pokemon, il est K.O.")
        else :
            booleanSwitch = False

    return pokemonNum