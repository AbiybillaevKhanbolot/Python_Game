import pygame
from enemy import Enemy
from random import randint
from sound import take_photo, bite_akulla, heal_hero


def event(enemies, scores, group_pearls, pearl, window):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            make_pearl(group_pearls, pearl)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                do_pause(window)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for fish in enemies:
                if fish.rect.collidepoint(x, y):
                    take_photo()
                    enemies.remove(fish)
                    fish.image = pygame.transform.scale(pygame.image.load('Image/Fish/Fishik1.png'), (70, 50))
                    fish.speed = 4
                    scores.amount_photo += 1

        if event.type == pygame.QUIT:
            exit()

def make_fish(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4,7))
        enemies.add(enemy)
        friends.add(enemy)
def make_friends(friends,window):
    friends.update()
    friends.draw(window)

def make_pearl(group_pearls, pearl):
    group_pearls.add(pearl)

def move_pearls(window, group_pearls):
    group_pearls.update()
    group_pearls.draw(window)


def collide(hero, enemies, group_pearls):
    if pygame.sprite.spritecollide(hero, enemies, True):
        bite_akulla()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero, group_pearls, True):
        if hero.health < 3:
            hero.health += 1
            heal_hero()

def do_pause(window):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pause_text = pygame.font.SysFont('comicsansms',50).render('ПАУЗА! Нажмите пробел для продолжения', True, (209, 52, 52))
        window.blit(pause_text, (200, 400))
        pygame.display.update()

