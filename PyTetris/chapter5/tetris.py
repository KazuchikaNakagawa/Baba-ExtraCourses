# tetris using pygame
import pygame

# Constants
WIDTH = 10
HEIGHT = 22
TILE_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
CURSOR_COLOR = (60, 60, 60)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

class Board:
    def __init__(self, tile_size):
        # 作る時にタイルサイズを指定する
        self.board = [[BLACK for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.TILE_SIZE = tile_size

        # Cursor
        self.cursor = Cursor()
    def draw(self, screen):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pygame.draw.rect(screen, self.board[y][x], (x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))

        # Draw the cursor
        for y in range(HEIGHT):
            if self.board[y][self.cursor.x] == BLACK:
                pygame.draw.rect(screen, CURSOR_COLOR, (self.cursor.x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
    
        # Draw the grid
        for y in range(HEIGHT):
            pygame.draw.line(screen, GRAY, (0, y * self.TILE_SIZE), (WIDTH * self.TILE_SIZE, y * self.TILE_SIZE))
        for x in range(WIDTH):
            pygame.draw.line(screen, GRAY, (x * self.TILE_SIZE, 0), (x * self.TILE_SIZE, HEIGHT * self.TILE_SIZE))

    def window_size(self):
        return (WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE)

class Cursor:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = 0
    def move_left(self):
        self.x = max(0, self.x - 1)
    def move_right(self):
        self.x = min(WIDTH - 1, self.x + 1)
    def move_down(self):
        self.y = min(HEIGHT - 1, self.y + 1)
    def move_up(self):
        self.y = max(0, self.y - 1)