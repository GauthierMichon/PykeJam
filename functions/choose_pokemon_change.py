import graph.graph as graph
from graph.graph_containers import *
import time

# Fonction permettant de choisir un pokemon
def ChoosePokemon(player, pokemonActualDresseurNum) :

    text_pokemon1 = font.render('{0}'.format(player.pokemons[0].name + " (1)"), False, BLACK)
    text_pokemon2 = font.render('{0}'.format(player.pokemons[1].name + " (2)"), False, BLACK)
    text_pokemon3 = font.render('{0}'.format(player.pokemons[2].name + " (3)"), False, BLACK)
    text_pokemon4 = font.render('{0}'.format(player.pokemons[3].name + " (4)"), False, BLACK)
    text_pokemon5 = font.render('{0}'.format(player.pokemons[4].name + " (5)"), False, BLACK)
    text_pokemon6 = font.render('{0}'.format(player.pokemons[5].name + " (6)"), False, BLACK)
    text_pokemon_PV_player = pokemon_PV_player.render('{0} / {1}'.format(player.pokemons[pokemonActualDresseurNum].PV, player.pokemons[pokemonActualDresseurNum].PVMax), False, BLACK)
    text_pokemon_name_player = pokemon_name_player.render('{0}'.format(player.pokemons[pokemonActualDresseurNum].name), False, BLACK)
    type1_pokemon_player = pygame.image.load("assets/types/{0}.png".format(player.pokemons[pokemonActualDresseurNum].Type))
    type1_pokemon_player = pygame.transform.scale(type1_pokemon_player, (102, 22))
    if player.pokemons[pokemonActualDresseurNum].Type2 != None :
            type2_pokemon_player = pygame.image.load("assets/types/{0}.png".format(player.pokemons[pokemonActualDresseurNum].Type2))
            type2_pokemon_player = pygame.transform.scale(type2_pokemon_player, (102, 22))
        

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
        graph.screen.blit(type1_pokemon_player, (945, 425))
        if player.pokemons[pokemonActualDresseurNum].Type2 != None :
            graph.screen.blit(type2_pokemon_player, (1065, 425))


        graph.screen.blit(actions_pokemon, rect_actions_pokemon)
        if player.pokemons[0].PV <= 0 :
            pokemon1.fill((255, 0, 0))
        elif player.pokemons[0].statut != None :
            pokemon1.fill((239, 213, 34))
        else :
            pokemon1.fill(WHITE)
        graph.screen.blit(pokemon1, rect_pokemon1)
        graph.screen.blit(text_pokemon1, rect_pokemon1)
        if player.pokemons[1].PV <= 0 :
            pokemon2.fill((255, 0, 0))
        elif player.pokemons[1].statut != None :
            pokemon2.fill((239, 213, 34))
        else :
            pokemon2.fill(WHITE)
        graph.screen.blit(pokemon2, rect_pokemon2)
        graph.screen.blit(text_pokemon2, rect_pokemon2)
        if player.pokemons[2].PV <= 0 :
            pokemon3.fill((255, 0, 0))
        elif player.pokemons[2].statut != None :
            pokemon3.fill((239, 213, 34))
        else :
            pokemon3.fill(WHITE)
        graph.screen.blit(pokemon3, rect_pokemon3)
        graph.screen.blit(text_pokemon3, rect_pokemon3)
        if player.pokemons[3].PV <= 0 :
            pokemon4.fill((255, 0, 0))
        elif player.pokemons[3].statut != None :
            pokemon4.fill((239, 213, 34))
        else :
            pokemon4.fill(WHITE)
        graph.screen.blit(pokemon4, rect_pokemon4)
        graph.screen.blit(text_pokemon4, rect_pokemon4)
        if player.pokemons[4].PV <= 0 :
            pokemon5.fill((255, 0, 0))
        elif player.pokemons[4].statut != None :
            pokemon5.fill((239, 213, 34))
        else :
            pokemon5.fill(WHITE)
        graph.screen.blit(pokemon5, rect_pokemon5)
        graph.screen.blit(text_pokemon5, rect_pokemon5)
        if player.pokemons[5].PV <= 0 :
            pokemon6.fill((255, 0, 0))
        elif player.pokemons[5].statut != None :
            pokemon6.fill((239, 213, 34))
        else :
            pokemon6.fill(WHITE)
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