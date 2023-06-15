import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Game-level class to manage assets & behavior"""

    def __init__(self):
        """Initialize game & create resources"""
        pygame.init()
        self.settings = Settings()

        # windowed
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # fullscreen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width
                
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")


    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

    def _check_events(self):      
        # watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            # hide the cursor
            pygame.mouse.set_visible(False)
            # clear any old game stuff
            self.aliens.empty()
            self.bullets.empty()
            # start fresh
            self._create_fleet()
            self.ship.center_ship()


    def _check_keydown_events(self, event):
        # respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  

    def _check_keyup_events(self, event):
        #  respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        self.bullets.update()
        # cleanup offscreen bullets. python expecrts the list to stay at same len, so we use a copy to modify
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """handle collisions"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # destroy active bullets & spawn new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    
    def _fire_bullet(self):
        # creates bullet & adds to the bullet group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        # redraw the screen during each pass w/ the color prop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        # make most recently drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """create a fleet of aliens"""    
        alien = Alien(self)
        # set spacing based on alien size along x axis
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y //( 2 * alien_height)

        # create the full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width +2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        check if the fleet is at an edge
        update all positions within the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit() 

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """logic for aliens hitting an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop the entire fleet & reverse direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _ship_hit(self):
        """respond to ship getting hit by aliens"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # clear the board
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet & reset to center
            self._create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible = True

    def _check_aliens_bottom(self):
        """check if any have made it to the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    # make a game instance & run
    ai = AlienInvasion()
    ai.run_game()