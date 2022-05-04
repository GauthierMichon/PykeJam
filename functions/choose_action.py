from cProfile import run

from functions.choose_attaque import ChooseAttaque
from functions.choose_item import ChooseItem
from functions.choose_pokemon_change import ChoosePokemon
import graph.graph as graph
from graph.graph_containers import *
from graph.reload_graph_pokemons import ReloadGraphPokemons


# Fonction qui fait choisir au joueur l'action à effectuée
def chooseAction(player, adversaire, pokemon_actuel_player, pokemon_actuel_adversaire, dresseurPokemonSwitch, pokemonActualDresseurNum) :
    print("chooseAction")

    # On affiche les actions possibles
    """ action = input("Quelle action faire ? (1 : Lancer une Attaque, 2 : Changer de pokemon, 3 : Utiliser un item)  ") """

    bg      = pygame.image.load("assets/bg_combat.png")
    bg      = pygame.transform.scale(bg, (1280, 550))

    graph.screen.fill((0,0,0))
    graph.screen.blit(bg, (0, 0))
    
    ReloadGraphPokemons(pokemon_actuel_player, pokemon_actuel_adversaire)


    actionNum = None
    running   = True
    while running:
        
        
        graph.screen.blit(infos_combat, rect_1)
        graph.screen.blit(actions, rect_2)
        graph.screen.blit(action1, rect_3)
        graph.screen.blit(text_action1, rect_3)
        graph.screen.blit(action2, rect_4)
        graph.screen.blit(text_action2, rect_4)
        graph.screen.blit(action3, rect_5)
        graph.screen.blit(text_action3, rect_5)
        graph.screen.blit(action4, rect_6)

        

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                action = 1
                actionNum = ChooseAttaque(pokemon_actuel_player)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                action = 2
                actionNum = ChoosePokemon(player, pokemonActualDresseurNum)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                action = 3
                actionNum = ChooseItem(player)

        if actionNum != None :
            running = False

        pygame.display.flip() 


        

    return int(action), int(actionNum)

        