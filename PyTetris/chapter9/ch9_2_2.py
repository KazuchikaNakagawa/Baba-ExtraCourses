def main():
    # Create the board
    board = Board(tile_size=30)

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(board.window_size())
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    # chapter 9 ブロックを生成する
    # ここを消してしまいます。
    # 3行目のBoard()の中で生成しているので、ここで生成する必要がなくなります。
    board.moving_block = TBlock()

    while True:
        """省略"""
        # key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            board.cursor_move_left()
            pygame.time.wait(100)
        if keys[pygame.K_RIGHT]:
            board.cursor_move_right()
            pygame.time.wait(100)
        if keys[pygame.K_DOWN]:
            board.cursor_move_down()
            pygame.time.wait(100)
        if keys[pygame.K_r]:
            board.block_rotate()
            pygame.time.wait(100)
        
        if keys[pygame.K_SPACE]:
            board.drop()
            pygame.time.wait(100)