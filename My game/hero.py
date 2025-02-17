import pygame

class Hero:
    def __init__(self, window):
        self.index = 0
        self.move_right = [pygame.transform.scale(pygame.image.load('image/hero/right1.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right2.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right3.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right4.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right5.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right6.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right7.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right8.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right9.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/right10.png').convert_alpha(),(220,90)),]
        self.move_left = [pygame.transform.scale(pygame.image.load('image/hero/Left1.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left2.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left3.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left4.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left5.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left6.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left7.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left8.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left9.png').convert_alpha(),(220,90)),
                           pygame.transform.scale(pygame.image.load('image/hero/Left10.png').convert_alpha(),(220,90)),]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(600, 400))
        self.speed = 3
        self.health = 3

    def update(self):
        self.image = self.move_right[self.index // 6]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.image = self.move_right[self.index // 6]
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 12:
            self.image = self.move_left[self.index // 6]
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.y > 178:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 628:
            self.rect.y += self.speed
        if self.index < 54:
            self.index += 1
        else:
            self.index = 0
        self.window.blit(self.image, self.rect)

