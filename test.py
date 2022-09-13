import pygame
from math import tan, atan, degrees, radians
import sys
pygame.init()

screen = pygame.display.set_mode((1440, 768))
clock = pygame.time.Clock()
clock.tick(1)

fov = 70
x = 100
x_intervals = 10
z = 100
w = screen.get_width()


while True:
    key_down_events = pygame.event.get(eventtype=pygame.KEYDOWN)
    key_up_events = pygame.event.get(eventtype=pygame.KEYUP)

    for key_event in key_down_events:
        if key_event.key in (pygame.K_LEFT, pygame.K_a):
            x -= x_intervals
        elif key_event.key in (pygame.K_RIGHT, pygame.K_d):
            x += x_intervals

    display_x = w / 2 * (1 + degrees(atan(x / (z + (2 * tan(radians(fov)) / w)))) / (2 * fov))
    print(x, z, "\t", display_x)

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (display_x, 500), 5)

    pygame.display.flip()

    if len(pygame.event.get(eventtype=pygame.QUIT)) >= 1:
        sys.exit()
