import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a single alien creator"""
    def __init__(self, ai_game):
        """initialize & set starting pos"""
        super().__init__()
        self.screen = ai_game.screen

        # load the image and set the rect
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self. image.get_rect()

        # place @ top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the horizontal pos
        self.x = float(self.rect.x)