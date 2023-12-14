import os
import random
import sys

import pygame


IMG_NAME = "car2.png"
COLOR = (255, 255, 255)
pygame.init()
SIZE = WIDTH, HEIGHT = 600, 95

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


class Bomb(pygame.sprite.Sprite):
    image = load_image(IMG_NAME)
    image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.x, self.y = 0, 0
        self.direction = 1

    def update(self, *args):
        self.x += 5 * self.direction
        self.rect = self.rect.move(5 * self.direction,
                                   0)
        self.reverse_check()

    def reverse_check(self):
        if self.x + self.image.get_size()[0] >= WIDTH or self.x<= 0:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)



fps = 60
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


Bomb(all_sprites)

running = True
screen.fill((0, 0, 0))
x, y = 0, 0
pygame.mouse.set_visible(True)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update(event)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
