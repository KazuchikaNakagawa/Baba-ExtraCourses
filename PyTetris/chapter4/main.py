import pygame
from tetris2 import Board

def main():
    # 作ったクラスを変数に入れてみます
    board = Board()

    # Initialize pygame
    pygame.init()

    # ウィンドウのサイズはboardのwindow_size()メソッドで取得できることにします
    # def window_size(self): の部分に対応しています
    screen = pygame.display.set_mode(board.window_size())

    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    while True:
        # ボードを描画
        # def draw(self, screen): の部分に対応しています
        board.draw(screen)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update the display
        pygame.display.update()

        # Tick
        clock.tick(60)

if __name__ == "__main__":
    main()