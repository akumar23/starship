from cProfile import run
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Starship")
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        ship.blitme()
        pygame.display.flip()
    
run_game()