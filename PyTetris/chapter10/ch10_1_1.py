class Board:
    """省略"""
    def update(self):
        # 下に動けるなら
        if self.moving_block.can_go_down(self.cursor, self.board):
            # 下に動かす
            self.cursor.move_down(self.moving_block, self)
        else:
            # 下に動けないなら
            # 新しくブロックを生成する
            self.generate_block()