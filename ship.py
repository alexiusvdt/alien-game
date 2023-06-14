import pygame

class Ship:
    """class for the ship behavior"""

    def __init__(self, ai_game):
        """initialize ship & set start pos"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship img & get the rect
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # place new ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # right movement flag
        self.moving_right = False

    def update(self):
        # update the ships position based on movement flag status
        if self.moving_right:
            self.rect.x += 1


    def blitme(self):
        # draw ship at its current location
        self.screen.blit(self.image, self.rect)

