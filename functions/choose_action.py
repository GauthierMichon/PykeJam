def chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire, dresseurPokemonSwitch, pokemonActualDresseurNum) :


    action = input("Quelle action faire ? (1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item)  ")

    if action == "1" :

        actionNum = input("Quelle Attaque utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3})  ".format(
            pokemon_actuel_player.Attaques[0].name,
            pokemon_actuel_player.Attaques[1].name,
            pokemon_actuel_player.Attaques[2].name,
            pokemon_actuel_player.Attaques[3].name
        ))

        #print(pokemon_actuel_player.Attaques[int(actionNum)-1].name)

    if action == "2" :

        booleanSwitch = True
        while booleanSwitch :
            actionNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
                player.pokemons[0].name,
                player.pokemons[1].name,
                player.pokemons[2].name,
                player.pokemons[3].name,
                player.pokemons[4].name,
                player.pokemons[5].name,
            ))
            actionNum = int(actionNum) - 1
            if actionNum == pokemonActualDresseurNum :
                print("Vous ne pouvez pas utiliser le pokemon actuel")
            elif dresseurPokemonSwitch.pokemons[actionNum].PV <= 0 :
                print("Vous ne pouvez pas utiliser ce pokemon, il est K.O.")
            else :
                booleanSwitch = False

        #print(player.pokemons[int(actionNum)-1])

        #pokemon_actuel_player = player.pokemons[int(pokemonNum)-1]
    
    if action == "3" :

        print("item")

    return int(action), int(actionNum)

        