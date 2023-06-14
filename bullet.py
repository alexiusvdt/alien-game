import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """managing bullets fired from ship"""
    def __init__(self, ai_game):
        # create a bullet at ship rect
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.bullets_allowed = 4

        # create bullet rect and set pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store pos as a float
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw it to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)