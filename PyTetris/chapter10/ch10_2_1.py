class Board:
    """省略"""
    """一番下あたりに書いてください"""
    def fix(self):
        """ブロックの情報をboardに書き込んでいきます"""
        block_info = self.moving_block.get_block_info(self.cursor)
        block_color = self.moving_block.color
        for pos in block_info:
            """posには、(x, y)の形で座標が入っています"""
            """boardには[y][x]の形でアクセスしないといけないので、posを逆にしています"""
            self.board[pos[1]][pos[0]] = block_color
        