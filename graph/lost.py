import pygame

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen  = pygame.display.set_mode((1280, 720))
clock   = pygame.time.Clock()
FPS     = 60
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)

bg          = pygame.image.load("background.png")
logo        = pygame.image.load("wasted.png").convert_alpha()
logo        = pygame.transform.scale(logo, (500, 150))

jam         = pygame.image.load("bat_jam.png")
jam         = pygame.transform.scale(jam, (180, 300))

goat        = pygame.image.load("got_rat.png")
goat        = pygame.transform.scale(goat, (180, 300))

pygame.mouse.set_visible(1)

pygame.display.set_caption('PykeJam')

running = True
while running:
    dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    screen.blit(bg,(0,0))
    screen.blit(logo, pygame.rect.Rect(400, 40, 128, 128))
    screen.blit(jam, (300, 300))
    screen.blit(goat, (800, 300))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 

print("Exited the game loop. Game will quit...")
quit() 