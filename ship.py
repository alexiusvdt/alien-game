import pygame

class Ship:
    """class for the ship behavior"""

    def __init__(self, ai_game):
        """initialize ship & set start pos"""
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
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update the rect obj from self x
        self.rect.x = self.x


    def blitme(self):
        # draw ship at its current location
        self.screen.blit(self.image, self.rect)

