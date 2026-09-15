import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Car")

ROAD = pygame.Color(60, 60, 60)
CAR = pygame.Color(0, 100, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
WHITE = pygame.Color(255, 255, 255)
DARK = pygame.Color(30, 30, 30)

CAR_COLOUR_CHANGE = pygame.USEREVENT + 1
SIGNAL_CHANGE = pygame.USEREVENT + 2


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((80, 40))
        self.image.fill(CAR)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.velocity = 5

    def update(self):
        self.rect.move_ip(self.velocity, 0)

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity = -self.velocity

            pygame.event.post(
                pygame.event.Event(CAR_COLOUR_CHANGE)
            )

            pygame.event.post(
                pygame.event.Event(SIGNAL_CHANGE)
            )


car = Car()

group = pygame.sprite.Group()
group.add(car)

signal_colour = RED

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == CAR_COLOUR_CHANGE:
            car.image.fill(
                pygame.Color(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )

        elif event.type == SIGNAL_CHANGE:
            if signal_colour == RED:
                signal_colour = GREEN
            else:
                signal_colour = RED

    screen.fill(WHITE)

    # Road
    pygame.draw.rect(screen, ROAD, (0, 180, WIDTH, 140))

    # Traffic signal pole
    pygame.draw.rect(
        screen,
        DARK,
        (WIDTH - 60, 140, 10, 80)
    )

    # Tall rectangular traffic signal
    pygame.draw.rect(
        screen,
        DARK,
        (WIDTH - 90, 40, 70, 100)
    )

    # One changing light
    pygame.draw.circle(
        screen,
        signal_colour,
        (WIDTH - 55, 90),
        25
    )

    group.update()
    group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()