import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a single alien creator"""
    def __init__(self, ai_game):
        """initialize & set starting pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the image and set the rect
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self. image.get_rect()

        # place @ top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the horizontal pos
        self.x = float(self.rect.x)

    def update(self):
        """move the alien to the right/left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """return true if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True