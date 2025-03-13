import pygame

# Initsialiseeri Pygame
pygame.init()

# Akna seaded
WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valgusfoor - Sinu Nimi")

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)
BLUE = (0, 102, 204)
ESTONIAN_BLACK = (0, 0, 0)
ESTONIAN_WHITE = (255, 255, 255)

# Tausta värv
screen.fill(BLACK)

# Foori kast
pygame.draw.rect(screen, GRAY, (110, 50, 80, 200), border_radius=10)

# Valgusfoori tuled
pygame.draw.circle(screen, RED, (150, 90), 30)
pygame.draw.circle(screen, YELLOW, (150, 150), 30)
pygame.draw.circle(screen, GREEN, (150, 210), 30)

# Foori post
pygame.draw.rect(screen, GRAY, (140, 250, 20, 80))

# Postialus (kolmnurk)
pygame.draw.polygon(screen, BLUE, [(120, 330), (180, 330), (150, 290)])  # Sinine
pygame.draw.polygon(screen, ESTONIAN_BLACK, [(120, 350), (180, 350), (150, 330)])  # Must
pygame.draw.polygon(screen, ESTONIAN_WHITE, [(120, 370), (180, 370), (150, 350)])  # Valge

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()