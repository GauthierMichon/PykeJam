def ChooseItem(player) :
    for i in range(len(player.inventaire)) :
        print(str(i + 1) + " : " + player.inventaire[i].name)
    actionNum = input("Quelle Objet utiliser ? ")

    return actionNum