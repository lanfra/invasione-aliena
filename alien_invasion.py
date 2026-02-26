import sys
import pygame

class AlienInvasion:
    """Classe principale del gioco ALIEN INVASION"""

    def __init__(self):
        """Risorse del gioco."""
        pygame.init()
        self.clock = pygame.time.Clock()

        #Finestra setting.
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Invasione Aliena")

        #Colore di sfondo.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Main Avvio gioco."""
        while True: #Ciclo continuo sempre attivo.
            for event in pygame.event.get(): #Ogni evento succede sulla finestra.
                #Uscita se premuto q.
                if event.type == pygame.quit:
                    sys.exit()

                #Colora schermata di sfondo.
                self.screen.fill(self.bg_color)
                #Mostra finestra.
                pygame.display.flip()
                #Frequenza di aggiornamento schermata.
                self.clock.tick(60) #Frequenza di aggiornamento di volte 60 al secondo.

#Avvio gioco.
if __name__ == "__main__":
    ai = AlienInvasion() 
    ai.run_game()

