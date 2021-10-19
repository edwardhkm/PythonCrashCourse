import sys

import pygame

class Rocket:
    def __init__(self, r_game):
        self.screen = r_game.screen
        self.screen_rect = r_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Set position of the ship
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.center = self.screen_rect.center

        # Set moving flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

class Rocket_game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket moving")
        self.bg_color = (230, 230, 230)
        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_event()
            self.rocket.update()
            self._update_screen()

    def _check_event(self):
        """Check events keypress"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        ###Make the most recently drawn screen visible.###
        pygame.display.flip()


if __name__ == "__main__":
    rg = Rocket_game()
    rg.run_game()