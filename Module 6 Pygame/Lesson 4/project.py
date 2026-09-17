import pygame
import random
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake and Mouse")

all_sprites = pygame.sprite.Group()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file):
        super().__init__()

        image_path = os.path.join(os.path.dirname(__file__), image_file)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0
        )
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0
        )


s1 = Sprite("snake.png")
s1.rect.x = random.randint(0, SCREEN_WIDTH - s1.rect.width)
s1.rect.y = random.randint(0, SCREEN_HEIGHT - s1.rect.height)
all_sprites.add(s1)

s2 = Sprite("mouse.png")
s2.rect.x = random.randint(0, SCREEN_WIDTH - s2.rect.width)
s2.rect.y = random.randint(0, SCREEN_HEIGHT - s2.rect.height)
all_sprites.add(s2)


running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_x
        ):
            running = False

    keys = pygame.key.get_pressed()

    x_change = (
        keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    ) * MOVEMENT_SPEED

    y_change = (
        keys[pygame.K_DOWN] - keys[pygame.K_UP]
    ) * MOVEMENT_SPEED

    s1.move(x_change, y_change)

    if s1.rect.colliderect(s2.rect):
        s2.rect.x = random.randint(0, SCREEN_WIDTH - s2.rect.width)
        s2.rect.y = random.randint(0, SCREEN_HEIGHT - s2.rect.height)

    screen.fill(pygame.Color("black"))

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(90)

pygame.quit()