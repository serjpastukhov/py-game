import pygame

class Player(pygame.Rect):
    def __init__(self, x, y, width, height):
        self.speed = 5
        self.target_x = x
        self.target_y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.rect = pygame.Rect(x, y, width, height)

    def move_to(self, x, y):
        self.target_x, self.target_y = x - self.width // 2, y - self.height // 2

    def update(self, obstacles):
        prev_x, prev_y = self.x, self.y

        dx, dy = self.target_x - self.x, self.target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > self.speed:
            self.x += dx * self.speed / distance
            self.y += dy * self.speed / distance

        self.rect.x, self.rect.y = self.x, self.y

        if self.check_collision(obstacles):
            self.x, self.y = prev_x, prev_y
            self.rect.x, self.rect.y = self.x, self.y

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return True
        return False

    def draw(self, screen, apply_camera):
        pygame.draw.rect(screen, (0, 0, 255), apply_camera(self))
        