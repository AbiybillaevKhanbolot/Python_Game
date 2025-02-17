import pygame
import background as bg
import events
from hero import Hero
from sound import bg_music
from scores import Scores
from pearl import Pearl



def run():
    pygame.init()

    pygame.display.set_caption('Photo-Hunter')
    window = pygame.display.set_mode((bg.WIDHT, bg.HEIGHT))
    clock = pygame.time.Clock()
    background = bg.Background()
    hero = Hero(window)
    scores = Scores(window)

    enemies = pygame.sprite.Group()
    friends = pygame.sprite.Group()
    group_pearls = pygame.sprite.Group()

    pygame.time.set_timer(pygame.USEREVENT, 1000)

    bg_music()


    while True:
        pearl = Pearl()
        events.event(enemies, scores, group_pearls, pearl, window)
        if scores.game:

            background.update()
            background.render(window)
            hero.update()
            scores.show_health(hero)
            scores.draw_photo()
            scores.finish(hero)
            events.make_friends(friends, window)
            events.make_fish(enemies, window, friends)
            events.move_pearls(window, group_pearls)
            events.collide(hero, enemies, group_pearls)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    run()