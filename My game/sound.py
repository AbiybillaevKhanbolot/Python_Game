import pygame

def bg_music():
    pygame.mixer.music.load('Sound/81cebf7e45fdef7.mp3')
    pygame.mixer.music.play(-1)

def take_photo():
    take_photo = pygame.mixer.Sound('Sound/zvuk-foto-na-ayfone.mp3')
    take_photo.play()

def bite_akulla():
    bite =pygame.mixer.Sound('Sound/e8a7967cf751e7d.mp3')
    bite.play()

def heal_hero():
    heal =pygame.mixer.Sound('Sound/22d98ea70c3b3ae.mp3')
    heal.play()

