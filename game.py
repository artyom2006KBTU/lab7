import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
BALL_RADIUS = 25
STEP = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

x, y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - BALL_RADIUS - STEP >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + BALL_RADIUS + STEP <= HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x - BALL_RADIUS - STEP >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + BALL_RADIUS + STEP <= WIDTH:
                x += STEP

pygame.quit()
