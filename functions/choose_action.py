from cProfile import run

from functions.choose_attaque import ChooseAttaque
from functions.choose_item import ChooseItem
from functions.choose_pokemon_change import ChoosePokemon
import graph.graph as graph
from graph.graph_containers import *


# Fonction qui fait choisir au joueur l'action à effectuée
def chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire, dresseurPokemonSwitch, pokemonActualDresseurNum) :
    print("chooseAction")

    # On affiche les actions possibles
    """ action = input("Quelle action faire ? (1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item)  ") """

    bg      = pygame.image.load("assets/bg_combat.png")
    bg      = pygame.transform.scale(bg, (1280, 550))

    text_pokemon_name_player = pokemon_name_player.render('{0}'.format(pokemon_actuel_player.name), False, BLACK)
    text_pokemon_PV_player = pokemon_PV_player.render('{0} / {1}'.format(pokemon_actuel_player.PV, pokemon_actuel_player.PVMax), False, BLACK)
    print(pokemon_actuel_player.name, pokemon_actuel_player.spriteDos)
    pokemon_player = pygame.image.load("assets/sprite_dos/{}".format(pokemon_actuel_player.spriteDos))
    pokemon_player = pygame.transform.scale(pokemon_player, (300, 300))



    running   = True
    while running:
        graph.screen.fill((0,0,0))
        graph.screen.blit(bg, (0, 0))
        graph.screen.blit(pokemon_player, (150, 282))
        graph.screen.blit(pokemon_adversaire, (850, 140 ))
        graph.screen.blit(infos_combat, rect_1)

        graph.screen.blit(actions, rect_2)
        graph.screen.blit(action1, rect_3)
        graph.screen.blit(text_action1, rect_3)
        graph.screen.blit(action2, rect_4)
        graph.screen.blit(text_action2, rect_4)
        graph.screen.blit(action3, rect_5)
        graph.screen.blit(text_action3, rect_5)
        graph.screen.blit(action4, rect_6)

        graph.screen.blit(info_pokemon_adversaire, rect_7)
        graph.screen.blit(text_pokemon_name_adversaire, rect_pokemon_adversaire_name)
        graph.screen.blit(text_pokemon_PV_adversaire, rect_pokemon_adversaire_PV)
        graph.screen.blit(info_pokemon_player,rect_8)
        graph.screen.blit(text_pokemon_name_player, rect_pokemon_player_name)
        graph.screen.blit(text_pokemon_PV_player, rect_pokemon_player_PV)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                action = 1
                actionNum = ChooseAttaque(pokemon_actuel_player)
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                action = 2
                actionNum = ChoosePokemon(player, pokemonActualDresseurNum)
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                action = 3
                actionNum = ChooseItem(player)
                running = False

        

        pygame.display.flip() 


        

    return int(action), int(actionNum)

        