import pygame
from .obstacle import Obstacle

class Level:
    def __init__(self) -> None:
        self.obstacles = pygame.sprite.Group()

    def create_obstacles(self):
        self.obstacles.add(Obstacle(100, 200, 50, 50, 'images\\obstacles\\pngwing.png'))
        self.obstacles.add(Obstacle(400, 100, 50, 50, 'images\\obstacles\\pngwing.png'))

    def draw(self, surface, camera):
        for obstacle in self.obstacles:
            if camera.rect.colliderect(obstacle.rect):
                surface.blit(obstacle.image, camera.apply(obstacle.rect))
