import pygame

pygame.init()
screen=pygame.display.set_mode((400, 300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen, (221, 160, 221), pygame.Rect(30,100,120,60))

    pygame.display.flip()