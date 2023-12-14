import os
import random
import sys

import pygame


pygame.init()
SIZE = WIDTH, HEIGHT = 500, 500

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
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.image.get_size()[0])
        self.rect.y = random.randrange(HEIGHT - self.image.get_size()[1])

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


fps = 60
clock = pygame.time.Clock()
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()


for _ in range(20):
    Bomb(all_sprites)

running = True
screen.fill((0, 0, 0))
x, y = 0, 0
pygame.mouse.set_visible(True)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update(event)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
