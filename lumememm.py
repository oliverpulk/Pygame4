import pygame

# Initsialiseeri Pygame
pygame.init()

# Akna seaded
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumemees - Sinu Nimi")

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# Tausta värv
screen.fill(BLACK)

# Lumememme joonistamine (kolm ringi)
pygame.draw.circle(screen, WHITE, (150, 80), 30)  # Pea
pygame.draw.circle(screen, WHITE, (150, 140), 40)  # Keha
pygame.draw.circle(screen, WHITE, (150, 220), 50)  # Alumine osa

# Silmad
pygame.draw.circle(screen, BLACK, (140, 70), 5)  # Vasak silm
pygame.draw.circle(screen, BLACK, (160, 70), 5)  # Parem silm

# Nina
pygame.draw.polygon(screen, ORANGE, [(150, 80), (140, 90), (160, 90)])

# Suu
pygame.draw.arc(screen, RED, (135, 75, 30, 20), 3.14, 0, 2)

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()