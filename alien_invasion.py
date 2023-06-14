import sys
import pygame

from settings import Settings

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


    def run_game(self):
        """start game loop"""
        while True:
            # watch for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # redraw the screen during each pass w/ the color prop
                self.screen.fill(self.settings.bg_color)

                # make most recently drawn screen visible
                pygame.display.flip()

if __name__ == '__main__':
    # make a game instance & run
    ai = AlienInvasion()
    ai.run_game()