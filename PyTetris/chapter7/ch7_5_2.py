class Board:
    """省略"""
    """一番下あたりに書いてください"""
    def block_rotate(self):
        if self.moving_block.can_rotate(self.cursor, self.board_data):
            self.moving_block.rotate()