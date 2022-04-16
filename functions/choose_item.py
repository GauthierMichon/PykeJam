def ChooseItem(player) :
    actionNum = input("Quelle Objet utiliser ? (1 : {0}, 2 : {1}, 3 : {2})  ".format(
        player.inventaire[0].name,
        player.inventaire[1].name,
        player.inventaire[2].name
    ))

    return actionNum