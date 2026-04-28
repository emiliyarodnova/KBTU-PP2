import pygame

def draw_ball(screen, x, y, radius):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)


def move_ball(keys, x, y, speed, radius, screen_width, screen_height):
    if keys[pygame.K_LEFT]:
        if x - speed - radius >= 0:
            x -= speed

    if keys[pygame.K_RIGHT]:
        if x + speed + radius <= screen_width:
            x += speed

    if keys[pygame.K_UP]:
        if y - speed - radius >= 0:
            y -= speed

    if keys[pygame.K_DOWN]:
        if y + speed + radius <= screen_height:
            y += speed

    return x, y
