import pygame
pygame.init()

# värvid
IGreen = [153, 255, 153]
Black = [0, 0, 0]

# Pildi loomine
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Ralliauto mäng")
screen.fill(IGreen)

# Taustapildi lisamine
Rally = pygame.image.load("bg_rally.jpg")
Rally = pygame.transform.scale(Rally, [640, 480])

# Autode lisamine
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

PosX, PosY = 180, 0
speed = 0.1

# Font skoori jaoks
font = pygame.font.SysFont(None, 36)
score = 0

gameover = False

# Mängu sulgemine ristist
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    screen.blit(Rally, [0,0])
    screen.blit(punane_auto, (300, 390))
    screen.blit(sinine_auto, (PosX, PosY))

    PosY += speed

    if PosY > 480:
        PosY = -sinine_auto.get_height()
        score += 1  # Lisame skoorile 1 punkti

    # Teksti loomine ja kuvamine
    score_text = font.render("Skoor: " + str(score), True, Black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()