import pygame

class Screen:
    def __init__(self, background_color):
        self.screen = pygame.display.set_mode((1440, 846))
        self.clock = pygame.time.Clock()
        self.clock.tick(1) # 1fps
        self.background_color = background_color
        self.screen.fill(self.background_color)

        self.font = pygame.font.Font("/Users/ryan.wong/Library/Fonts/GenshinImpact_ja-jp.ttf", 10)

    def update_screen(self):
        pygame.display.flip()
        self.screen.fill(self.background_color)

    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, width, height))

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def draw_line(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))

    def draw_polygon(self, points, color):
        pygame.draw.polygon(self.screen, color, points)

    def draw_text(self, text, x, y, size, color):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))