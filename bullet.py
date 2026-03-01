import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Gestione proiettili."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Proiettile.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y) #Momorizza la posizione dello sparo.

    def update(self):
        """Il proiettile si muove verso su."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Disegno del proiettile."""
        pygame.draw.rect(self.screen, self.color, self.rect)

