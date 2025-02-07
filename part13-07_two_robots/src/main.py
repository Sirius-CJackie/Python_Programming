# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
x1 = 0
y = 0
velocity1 = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x1, y+200))
    pygame.display.flip()
    
    x += velocity1
    x1 += velocity2
    if velocity1 > 0 and x+robot.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x <= 0:
        velocity1 = -velocity1
    if velocity2 > 0 and x1+robot.get_width() >= 640:
        velocity2 = -velocity2
    if velocity1 < 0 and x1 <= 0:
        velocity2 = -velocity2


    clock.tick(60)