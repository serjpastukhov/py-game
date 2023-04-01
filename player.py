import pygame

class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.speed = 5
        self.target_x = x
        self.target_y = y

    def move_to(self, x, y):
        self.target_x, self.target_y = x - self.width // 2, y - self.height // 2

    def update(self):
        dx, dy = self.target_x - self.x, self.target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > self.speed:
            self.x += dx * self.speed / distance
            self.y += dy * self.speed / distance

    def draw(self, screen, apply_camera):
        pygame.draw.rect(screen, (0, 0, 255), apply_camera(self))
        