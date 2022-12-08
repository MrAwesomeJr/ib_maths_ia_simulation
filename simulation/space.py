import pygame

class Space:
    def __init__(self, x_fov, y_fov):
        self.x_fov = x_fov
        self.y_fov = y_fov
        self.x = 0
        self.y = 0
        self.z = 0
        self.objects = []
        self.sensitivity = 50
        self.angle_sensitivity = 15
        self.x_angle = 0
        self.y_angle = 0

    def update_space(self):
        self.get_input()

    def get_input(self):
        key_down_events = pygame.event.get(eventtype=pygame.KEYDOWN)

        for key_event in key_down_events:
            if key_event.key in (pygame.K_LEFT, pygame.K_a):
                self.x -= self.sensitivity
            elif key_event.key in (pygame.K_RIGHT, pygame.K_d):
                self.x += self.sensitivity
            elif key_event.key in (pygame.K_UP, pygame.K_w):
                self.z += self.sensitivity
            elif key_event.key in (pygame.K_DOWN, pygame.K_s):
                self.z -= self.sensitivity
            elif key_event.key == pygame.K_SPACE:
                self.y += self.sensitivity
            elif key_event.key == pygame.K_LSHIFT:
                self.y -= self.sensitivity
            elif key_event.key == pygame.K_j:
                self.x_angle -= self.angle_sensitivity
            elif key_event.key == pygame.K_l:
                self.x_angle += self.angle_sensitivity
            elif key_event.key == pygame.K_i:
                self.y_angle += self.angle_sensitivity
            elif key_event.key == pygame.K_k:
                self.y_angle -= self.angle_sensitivity

    def coords(self):
        return (self.x, self.y, self.z)