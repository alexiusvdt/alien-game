class GameStats:
    """scoring is fun!"""

    def __init__(self, ai_game):
        """initialize"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """initialize resettable stats"""
        self.ships_left = self.settings.ship_limit