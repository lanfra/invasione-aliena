import sys
import pygame

class AlienInvasion:
    """Classe principale del gioco ALIEN INVASION"""

    def __init__(self):
        """Risorse del gioco."""
        pygame.init()

        #Finestra setting.
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Invasione Aliena")

    def run_game(self):
        """Main Avvio gioco."""
        while True: #Ciclo continuo sempre attivo.
            for event in pygame.event.get(): #Ogni evento succede sulla finestra.
                #Uscita se premuto q.
                if event.type == pygame.quit:
                    sys.exit()

                #Mostra finestra.
                pygame.display.flip()

#Avvio gioco.
if __name__ == "__main__":
    ai = AlienInvasion() 
    ai.run_game()

