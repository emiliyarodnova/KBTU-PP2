import pygame
import math
from datetime import datetime


def get_time():
    now = datetime.now()
    return now.minute, now.second


def get_angles(minutes, seconds):
    minute_angle = minutes * 6
    second_angle = seconds * 6
    return minute_angle, second_angle


def draw_hand(screen, center_x, center_y, angle, length, color, width):
    rad = math.radians(angle - 90)

    end_x = center_x + length * math.cos(rad)
    end_y = center_y + length * math.sin(rad)

    pygame.draw.line(screen, color, (center_x, center_y), (end_x, end_y), width)


def draw_clock(screen, background, center_x, center_y):
    screen.blit(background, (0, 0))

    minutes, seconds = get_time()
    minute_angle, second_angle = get_angles(minutes, seconds)

    draw_hand(screen, center_x, center_y, minute_angle, 100, (0, 0, 0), 6)

    draw_hand(screen, center_x, center_y, second_angle, 140, (255, 0, 0), 3)
