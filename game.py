import pygame
from player import Player
from camera import Camera

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(50, 50)
        self.camera = Camera(3200, 3200, 800, 600)

    # Функция обработки событий
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    x, y = event.pos
                    self.player.move_to(x + self.camera.viewport.x, y + self.camera.viewport.y)

        keys = pygame.key.get_pressed()
        move_speed = 10
        if keys[pygame.K_UP]:
            self.camera.move(0, -move_speed)
            print("Camera position:", self.camera.target_position)
        if keys[pygame.K_DOWN]:
            self.camera.move(0, move_speed)
            print("Camera position:", self.camera.target_position)
        if keys[pygame.K_LEFT]:
            self.camera.move(-move_speed, 0)
            print("Camera position:", self.camera.target_position)
        if keys[pygame.K_RIGHT]:
            self.camera.move(move_speed, 0)
            print("Camera position:", self.camera.target_position)
                
    # Функция обновления состояния игры
    def update(self):
        self.camera.update()
        self.player.update()

    # Функция рисования игровых объектов
    def draw(self):
        self.screen.fill((0, 0, 0))

        cell_size = 100
        for i in range(0, 3200, cell_size):
            for j in range(0, 3200, cell_size):
                if (i // cell_size + j // cell_size) % 2 == 0:
                    color = (230, 230, 230)
                else:
                    color = (150, 150, 150)
                rect = pygame.Rect(i, j, cell_size, cell_size)
                adjusted_rect = self.camera.apply_float(rect)
                pygame.draw.rect(self.screen, color, pygame.Rect(round(adjusted_rect.x), round(adjusted_rect.y), cell_size, cell_size))
        self.player.draw(self.screen, self.camera.apply)
        pygame.display.flip()

    # Функция запуска основного цикла игры
    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60) # Ограничение до 60 кадров в секунду
