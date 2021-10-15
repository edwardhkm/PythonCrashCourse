import pygame

class Rocket_game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Rocket moving")
        self.bg_color = (230, 230, 230)
        self.rocket = Rocket()

    def run_game(self):

    def _check_event(self):

    def _check_keyup_events(self):

    def _check_keydown_events(self):

class Rocket:
    def __init__(self, r_game):
        self.rocket_game = r_game.screen
        self.screen_rect = r_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.image = pygame.image.load('images/ship.bmp')



if __name__ == "__main__":
    rg = Rocket_game()
    rg.run_game()