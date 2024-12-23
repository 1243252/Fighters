import pygame
from plattform import Platform


class Player(pygame.sprite.Sprite): #Player-Klasse erbt von der Sprite-Klasse von pygame womit man Spielerobjekte verwaltet
    def __init__(self):
        super().__init__() #Konstruktor
        self.image = pygame.Surface((50, 50)) #Spielergröße
        self.image.fill((255, 255, 255)) #Farbe weiß; hier kann auch ein Bild rein (pygame.image.load)
        self.rect = self.image.get_rect() #gibt Rechteck mit der Größe und Position zurück
        self.rect.center = (450,575) #Startposition
        self.speed = 5

        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -15
        self.is_jumping = False

    def update(self, keys, platform_group):
        if keys[pygame.K_a] and self.rect.left > 0: #durch self.rect.left > 0 wird erkannt, wo die Ränder sind
            self.rect.x -= self.speed
            #jetzt wird geprüft, ob Spieler mit Plattform kollidiert, wenn er "a" drückt
            collided_platforms = pygame.sprite.spritecollide(self, platform_group, False)
            for platform in collided_platforms:
                if self.rect.left < platform.rect.right:
                    self.rect.left = platform.rect.right

        if keys[pygame.K_d] and self.rect.right < 800:
            self.rect.x += self.speed
            #geprüft, ob Spieler mit Plattform kollidiert, wenn er "d" drückt
            collided_platforms = pygame.sprite.spritecollide(self, platform_group, False)
            for platform in collided_platforms:
                if self.rect.right > platform.rect.left:
                    self.rect.right = platform.rect.left

        #Sprung starten
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_strength #wenn Leertaste gedrückt, dann wir velocity auf jump_strength gesetzt
            self.is_jumping = True #jump-Zustand wird auf true gesetzt

        #Schwerkraft anwenden
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y


        #vertikale Kollision
        collided_platforms = pygame.sprite.spritecollide(self, platform_group, False)
        if collided_platforms and self.velocity_y > 0:
            self.rect.bottom = collided_platforms[0].rect.top
            self.velocity_y = 0
            self.is_jumping = False

        #Bodenbeschränkung
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.is_jumping = False
            self.velocity_y = 0