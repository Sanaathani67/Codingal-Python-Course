import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT=500, 400
MOVEMENT_SPEED=5
FONT_SIZE= 72

pygame.init()

font=pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__ (self, colour, height, width):
        super().__init__()
        self.image=pygame.Surface([width, height])
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, height, width))
        self.rect=self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x=max(min(self.rect.x+x_change, SCREEN_WIDTH-self.rect.width), 0)
        self.rect.y=max(min(self.rect.y+y_change, SCREEN_HEIGHT-self.rect.height), 0)


# Setup

screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.Group()


# Create the sprites
s1=Sprite((255, 215, 0), 30, 30)
s1.rect.x=random.randint(0, SCREEN_WIDTH-s1.rect.width)
s1.rect.y=random.randint(0, SCREEN_HEIGHT-s1.rect.height)
all_sprites.add(s1)
s2=Sprite((0, 255, 127), 30, 30)
s2.rect.x=random.randint(0, SCREEN_WIDTH-s2.rect.width)
s2.rect.y=random.randint(0, SCREEN_HEIGHT-s2.rect.height)
all_sprites.add(s2)


# Game loop control variables

running = True

won = False

clock = pygame.time.Clock()

# Main game loop

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):

            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT]- keys[pygame.K_LEFT])*MOVEMENT_SPEED
        y_change=(keys[pygame.K_DOWN]- keys[pygame.K_UP])*MOVEMENT_SPEED
        s1.move(x_change, y_change)

        if s1.rect.colliderect(s2.rect):
            all_sprites.remove(s2)
            #PROJECT: instesd of removing the sprite, can i respawn the sorite to another random location
            won=True

    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)

    if won:
        win_text=font.render(" you win!!!!", True, pygame.Color("white"))
        text_x=(SCREEN_WIDTH-win_text.get_width())//2
        text_y=(SCREEN_HEIGHT-win_text.get_height())//2
        screen.blit(win_text, (text_x, text_y))

    pygame.display.flip()

    clock.tick(90)

pygame.quit()