import graph.graph as graph
from graph.graph_containers import *
import time

def ReloadGraphPokemons(pokemon_actuel_player, pokemon_actuel_adversaire) :
    text_pokemon_name_player = pokemon_name_player.render('{0}'.format(pokemon_actuel_player.name), False, BLACK)
    text_pokemon_PV_player = pokemon_PV_player.render('{0} / {1}'.format(pokemon_actuel_player.PV, pokemon_actuel_player.PVMax), False, BLACK)
    if pokemon_actuel_player.statut != None :
        statut_pokemon_player = pygame.image.load("assets/statuts/{0}.png".format(pokemon_actuel_player.statut))
        statut_pokemon_player = pygame.transform.scale(statut_pokemon_player, (80, 40))
    pokemon_player = pygame.image.load("assets/sprite_dos/{}".format(pokemon_actuel_player.spriteDos))
    pokemon_player = pygame.transform.scale(pokemon_player, (300, 300))

    text_pokemon_name_adversaire = pokemon_name_adversaire.render('{0}'.format(pokemon_actuel_adversaire.name), False, BLACK)
    text_pokemon_PV_adversaire = pokemon_PV_adversaire.render('{0} / {1}'.format(pokemon_actuel_adversaire.PV, pokemon_actuel_adversaire.PVMax), False, BLACK)
    if pokemon_actuel_adversaire.statut != None :
        statut_pokemon_adversaire = pygame.image.load("assets/statuts/{0}.png".format(pokemon_actuel_adversaire.statut))
        statut_pokemon_adversaire = pygame.transform.scale(statut_pokemon_adversaire, (80, 40))
    pokemon_adversaire = pygame.image.load("assets/sprite/{}".format(pokemon_actuel_adversaire.sprite))
    pokemon_adversaire = pygame.transform.scale(pokemon_adversaire, (300, 300))

    graph.screen.blit(pokemon_player, (150, 282))
    graph.screen.blit(pokemon_adversaire, (850, 140 ))
    graph.screen.blit(infos_combat, rect_1)
    
    graph.screen.blit(info_pokemon_adversaire, rect_7)
    graph.screen.blit(text_pokemon_name_adversaire, rect_pokemon_adversaire_name)
    graph.screen.blit(text_pokemon_PV_adversaire, rect_pokemon_adversaire_PV)
    if pokemon_actuel_adversaire.statut != None :
        graph.screen.blit(statut_pokemon_adversaire, (200, 90))

    graph.screen.blit(info_pokemon_player,rect_8)
    graph.screen.blit(text_pokemon_name_player, rect_pokemon_player_name)
    graph.screen.blit(text_pokemon_PV_player, rect_pokemon_player_PV)
    if pokemon_actuel_player.statut!= None :
        graph.screen.blit(statut_pokemon_player, (775, 450))

    pygame.display.flip() 

    