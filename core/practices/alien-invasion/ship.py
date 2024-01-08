import pygame


class Ship:
    """ Class for ship elements

        Attributes:
            -ai_game: instance of AlienInvasion class
            -image: ship image
            -rect: get a rectangle from ship image
            -rect.midbottom: ship starting position
            -move_right: right movement flag
            -move_left: left movement flag
            -x: decimal value of x position for rect


        Methods:
            -blitme: draw the ship at its current location
            -update: update position based on the movement flag
    """
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.image = pygame.image.load('resources/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.x = float(self.rect.x)

    def blitme(self):
        self.ai_game.screen.blit(self.image, self.rect)

    def move_ship(self):
        if self.move_right and self.rect.right < self.ai_game.screen_rect.right:
            self.x += self.ai_game.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.ai_game.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x
