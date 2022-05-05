import time
import graph.graph as graph
from graph.graph_containers import *

def WriteInfo(info) :
    infos_render = pygame.font.SysFont('arial', 45).render(info, False, WHITE)
    graph.screen.blit(infos_combat, rect_1)
    graph.screen.blit(infos_render, rect_infos)

    pygame.display.flip()
    

    time.sleep(2)

