import pygame

class Camera:
    def __init__(self, width, height, screen_width, screen_height):
        self.viewport = pygame.Rect(0, 0, screen_width, screen_height)
        self.position = pygame.math.Vector2(0, 0)
        self.target_position = pygame.math.Vector2(0, 0)
        self.speed = 0.1
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def move(self, dx, dy):
        new_target_position = self.target_position + pygame.math.Vector2(dx, dy)

        # Ограничение движения камеры в пределах игрового поля
        if 0 <= new_target_position.x <= self.width - self.screen_width:
            self.target_position.x = new_target_position.x
        if 0 <= new_target_position.y <= self.height - self.screen_height:
            self.target_position.y = new_target_position.y
        

    def update(self):
        self.position.x += (self.target_position.x - self.position.x) * self.speed
        self.position.y += (self.target_position.y - self.position.y) * self.speed

        self.viewport = pygame.Rect(self.position.x, self.position.y, self.screen_width, self.screen_height)

    def apply(self, rect):
        return rect.move(-self.viewport.x, -self.viewport.y)
    
    def apply_float(self, rect):
        return rect.move(-self.position.x, -self.position.y)
