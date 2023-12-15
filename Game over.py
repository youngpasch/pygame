import os
import random
import sys

import pygame


IMG_NAME = "gameover.png"
COLOR = (255, 255, 255)
pygame.init()
SIZE = WIDTH, HEIGHT = 600, 300

screen = pygame.display.set_mode(SIZE)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


class GameOver(pygame.sprite.Sprite):
    image = load_image(IMG_NAME)

    def __init__(self, group):
        super().__init__(group)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.x, self.y = - self.image.get_size()[0], 0
        self.rect = self.rect.move(self.x, 0)

    def update(self, *args):
        if args and self.rect.x + self.image.get_size()[0] < WIDTH:
            speed = args[0]
            self.rect.x += speed


fps = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


GameOver(all_sprites)

running = True
screen.fill((0, 0, 255))
x, y = 0, 0
speed = 200
pygame.mouse.set_visible(True)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 255))
    all_sprites.draw(screen)
    all_sprites.update(speed / fps)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
