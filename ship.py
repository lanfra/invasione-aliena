import pygame

class Ship:
    def __init__(self, ai_game):
        """Astronava e settings iniziale."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Astronava.
        self.image  = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Disegna l'astronave in basso allo schermo."""
        self.screen.blit(self.image, self.rect)