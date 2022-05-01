import graph.graph as graph
from graph.graph_containers import *

def ChooseItem(player) :
    """ for i in range(len(player.inventaire)) :
        print(str(i + 1) + " : " + player.inventaire[i].name)
    actionNum = input("Quelle Objet utiliser ? ") """

    text_objet1 = None
    text_objet2 = None
    text_objet3 = None

    for i in range(len(player.inventaire)) :
        if i == 0 :
            text_objet1 = font.render('{0}'.format(player.inventaire[0].name), False, BLACK)
        elif i == 1 :
            text_objet2 = font.render('{0}'.format(player.inventaire[1].name), False, BLACK)
        elif i == 2 :
            text_objet3 = font.render('{0}'.format(player.inventaire[2].name), False, BLACK)


    actionNum = None
    running   = True
    while running:
        graph.screen.blit(actions, rect_2)
        graph.screen.blit(action1, rect_3)
        if text_objet1 != None :
            graph.screen.blit(text_objet1, rect_3)
        graph.screen.blit(action2, rect_4)
        if text_objet2!= None :
            graph.screen.blit(text_objet2, rect_4)
        graph.screen.blit(action3, rect_5)
        if text_objet3!= None :
            graph.screen.blit(text_objet3, rect_5)
        graph.screen.blit(action4, rect_6)

        for event in pygame.event.get():
            if text_objet1 != None :
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    actionNum = 1
                    running = False

            if text_objet2!= None :
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    actionNum = 2
                    running = False

            if text_objet3!= None :
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    actionNum = 3
                    running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                running = False

        pygame.display.flip() 

    return actionNum