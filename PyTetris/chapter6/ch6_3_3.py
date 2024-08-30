class Cursor:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = 0

    # カーソルは動く時にblockという引数と
    # boardをもらうことにします
    # こうしないとblockの
    # can_go_left関数が使えません
    def move_left(self, block, board):
        # もし、blockが左に動けるなら
        if """blockが左に動けるかを返す関数""":
            # カーソルを左に動かします
            self.x = max(0, self.x - 1)

    # 残りも変えてみましょう
    def move_right(self):
        self.x = min(WIDTH - 1, self.x + 1)
    def move_down(self):
        self.y = min(HEIGHT - 1, self.y + 1)
    def move_up(self):
        self.y = max(0, self.y - 1)