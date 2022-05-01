from math import ceil
import graph.graph as graph
from graph.graph_containers import *


def ActionItemRes(dresseur, item) :

    pokemonNum = ChoosePokemonToRes(dresseur)
    dresseur.pokemons[pokemonNum].PV = ceil(dresseur.pokemons[pokemonNum].PVMax * item.PV)

    return dresseur




def ChoosePokemonToRes(dresseur) :
    """ pokemonNum = input("Quelle Pokemon utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3}, 5 : {4}, 6 : {5})  ".format(
        dresseur.pokemons[0].name,
        dresseur.pokemons[1].name,
        dresseur.pokemons[2].name,
        dresseur.pokemons[3].name,
        dresseur.pokemons[4].name,
        dresseur.pokemons[5].name,
    ))
    pokemonNum = int(pokemonNum) - 1
    if dresseur.pokemons[pokemonNum].PV > 0 :
        print("Ce pokemon n'est pas K.O.")
        return ChoosePokemonToRes(dresseur) """

    text_pokemon1 = font.render('{0}'.format(dresseur.pokemons[0].name), False, BLACK)
    text_pokemon2 = font.render('{0}'.format(dresseur.pokemons[1].name), False, BLACK)
    text_pokemon3 = font.render('{0}'.format(dresseur.pokemons[2].name), False, BLACK)
    text_pokemon4 = font.render('{0}'.format(dresseur.pokemons[3].name), False, BLACK)
    text_pokemon5 = font.render('{0}'.format(dresseur.pokemons[4].name), False, BLACK)
    text_pokemon6 = font.render('{0}'.format(dresseur.pokemons[5].name), False, BLACK)

    pokemonNum = None
    running = True
    while running :

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

            
        if pokemonNum != None :
            if dresseur.pokemons[pokemonNum].PV > 0 :
                print("Ce pokemon n'est pas K.O.")
                # return ChoosePokemonToRes(dresseur)
            else :
                running = False

        pygame.display.flip()
    

    return pokemonNum