import pygame

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen  = pygame.display.set_mode((1280, 720))
clock   = pygame.time.Clock()
FPS     = 60
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)

bg  = pygame.image.load("bg_combat.png")
bg  = pygame.transform.scale(bg, (1280, 550))


pygame.display.set_caption('Show Text')
font    = pygame.font.Font('freesansbold.ttf', 32)
title   = font.render('', True, WHITE, BLACK)

rect    = pygame.Rect((0, 550), (310, 170))
txt     = pygame.Surface((310, 170))
txt.fill(WHITE)

rect_object = pygame.Rect((320, 550), (310, 170))
obj         = pygame.Surface((310, 170))
obj.fill(WHITE)

rect_2  = pygame.Rect((650, 550), (310, 80))
attaque_1 = pygame.Surface((310, 80))
attaque_1.fill(WHITE)

rect_3  = pygame.Rect((650, 640), (310,80))
attaque_2 = pygame.Surface((310, 80))
attaque_2.fill(WHITE)

rect_4 = pygame.Rect(( 970, 550),(310, 80))
attaque_3 = pygame.Surface((310, 80))
attaque_3.fill(WHITE)

rect_5 = pygame.Rect(( 970, 640),(310, 80))
attaque_4 = pygame.Surface((310, 80))
attaque_4.fill(WHITE)

pygame.mouse.set_visible(1)
pygame.display.set_caption('PykeJam')

running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.blit(bg,(0,0))
    screen.blit(txt, rect)
    screen.blit(obj, rect_object)
    screen.blit(attaque_1, rect_2)
    screen.blit(attaque_2, rect_3)
    screen.blit(attaque_3, rect_4)
    screen.blit(attaque_4, rect_5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 

print("Exited the game loop. Game will quit...")
quit() 
