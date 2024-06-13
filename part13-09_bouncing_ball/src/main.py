import pygame
import sys

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BALL_COLOR = (255, 0, 0)

ball_radius = 20
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_velocity_x = 1
ball_velocity_y = 1

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y


    if ball_x + ball_radius >= WINDOW_WIDTH or ball_x - ball_radius <= 0:
        ball_velocity_x *= -1
    if ball_y + ball_radius >= WINDOW_HEIGHT or ball_y - ball_radius <= 0:
        ball_velocity_y *= -1

    window.fill((0, 0, 0))

    pygame.draw.circle(window, BALL_COLOR, (ball_x, ball_y), ball_radius)

    pygame.display.update()

    clock.tick(60)