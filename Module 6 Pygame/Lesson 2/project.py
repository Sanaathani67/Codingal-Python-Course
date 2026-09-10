import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

PAPAYA_WHIP = (255, 239, 213)
HOT_PINK = (255, 105, 180)
ORANGE_RED = (255, 69, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 0)

current_color = WHITE

x, y = 30, 30
sprite_width, sprite_height = 60, 60
radius = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x -= 3

    if pressed[pygame.K_RIGHT]:
        x += 3

    if pressed[pygame.K_UP]:
        y -= 3

    if pressed[pygame.K_DOWN]:
        y += 3

    x = min(max(0, x), 500 - sprite_width)
    y = min(max(0, y), 500 - sprite_height)

    if x == 0:
        current_color = BLUE
    elif x == 500 - sprite_width:
        current_color = HOT_PINK
    elif y == 0:
        current_color = ORANGE_RED
    elif y == 500 - sprite_height:
        current_color = PAPAYA_WHIP
    else:
        current_color = WHITE

    screen.fill((0, 0, 0))

    pygame.draw.circle(
        screen,
        current_color,
        (x + radius, y + radius),
        radius
    )

    pygame.display.flip()
    clock.tick(90)

pygame.quit()