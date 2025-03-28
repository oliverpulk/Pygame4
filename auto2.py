import pygame
pygame.init()

# Värvid
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
sinine_autoO = pygame.image.load("f1_blue.png")
sinine_auto = pygame.transform.rotate(sinine_autoO, 180)

sinine_auto2o = pygame.image.load("f1_blue.png")
sinine_auto2 = pygame.transform.rotate(sinine_auto2o, 180)

sinine_auto3o = pygame.image.load("f1_blue.png")
sinine_auto3 = pygame.transform.rotate(sinine_auto3o, 180)


def reset_game():
    global player_x, player_y, player_speed, PosX, PosY, PosX2, PosY2, PosX3, PosY3, speed, speed2, speed3, score, gameover
    # Mängija auto algasend
player_x = 300
player_y = 390
player_speed = 0.1

# Vastaste autod
PosX, PosY = 180, 0
PosX2, PosY2 = 410, 200
PosX3, PosY3 = 300, 120
speed = 0.03
speed2 = 0.02
speed3 = 0.023

# Font skoori jaoks
font = pygame.font.SysFont(None, 36)
score = 0

gameover = False

# Mängu tsükkel
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:   # Kui vajutatakse vasakule noolt
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:  # Kui vajutatakse paremale noolt
        player_x += player_speed


    # Veendume, et auto ei läheks ekraanilt välja
    if player_x < 146:
        player_x = 146
    if player_x > 495 - punane_auto.get_width():
        player_x = 495 - punane_auto.get_width()

    # Taust ja autod
    screen.blit(Rally, [0,0])
    screen.blit(punane_auto, (player_x, player_y))
    screen.blit(sinine_auto, (PosX, PosY))
    screen.blit(sinine_auto2, (PosX2, PosY2))
    screen.blit(sinine_auto3, (PosX3, PosY3))

    # Vastaste liikumine
    PosY += speed
    PosY2 += speed2
    PosY3 += speed3

    # Kui autod jõuavad alla, alustavad uuesti ülevalt ja lisatakse skoori
    if PosY > 480:
        PosY = -sinine_auto.get_height()
        score += 1

    if PosY2 > 480:
        PosY2 = -sinine_auto2.get_height()
        score += 1

    if PosY3 > 480:
        PosY3 = -sinine_auto3.get_height()
        score += 1

    # Skoori kuvamine
    score_text = font.render("Skoor: " + str(score), True, Black)
    screen.blit(score_text, (10, 10))

    player_rect = pygame.Rect(player_x, player_y, punane_auto.get_width(), punane_auto.get_height())
    enemy_rect1 = pygame.Rect(PosX, PosY, sinine_auto.get_width(), sinine_auto.get_height())
    enemy_rect2 = pygame.Rect(PosX2, PosY2, sinine_auto2.get_width(), sinine_auto2.get_height())
    enemy_rect3 = pygame.Rect(PosX3, PosY3, sinine_auto3.get_width(), sinine_auto3.get_height())

    if player_rect.colliderect(enemy_rect1) or player_rect.colliderect(enemy_rect2) or player_rect.colliderect(
            enemy_rect3):
        gameover = True  # Mäng peatub, kuid ei sulgu

    else:
        # Kui mäng on läbi, näitame Game Over teksti ja ootame, et mängija vajutaks ENTER
        gameover_text = font.render("MÄNG LÄBI! Vajuta ENTER, et uuesti alustada", True, Black)
        screen.blit(gameover_text, (100, 240))

        if keys[pygame.K_RETURN]:  # Kui vajutatakse ENTER
            reset_game()

        # ESC-klahviga saab väljuda
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()

pygame.quit()
