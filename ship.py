from turtle import screensize
import pygame

class Ship():
    def __init__(self, settings, screen) -> None:
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False
        self.moving_left = False 
        self.center = float(self.rect.centerx)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.ship_speed
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)