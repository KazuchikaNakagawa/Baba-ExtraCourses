class Board:
    """省略"""
    def update(self):
        # 下に動けるなら
        if self.moving_block.can_go_down(self.cursor, self.board):
            # 下に動かす
            self.cursor.move_down(self.moving_block, self)
        else:
            # ここに追加
            # ブロックを変えてしまう前に置いておきます
            self.fix()
            # 新しくブロックを生成する
            self.generate_block()