import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((40, 40)) #Größe des Gegners
        self.image.fill((255, 0, 0)) #rote Farbe
        self.rect = self.image.get_rect()

        #zufällige Spawnposition
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height) #spawnt über dem Boden

        self.speed = 3 #zufällige Geschwindigkeit

    def update(self):

        #Bewegung nach unten
        self.rect.y += self.speed

        if self.rect.bottom >= 600:
            self.rect.bottom = 600

        #Entfernen, wenn der Gegner aus dem Bildschrim herausfällt
        if self.rect.top > 600:
            self.kill()
