import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """class for the ship behavior"""

    def __init__(self, ai_game):
        """initialize ship & set start pos"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship img & get the rect
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # place new ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float  for ship x position
        self.x = float(self.rect.x)

        # right movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ships position based on movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update the rect obj from self x
        self.rect.x = self.x

    def blitme(self):
        # draw ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center player ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
