import pygame
import sys
from screen import Screen
from space import Space
from render import *
from objects import *

x_fov = 70
y_fov = 70

pygame.init()
screen = Screen((255, 255, 255))
space = Space(x_fov, y_fov)
render3d = Render3D(screen, x_fov, y_fov, 672, 0, 768, 768)
render2d_topdown = Render2D_TopDown(screen, x_fov, y_fov, 0, 0, 672, 768)

space.objects.append(Point(0, 384, 500))
space.objects.append(Cube(0, 384, 500, 500))

while True:
    render2d_topdown.render(space)
    render3d.render(space)
    screen.update_screen()
    space.get_input()

    if len(pygame.event.get(eventtype=pygame.QUIT)) >= 1:
        sys.exit()