from cmath import rect
import pygame
from graph_containers import *


successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen  = pygame.display.set_mode((1280, 720))
clock   = pygame.time.Clock()
FPS     = 60
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE    = (89, 119, 178)
ORANGE  = (234, 151, 40)
GREY   = (128, 128, 128)

bg  = pygame.image.load("assets/bg_combat.png")
bg  = pygame.transform.scale(bg, (1280, 550))



pygame.mouse.set_visible(1)
pygame.display.set_caption('PykeJam')

running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.blit(bg,(0,0))
    screen.blit(pokemon_player, (150, 282))
    screen.blit(pokemon_adversaire, (850, 140 ))
    screen.blit(infos_combat, rect_1)

    # Choose action
    """ screen.blit(actions, rect_2)
    screen.blit(action1, rect_3)
    screen.blit(text_action1, rect_3)
    screen.blit(action2, rect_4)
    screen.blit(text_action2, rect_4)
    screen.blit(action3, rect_5)
    screen.blit(text_action3, rect_5)
    screen.blit(action4, rect_6) """


    # Action Attaque
    """ screen.blit(actions, rect_2)
    screen.blit(action1, rect_3)
    screen.blit(text_attaque1, rect_3)
    screen.blit(action2, rect_4)
    screen.blit(text_attaque2, rect_4)
    screen.blit(action3, rect_5)
    screen.blit(text_attaque3, rect_5)
    screen.blit(action4, rect_6)
    screen.blit(text_attaque4, rect_6) """


    # Action Objet
    screen.blit(actions, rect_2)
    screen.blit(action1, rect_3)
    screen.blit(text_objet1, rect_3)
    screen.blit(action2, rect_4)
    screen.blit(text_objet2, rect_4)
    screen.blit(action3, rect_5)
    screen.blit(text_objet3, rect_5)
    screen.blit(action4, rect_6)



    # Action pokemon
    """
    screen.blit(actions_pokemon, rect_actions_pokemon)
    screen.blit(pokemon1, rect_pokemon1)
    screen.blit(text_pokemon1, rect_pokemon1)
    screen.blit(pokemon2, rect_pokemon2)
    screen.blit(text_pokemon2, rect_pokemon2)
    screen.blit(pokemon3, rect_pokemon3)
    screen.blit(text_pokemon3, rect_pokemon3)
    screen.blit(pokemon4, rect_pokemon4)
    screen.blit(text_pokemon4, rect_pokemon4)
    screen.blit(pokemon5, rect_pokemon5)
    screen.blit(text_pokemon5, rect_pokemon5)
    screen.blit(pokemon6, rect_pokemon6)
    screen.blit(text_pokemon6, rect_pokemon6) """
    

    screen.blit(info_pokemon_adversaire, rect_7)
    screen.blit(text_pokemon_name_adversaire, rect_pokemon_adversaire_name)
    screen.blit(text_pokemon_PV_adversaire, rect_pokemon_adversaire_PV)
    screen.blit(info_pokemon_player,rect_8)
    screen.blit(text_pokemon_name_player, rect_pokemon_player_name)
    screen.blit(text_pokemon_PV_player, rect_pokemon_player_PV)

    screen.blit(statut_pokemon_adversaire, (200, 90))
    screen.blit(statut_pokemon_player, (775, 450))

    screen.blit(type1_pokemon_player, (945, 425))
    screen.blit(type2_pokemon_player, (1065, 425))

    screen.blit(type1_pokemon_player, (370, 70))
    screen.blit(type2_pokemon_player, (490, 70))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 

print("Exited the game loop. Game will quit...")
quit() 
