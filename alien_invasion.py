import sys
import pygame

class AlienInvasion:
    """Game-level class to manage assets & behavior"""

    def __init__(self):
        """Initialize game & create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """start game loop"""
        while True:
            # watch for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                

                # make most recently drawn screen visible
                pygame.display.flip()

if __name__ == '__main__':
    # make a game instance & run
    ai = AlienInvasion()
    ai.run_game()