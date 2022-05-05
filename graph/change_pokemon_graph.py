import time
import graph.graph as graph
from graph.graph_containers import *
from graph.reload_graph_pokemons import ReloadGraphPokemons

def ChangePokemonGraph(pokemon_actuel_player, pokemon_actuel_adversaire) :    
    bg      = pygame.image.load("assets/bg_combat.png")
    bg      = pygame.transform.scale(bg, (1280, 550))

    graph.screen.fill((0,0,0))
    graph.screen.blit(bg, (0, 0))

    ReloadGraphPokemons(pokemon_actuel_player, pokemon_actuel_adversaire)
        
        
    graph.screen.blit(infos_combat, rect_1)
    

    pygame.display.flip()