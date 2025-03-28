import pygame, sys
import pygame, sys, random

pygame.init()

# Värvid
red = [255, 0, 0]
lBlue = [153, 204, 255]

# Ekraani seaded
screenX, screenY = 640, 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()

# Graafika laadimine
ball = pygame.image.load("pall.png")

# Palli kiirus ja asukoht
ballX, ballY = random.randint(0, screenX - ball.get_width()), random.randint(0, screenY - ball.get_height())
speedX, speedY = 3, 4

# Ruudukeste koordinaadid ja kiirused
coords = [[random.randint(0, screenX), random.randint(-50, screenY)] for _ in range(10)]
speeds = [random.randint(1, 4) for _ in range(10)]  # Erinevad kiirused ruudukestele

running = True
while running:
    clock.tick(60)  # Kaadrisagedus

    # Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(lBlue)  # Tausta värvimine

    # Ruudukeste liikumine
    for i in range(len(coords)):
        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += speeds[i]

        # Kui jõuab alla, alustame uuesti ülal
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)

    # Palli liikumine
    screen.blit(ball, (ballX, ballY))
    ballX += speedX
    ballY += speedY

    # Palli põrkumine ekraani servadelt
    if ballX > screenX - ball.get_width() or ballX < 0:
        speedX = -speedX
    if ballY > screenY - ball.get_height() or ballY < 0:
        speedY = -speedY

    pygame.display.flip()  # Ekraani uuendamine

pygame.quit()
sys.exit()
