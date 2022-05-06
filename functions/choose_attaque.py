from cProfile import run
from graph.color_attaques import ColorAttaque
import graph.graph as graph
from graph.graph_containers import *
import time

def ChooseAttaque(pokemon_actuel_player) :
    """ actionNum = input("Quelle Attaque utiliser ? (1 : {0}, 2 : {1}, 3 : {2}, 4 : {3})  ".format(
        pokemon_actuel_player.Attaques[0].name,
        pokemon_actuel_player.Attaques[1].name,
        pokemon_actuel_player.Attaques[2].name,
        pokemon_actuel_player.Attaques[3].name
    )) """

    text_attaque1 = font.render('{0}'.format(pokemon_actuel_player.Attaques[0].name + " (1)"), False, BLACK)
    text_attaque2 = font.render('{0}'.format(pokemon_actuel_player.Attaques[1].name + " (2)"), False, BLACK)
    text_attaque3 = font.render('{0}'.format(pokemon_actuel_player.Attaques[2].name + " (3)"), False, BLACK)
    text_attaque4 = font.render('{0}'.format(pokemon_actuel_player.Attaques[3].name + " (4)"), False, BLACK)

    actionNum = None
    running   = True
    while running:
        graph.screen.blit(actions, rect_2)
        action1.fill(ColorAttaque(pokemon_actuel_player.Attaques[0].Type))
        graph.screen.blit(action1, rect_3)
        graph.screen.blit(text_attaque1, rect_3)
        action2.fill(ColorAttaque(pokemon_actuel_player.Attaques[1].Type))
        graph.screen.blit(action2, rect_4)
        graph.screen.blit(text_attaque2, rect_4)
        action3.fill(ColorAttaque(pokemon_actuel_player.Attaques[2].Type))
        graph.screen.blit(action3, rect_5)
        graph.screen.blit(text_attaque3, rect_5)
        action4.fill(ColorAttaque(pokemon_actuel_player.Attaques[3].Type))
        graph.screen.blit(action4, rect_6)
        graph.screen.blit(text_attaque4, rect_6)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                actionNum = 1
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                actionNum = 2
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                actionNum = 3
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                actionNum = 4
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                running = False

        pygame.display.flip() 

        

    return actionNum