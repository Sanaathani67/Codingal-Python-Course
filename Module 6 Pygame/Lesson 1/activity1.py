import pygame

pygame.init()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600

display_surface= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done=False

#not False=True
#not True= False

#game loop 
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.display.flip()  