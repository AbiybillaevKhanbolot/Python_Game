import pygame
import background as bg
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Image/Fish/Akula.png'), (125,60))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = bg.WIDHT
        self.rect.y = randint(178, 628)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def draw(self,window):
        window.blit(self.image, self.rect)


