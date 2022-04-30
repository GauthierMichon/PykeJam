import pygame

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE    = (89, 119, 178)
ORANGE  = (234, 151, 40)
GREY   = (128, 128, 128)

pygame.font.init()

# Page d'accueil
bg_accueil = pygame.image.load("assets/background.png")

logo        = pygame.image.load("assets/logo.png")
logo        = pygame.transform.scale(logo, (300, 300))

# Page de combat
bg  = pygame.image.load("assets/bg_combat.png")
bg  = pygame.transform.scale(bg, (1280, 550))

# Sprites
pokemon_player = pygame.image.load("assets/sprite_dos/Tortank.png")
pokemon_player = pygame.transform.scale(pokemon_player, (300, 300))
pokemon_adversaire = pygame.image.load("assets/sprite/Mackogneur.gif")
pokemon_adversaire = pygame.transform.scale(pokemon_adversaire, (200, 200))

# Infos combat
rect_1  = pygame.Rect((10, 560), (1260, 150), )
infos_combat = pygame.Surface((1260, 150))
infos_combat.fill(BLUE)

pygame.draw.rect(infos_combat, WHITE, pygame.Rect(0, 0, 1260, 150),  10, 3)

# Actions
rect_2 = pygame.Rect((630, 570), (630, 150))
actions = pygame.Surface((630, 130))
actions.fill(BLUE)

pygame.draw.rect(actions, ORANGE, pygame.Rect(0, 0, 630, 130),  10, 3)
font = pygame.font.SysFont('arial', 35)

# Action 1
rect_3      = pygame.Rect((645, 585), (295, 45))
action1     = pygame.Surface((295, 45))
action1.fill('WHITE')

text_action1 = font.render('Attaque', False, BLACK)

# Action 2
rect_4      = pygame.Rect((645, 640), (295, 45))
action2     = pygame.Surface((295, 45))
action2.fill('WHITE')

text_action2 = font.render('Pokémons', False, BLACK)

# Action 3
rect_5      = pygame.Rect((950, 585), (295, 45))
action3     = pygame.Surface((295, 45))
action3.fill('WHITE')

text_action3 = font.render('Objets', False, BLACK)

# Action 4
rect_6      = pygame.Rect((950, 640), (295, 45))
action4     = pygame.Surface((295, 45))
action4.fill('WHITE')

# Infos pokemon adversaire
rect_7  = pygame.Rect((175, 40), (450, 125), )
info_pokemon_adversaire    = pygame.Surface((450, 125))
info_pokemon_adversaire.fill(WHITE)

rect_pokemon_adversaire_name = pygame.Rect((190, 55), (450, 45), )
pokemon_name_adversaire = pygame.font.SysFont('arial', 25)
text_pokemon_name_adversaire = pokemon_name_adversaire.render('Makogneur', False, BLACK)

statut_pokemon_adversaire = pygame.image.load("assets/statuts/Gel.png")
statut_pokemon_adversaire = pygame.transform.scale(statut_pokemon_adversaire, (80, 40))

rect_pokemon_adversaire_PV = pygame.Rect((450, 110), (450, 45), )
pokemon_PV_adversaire = pygame.font.SysFont('arial', 25)
text_pokemon_PV_adversaire = pokemon_PV_adversaire.render('179 / 179', False, BLACK)

pygame.draw.rect(info_pokemon_adversaire, BLACK, pygame.Rect(0, 0, 450, 125),  10, 3)

# Infos pokemon joueur
rect_8      = pygame.Rect((750, 400), (450, 125), )
info_pokemon_player     = pygame.Surface((450, 125))
info_pokemon_player.fill(WHITE)

pokemon_name_player = pygame.font.SysFont('arial', 25)
text_pokemon_name_player = pokemon_name_player.render('Tortank', False, BLACK)

rect_pokemon_player_name = pygame.Rect((765, 415), (450, 45), )
pokemon_name_player = pygame.font.SysFont('arial', 25)
text_pokemon_name_player = pokemon_name_player.render('Tortank', False, BLACK)

statut_pokemon_player = pygame.image.load("assets/statuts/Gel.png")
statut_pokemon_player = pygame.transform.scale(statut_pokemon_player, (80, 40))

rect_pokemon_player_PV = pygame.Rect((1025, 470), (450, 45), )
pokemon_PV_player = pygame.font.SysFont('arial', 25)
text_pokemon_PV_player = pokemon_PV_player.render('179 / 179', False, BLACK)

pygame.draw.rect(info_pokemon_player, BLACK, pygame.Rect(0, 0, 450, 125),  10, 3)


########################################################################################################################
# Action Attaque
text_attaque1 = font.render('Attaque 1', False, BLACK)
text_attaque2 = font.render('Attaque 2', False, BLACK)
text_attaque3 = font.render('Attaque 3', False, BLACK)
text_attaque4 = font.render('Attaque 4', False, BLACK)


########################################################################################################################
# Action Objet
text_objet1 = font.render('Objet 1', False, BLACK)
text_objet2 = font.render('Objet 2', False, BLACK)
text_objet3 = font.render('Objet 3', False, BLACK)



########################################################################################################################
# Actions pokemon
rect_actions_pokemon = pygame.Rect((20, 570), (1260, 150))
actions_pokemon = pygame.Surface((1240, 130))
actions_pokemon.fill(BLUE)

pygame.draw.rect(actions_pokemon, ORANGE, pygame.Rect(0, 0, 1240, 130),  10, 3)

rect_pokemon1       = pygame.Rect((35, 585), (390, 45))
pokemon1            = pygame.Surface((390, 45))
pokemon1.fill('WHITE')
text_pokemon1 = font.render('pokemon 1', False, BLACK)

rect_pokemon2       = pygame.Rect((445, 585), (390, 45))
pokemon2            = pygame.Surface((390, 45))
pokemon2.fill('WHITE')
text_pokemon2 = font.render('pokemon 2', False, BLACK)

rect_pokemon3       = pygame.Rect((855, 585), (390, 45))
pokemon3            = pygame.Surface((390, 45))
pokemon3.fill('WHITE')
text_pokemon3 = font.render('pokemon 3', False, BLACK)

rect_pokemon4       = pygame.Rect((35, 640), (390, 45))
pokemon4            = pygame.Surface((390, 45))
pokemon4.fill('WHITE')
text_pokemon4 = font.render('pokemon 4', False, BLACK)

rect_pokemon5       = pygame.Rect((445, 640), (390, 45))
pokemon5            = pygame.Surface((390, 45))
pokemon5.fill('WHITE')
text_pokemon5 = font.render('pokemon 5', False, BLACK)

rect_pokemon6       = pygame.Rect((855, 640), (390, 45))
pokemon6            = pygame.Surface((390, 45))
pokemon6.fill('WHITE')
text_pokemon6 = font.render('pokemon 6', False, BLACK)
