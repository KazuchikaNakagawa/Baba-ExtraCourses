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
LIGHT_GRAY = (200, 200, 200)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

def main():
    # Create the board
    """
    盤面と対応するリストを作ります
    盤面は幅１０高さ２２なので
    「黒を１０個並べたもの」を２２個並べたリストを作ります
    下の表記はリスト内包表記と呼ばれるものです
    [0 for _ in range(10)] は [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] と同じです.

    今回は最初の状態として全てのマスを黒にしています。
    """
    board = [[BLACK for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Initialize pygame
    # なぜ呼ぶのかは考えなくてOK
    pygame.init()

    # 画面の解像度を設定して作成
    # この行があって初めてウィンドウが作成される
    screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))

    # ウィンドウのタイトルを設定
    pygame.display.set_caption("Tetris")

    # ゲーム内の時刻を表す変数になります
    clock = pygame.time.Clock()

    while True:
        # 画面を表示します
        # 縦にHEIGHT(22)回、
        for y in range(HEIGHT):
            # 横にWIDTH(10)回、
            for x in range(WIDTH):
                # それぞれのマスを描画します
                pygame.draw.rect(screen, board[y][x], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # 線を描画します
        # 縦線を22本
        for y in range(HEIGHT):
            pygame.draw.line(screen, GRAY, (0, y * TILE_SIZE), (WIDTH * TILE_SIZE, y * TILE_SIZE))
        # 横線を10本
        for x in range(WIDTH):
            pygame.draw.line(screen, GRAY, (x * TILE_SIZE, 0), (x * TILE_SIZE, HEIGHT * TILE_SIZE))
        
        # 画面が消されたらmainもreturnで終了します
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # この行で描画内容が実際のモニターに反映されます
        pygame.display.update()

        # 画面の更新頻度を設定します。この場合は一秒間に60回更新します
        clock.tick(60) # 60fps

if __name__ == "__main__":
    main()