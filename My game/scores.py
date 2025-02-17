import pygame
from hero import Hero


class Scores():
    def __init__(self, window):
        self.image_hp = pygame.transform.scale(pygame.image.load('Image/stats/Heard.png').convert_alpha(), (50, 50))
        self.image_camera = pygame.transform.scale(pygame.image.load('Image/stats/kamera.png').convert_alpha(), (50, 50))
        self.window = window
        self.amount_photo = 0
        self.game = True


    def show_health(self, hero):
        x = 10
        for hp in range(hero.health):
            self.window.blit(self.image_hp,(x,20))
            x += 50


    def draw_photo(self):
        print_score = pygame.font.SysFont('comicsansms', 50).render(str(self.amount_photo),True,(209,52,52))
        self.window.blit(self.image_camera, (1050, 20))
        self.window.blit(print_score, (1110, 10))
    def finish(self, hero):
        if hero.health < 1:
            finish_text = pygame.font.SysFont('comicsansms', 50).render('ВЫ ПРОИГРАЛИ !',True,(209, 52, 52))
            self.window.blit(finish_text, (400,400))
            self.game = False
        elif self.amount_photo > 10:
            finish_text = pygame.font.SysFont('comicsansms', 50).render(f'ПОЗДРАВЛЯЮ! ВЫ СДЕЛАЛИ {self.amount_photo} ФОТО!', True, (209, 52, 52))
            self.window.blit(finish_text, (100,90))
            self.game = False

