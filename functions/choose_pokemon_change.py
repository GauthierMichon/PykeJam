import graph.graph as graph
from graph.graph_containers import *
import time

# Fonction permettant de choisir un pokemon
def ChoosePokemon(player, pokemonActualDresseurNum) :

    text_pokemon1 = font.render('{0}'.format(player.pokemons[0].name), False, BLACK)
    text_pokemon2 = font.render('{0}'.format(player.pokemons[1].name), False, BLACK)
    text_pokemon3 = font.render('{0}'.format(player.pokemons[2].name), False, BLACK)
    text_pokemon4 = font.render('{0}'.format(player.pokemons[3].name), False, BLACK)
    text_pokemon5 = font.render('{0}'.format(player.pokemons[4].name), False, BLACK)
    text_pokemon6 = font.render('{0}'.format(player.pokemons[5].name), False, BLACK)
    text_pokemon_PV_player = pokemon_PV_player.render('{0} / {1}'.format(player.pokemons[pokemonActualDresseurNum].PV, player.pokemons[pokemonActualDresseurNum].PVMax), False, BLACK)
    text_pokemon_name_player = pokemon_name_player.render('{0}'.format(player.pokemons[pokemonActualDresseurNum].name), False, BLACK)


    pokemonNum = None
    running = True
    while running :
        # Affiche les pokemons du dresseur et demande au joueur de choisir un pokemon
        """ pokemonNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
            player.pokemons[0].name,
            player.pokemons[1].name,
            player.pokemons[2].name,
            player.pokemons[3].name,
            player.pokemons[4].name,
            player.pokemons[5].name,
        ))
        pokemonNum = int(pokemonNum) - 1 """


        graph.screen.blit(info_pokemon_player, rect_8)
        graph.screen.blit(text_pokemon_name_player, rect_pokemon_player_name)
        graph.screen.blit(text_pokemon_PV_player, rect_pokemon_player_PV)
        

        graph.screen.blit(actions_pokemon, rect_actions_pokemon)
        graph.screen.blit(pokemon1, rect_pokemon1)
        graph.screen.blit(text_pokemon1, rect_pokemon1)
        graph.screen.blit(pokemon2, rect_pokemon2)
        graph.screen.blit(text_pokemon2, rect_pokemon2)
        graph.screen.blit(pokemon3, rect_pokemon3)
        graph.screen.blit(text_pokemon3, rect_pokemon3)
        graph.screen.blit(pokemon4, rect_pokemon4)
        graph.screen.blit(text_pokemon4, rect_pokemon4)
        graph.screen.blit(pokemon5, rect_pokemon5)
        graph.screen.blit(text_pokemon5, rect_pokemon5)
        graph.screen.blit(pokemon6, rect_pokemon6)
        graph.screen.blit(text_pokemon6, rect_pokemon6)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                pokemonNum = 0

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pokemonNum = 1

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                pokemonNum = 2

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                pokemonNum = 3

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                pokemonNum = 4

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                pokemonNum = 5

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                running = False

        

        pygame.display.flip()

        # Si le pokemon choisi est déjà celui envoyé
        if pokemonNum != None :
            if pokemonNum == pokemonActualDresseurNum :
                print("Vous ne pouvez pas utiliser le pokemon actuel")
                pokemonNum = None
            # Si le pokemon choisi est K.O.
            elif player.pokemons[pokemonNum].PV <= 0 :
                print("Vous ne pouvez pas utiliser ce pokemon, il est K.O.")
                pokemonNum = None
            else :
                running = False

    return pokemonNum