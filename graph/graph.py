import pygame
from functions.game import game
from graph.graph_containers import *


successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen  = pygame.display.set_mode((1280, 720))
clock   = pygame.time.Clock()
FPS     = 60
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)

bg          = bg_accueil

pygame.display.set_caption('Show Text')
font    = pygame.font.Font('freesansbold.ttf', 32)
title   = font.render('', True, WHITE, BLACK)

pygame.mouse.set_visible(1)

pygame.display.set_caption('PykeJam')

running = True
start   = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.blit(bg,(0,0))
    screen.blit(title, (400, 100))
    if start == True: 
        screen.blit(logo, pygame.rect.Rect(490, 210, 128, 128))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start       = False
            """ bg          = pygame.image.load("assets/background_2.png")
            bg          = pygame.transform.scale(bg, (1280, 800))
            title       = font.render('Choose your first pokémon ', True, WHITE) """

            game()

            


    pygame.display.flip() 

print("Exited the game loop. Game will quit...")
quit() 