import pygame
from tetris import Board

def main():
    # Create the board
    board = Board(tile_size=30)

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(board.window_size())
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    while True:
        # Draw the board
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