def round(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire) :

    if pokemon_actuel_player.speed > pokemon_actuel_adversaire.speed :

        action = input("Quelle action faire : 1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item")

        if action == "1" :

            attaquenum = input("Quelle Attaque utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3})".format(
                pokemon_actuel_player.Attaques[0],
                pokemon_actuel_player.Attaques[1],
                pokemon_actuel_player.Attaques[2],
                pokemon_actuel_player.Attaques[3]
            ))

            print(pokemon_actuel_player[int(attaquenum)-1])

        