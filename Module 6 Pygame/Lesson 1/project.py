import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Facts")

background = pygame.image.load(r"Module 6 Pygame\Lesson 1\background.png")
tiger = pygame.image.load(r"Module 6 Pygame\Lesson 1\tiger.png")

background = pygame.transform.scale(background, (800, 500))
tiger = pygame.transform.scale(tiger, (250, 180))

tiger_rect = tiger.get_rect(center=(400, 280))

heading_font = pygame.font.Font(None, 50)
fact_font = pygame.font.Font(None, 30)

heading = heading_font.render("Tiger Facts", True, (255, 255, 255))
fact = fact_font.render(
    "Tigers are the largest members of the cat family.",
    True,
    (255, 255, 255)
)

heading_rect = heading.get_rect(center=(400, 50))
fact_rect = fact.get_rect(center=(400, 470))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(tiger, tiger_rect)
        screen.blit(heading, heading_rect)
        screen.blit(fact, fact_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

game_loop()