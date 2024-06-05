import pygame
from tetris import Board
# chapter 6 ブロックを動かす
# OBlockをインポートします
from tetris import OBlock

def main():
    # Create the board
    board = Board(tile_size=30)

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(board.window_size())
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # chapter 6 ブロックを動かす
    # とりあえずOブロックを作っておきます
    # 将来はランダムに作ります
    board.moving_block = OBlock()

    while True:
        # Draw the board
        board.draw(screen)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            board.cursor.move_left()
            pygame.time.wait(100)
        if keys[pygame.K_RIGHT]:
            board.cursor.move_right()
            pygame.time.wait(100)
        if keys[pygame.K_DOWN]:
            board.cursor.move_down()
            pygame.time.wait(100)
        # Update the display
        pygame.display.update()

        # Tick
        clock.tick(60)

if __name__ == "__main__":
    main()