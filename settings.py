class Settings:
    """settings for the game"""

    def __init__(self):
        """initialize static and dynamic settings"""
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 4
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # game scaling modifier
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init dynamic settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.25
        self.alien_speed = 1.0

        self.alien_points = 50

        # 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed and alien point values per modifiers"""
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)