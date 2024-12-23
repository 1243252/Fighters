import pygame
import random

from settings import Screen_Height, Screen_Width, FPS, White, Black
from player import Player
from plattform import Platform
from enemy import Enemy


pygame.init() #pygame initialisieren

#Fenster
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Fighters")
clock = pygame.time.Clock()

#Gruppen für Sprites
#mit Gruppen kann man all darin enthaltenen Sprites gleichzeitig zeichnen oder aktualisieren
player_group = pygame.sprite.Group()


#Player erstellen
player = Player()
player_group.add(player)


#plattform gruppe erstellen
platform_group = pygame.sprite.Group()

platform1 = Platform(550, 550, 100, 20)
platform2 = Platform (200, 500, 50, 10)

platform_group.add(platform1)
platform_group.add(platform2)


#enemy Gruppe erstellen
enemy_group = pygame.sprite.Group()



#Main-Loop
running = True
while running:
    for event in pygame.event.get(): #pygame.event.get() holt alle Ereignisse, die seit dem letzten Frame passiert sind
        if event.type == pygame.QUIT:
            running = False

    #Eingaben des Players verarbeiten
    keys = pygame.key.get_pressed()
    player.update(keys, platform_group)

    if len(enemy_group) == 0:
        enemy = Enemy(Screen_Width, Screen_Height)
        enemy_group.add(enemy)

    if pygame.sprite.spritecollide(player, enemy_group, True):
        print("Spieler wurde getroffen")

    enemy_group.update()

    #Kollision prüfen von Spieler mit Enemy
    if pygame.sprite.spritecollide(player, enemy_group, True):
        print("Spieler wurde getroffen")

    #Bildschirm aktualisieren
    screen.fill(Black)
    player_group.draw(screen)
    platform_group.draw(screen)
    enemy_group.draw(screen)
    pygame.display.flip()

    #FPS
    clock.tick(FPS)

pygame.quit()
