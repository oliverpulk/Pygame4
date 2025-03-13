import pygame


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2")


bg = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")
logo = pygame.image.load("VIKK logo.png")
sword = pygame.image.load("mõõk.png")
tort = pygame.image.load("tort.png")


seller = pygame.transform.scale(seller, (248, 294))
chat = pygame.transform.scale(chat, (230, 183))
logo = pygame.transform.scale(logo, (265. , 45))
sword = pygame.transform.scale(sword, (173, 143))
tort = pygame.transform.scale(tort, (100, 93))

# Fondi seaded
font = pygame.font.Font(None, 33)
text = font.render("Oliver Pulk", True, (255, 255, 255))
arc_font = pygame.font.Font(None, 30)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(bg, (0, 0))
    screen.blit(logo, (10, 10))
    screen.blit(seller, (90, 150))
    screen.blit(chat, (216, 75))
    screen.blit(text, (236, 140))
    screen.blit(tort, (420, 200))
    screen.blit(sword, (515, 100))

    pygame.display.flip()

pygame.quit()