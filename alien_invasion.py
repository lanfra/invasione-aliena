import sys
import pygame
from settings import Settings #Importo file setting
from ship import Ship #Modulo astronave.

class AlienInvasion:
    """Classe principale del gioco ALIEN INVASION"""

    def __init__(self):
        """Risorse del gioco."""
        pygame.init()
        self.clock = pygame.time.Clock()

        #Setting della finestra.
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_width))

        pygame.display.set_caption("Invasione Aliena")
        self.ship = Ship(self) #Richiamo l'astronave.

    def run_game(self):
        """Main Avvio gioco."""
        while True: #Ciclo continuo sempre attivo.
            for event in pygame.event.get(): #Ogni evento succede sulla finestra.
                #Uscita se premuto q.
                if event.type == pygame.quit:
                    sys.exit()

                #Colora schermata di sfondo, la ridimensiona e aggiunge elementi.
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                
                #Mostra finestra.
                pygame.display.flip()

                #Frequenza di aggiornamento schermata.
                self.clock.tick(60) #Frequenza di aggiornamento di volte 60 al secondo.

#Avvio gioco.
if __name__ == "__main__":
    ai = AlienInvasion() 
    ai.run_game()

