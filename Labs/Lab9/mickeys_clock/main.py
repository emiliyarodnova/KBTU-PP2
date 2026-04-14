import pygame
import os
from clock import draw_clock


WIDTH = 1000
HEIGHT = 1000
FPS = 60

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2 - 30


def load_image(path):
    return pygame.image.load(path).convert()


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "images", "mickeyclock.jpeg")

background = load_image(image_path)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock(screen, background, CENTER_X, CENTER_Y)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
