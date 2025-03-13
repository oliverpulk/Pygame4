import pygame


def draw_grid(screen, square_size, rows, cols, line_color):
    """Joonistab ekraanile ruudustiku."""
    screen.fill((144, 238, 144))  # Taust roheline
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, line_color, rect, 2)  # 2px paksune joon


def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    square_size = 20  # Muuda siit ruudu suurust
    rows = HEIGHT // square_size
    cols = WIDTH // square_size
    line_color = (255, 0, 0)  # Punane joon

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Harjutamine")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(screen, square_size, rows, cols, line_color)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
