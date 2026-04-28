import pygame
from ball import draw_ball, move_ball

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball_x = 400
ball_y = 300
ball_radius = 25
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    ball_x, ball_y = move_ball(
        keys,
        ball_x,
        ball_y,
        speed,
        ball_radius,
        screen_width,
        screen_height
    )

    screen.fill((255, 255, 255))
    draw_ball(screen, ball_x, ball_y, ball_radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
