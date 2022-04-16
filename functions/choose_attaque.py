def ChooseAttaque(pokemon_actuel_player) :
    actionNum = input("Quelle Attaque utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3})  ".format(
        pokemon_actuel_player.Attaques[0].name,
        pokemon_actuel_player.Attaques[1].name,
        pokemon_actuel_player.Attaques[2].name,
        pokemon_actuel_player.Attaques[3].name
    ))

    return actionNum