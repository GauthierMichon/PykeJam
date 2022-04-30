import graph.graph as graph
from graph.graph_containers import *

# Fonction qui vérifie si le combat continue ou non
def CombatContinue(player, adversaire) :
    # Si tous les pokemons du joueur sont KO, le combat est terminé
    if player.pokemons[0].PV <= 0 and player.pokemons[1].PV <= 0 and player.pokemons[2].PV <= 0 and player.pokemons[3].PV <= 0 and player.pokemons[4].PV <= 0 and player.pokemons[5].PV <= 0 :
        print("Vous avez perdu")
        running = True
        while running :
            graph.screen.blit(bg_accueil, (0, 0))
            graph.screen.blit(lose, pygame.rect.Rect(400, 40, 128, 128))
            graph.screen.blit(jamLose, (300, 300))
            graph.screen.blit(goatLose, (800, 300))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            pygame.display.flip()


        return False
    # Si tous les pokemons de l'adversaire sont KO, le combat est terminé
    elif adversaire.pokemons[0].PV <= 0 and adversaire.pokemons[1].PV <= 0 and adversaire.pokemons[2].PV <= 0 and adversaire.pokemons[3].PV <= 0 and adversaire.pokemons[4].PV <= 0 and adversaire.pokemons[5].PV <= 0 :
        print("Vous avez gagné")
        running = True
        while running :
            graph.screen.blit(bg_accueil, (0, 0))
            graph.screen.blit(win, pygame.rect.Rect(400, 40, 128, 128))
            graph.screen.blit(jamWin, (300, 300))
            graph.screen.blit(goatWin, (800, 300))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            pygame.display.flip()


        return False
    # Sinon, le combat continue
    else :
        return True