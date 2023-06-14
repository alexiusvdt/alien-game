import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Game-level class to manage assets & behavior"""

    def __init__(self):
        """Initialize game & create resources"""
        pygame.init()
        self.settings = Settings()

        # display size set up, this can be changed later but hardcoded for now
        # in pygame, every element is its own surface
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):      
        # watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            
    def _update_screen(self):
        # redraw the screen during each pass w/ the color prop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance & run
    ai = AlienInvasion()
    ai.run_game()