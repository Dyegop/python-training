import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        """ Manage the game functions and attributes

            Attributes:
                -settings: instance of Setting class
                -screen: game screen
                -screen_rect: game screen rectangle
                -ship: instance of Ship class, passing the game itself as a parameter
                -key_flag: True: pressed, False released

            Functions:
                -run_game: execute main game functions
                -_check_events: check input pygame events (from keyboard/mouse)
                -_update_screen: update element position, color, etc. displayed on screen

        """
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.key_flag = False

    def run_game(self):
        while True:
            self._check_events()
            self.ship.move_ship()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.key_flag = True
                self._key_events(event)
            elif event.type == pygame.KEYUP:
                self.key_flag = False
                self._key_events(event)

    def _key_events(self, event):
        if self.key_flag:
            if event.key == pygame.K_a:
                self.ship.move_left = True
            elif event.key == pygame.K_d:
                self.ship.move_right = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        if not self.key_flag:
            self.ship.move_left = False
            self.ship.move_right = False

    def _update_screen(self):
        # Fill background
        self.screen.fill(self.settings.bg_color)
        # Draw ship
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()





if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    # Make a game instance, and run the game.
    ai = AlienInvasion()

    ai.run_game()
