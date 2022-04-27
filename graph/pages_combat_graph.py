from cmath import rect
import pygame

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen  = pygame.display.set_mode((1280, 720))
clock   = pygame.time.Clock()
FPS     = 60
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE    = (89, 119, 178)
ORANGE  = (234, 151, 40)

bg  = pygame.image.load("bg_combat.png")
bg  = pygame.transform.scale(bg, (1280, 550))

pokemon_1 = pygame.image.load("sprite_dos/Tortank.png")
pokemon_1 = pygame.transform.scale(pokemon_1, (300, 300))
pokemon_2 = pygame.image.load("sprite/Mackogneur.gif")
pokemon_2 = pygame.transform.scale(pokemon_2, (200, 200))

rect_1  = pygame.Rect((10, 560), (1260, 150), )
instruction = pygame.Surface((1260, 150))
instruction.fill(BLUE)

pygame.draw.rect(instruction, WHITE, pygame.Rect(0, 0, 1260, 150),  10, 3)

rect_2 = pygame.Rect((630, 570), (630, 150))
actions = pygame.Surface((630, 130))
actions.fill(BLUE)

pygame.draw.rect(actions, ORANGE, pygame.Rect(0, 0, 630, 130),  10, 3)

rect_3      = pygame.Rect((645, 585), (295, 45))
attaque     = pygame.Surface((295, 45))
attaque.fill('WHITE')

rect_4      = pygame.Rect((645, 640), (295, 45))
pokemon     = pygame.Surface((295, 45))
pokemon.fill('WHITE')

rect_5      = pygame.Rect((950, 585), (295, 45))
sac         = pygame.Surface((295, 45))
sac.fill('WHITE')

rect_6      = pygame.Rect((950, 640), (295, 45))
fuite       = pygame.Surface((295, 45))
fuite.fill('WHITE')

rect_7  = pygame.Rect((175, 40), (450, 125), )
stat    = pygame.Surface((450, 125))
stat.fill(WHITE)

pygame.draw.rect(stat, BLACK, pygame.Rect(0, 0, 450, 125),  10, 3)

rect_8      = pygame.Rect((750, 400), (450, 125), )
my_stat     = pygame.Surface((450, 125))
my_stat.fill(WHITE)

pygame.draw.rect(my_stat, BLACK, pygame.Rect(0, 0, 450, 125),  10, 3)

pygame.mouse.set_visible(1)
pygame.display.set_caption('PykeJam')

running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.blit(bg,(0,0))
    screen.blit(pokemon_1, (150, 282))
    screen.blit(pokemon_2, (850, 140 ))
    screen.blit(instruction, rect_1)
    screen.blit(actions, rect_2)
    screen.blit(attaque, rect_3)
    screen.blit(pokemon, rect_4)
    screen.blit(sac, rect_5)
    screen.blit(fuite, rect_6)
    screen.blit(stat, rect_7)
    screen.blit(my_stat,rect_8)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 

print("Exited the game loop. Game will quit...")
quit() 
