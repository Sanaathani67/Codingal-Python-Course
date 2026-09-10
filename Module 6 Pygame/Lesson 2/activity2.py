import pygame

pygame.init()
screen=pygame.display.set_mode((500, 500))
done=False

#(RGB)
#constant-uppercase
PAPAYA_WHIP=(255, 239, 213)
HOT_PINK=(255, 105, 180)
ORANGE_RED=(255, 69, 0)

screen.fill(PAPAYA_WHIP)


pygame.draw.circle(screen, HOT_PINK, (300, 300), 50)


pygame.draw.circle(screen, ORANGE_RED,(300,300), 50, 3)


pygame.display.update()


while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
   

    pygame.display.flip()

pygame.quit()