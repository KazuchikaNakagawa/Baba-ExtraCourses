from random import randint

"""省略"""

class Board:
    def __init__(self):
        """省略"""
        # chapter 9 ブロックを生成する で追加
        # ブロックを生成します
        self.generate_block()
        
    """省略"""

    """一番下あたりに書いてください"""
    def generate_block(self):
        # 1に戻すのは、上にはみ出るブロックのためです
        """カーソルのy座標を1に戻します"""
        # ランダムにブロックを生成します
        block_type = randint(0, 6)
        if block_type == 0:
            self.moving_block = TBlock()
        elif block_type == 1:
            self.moving_block = OBlock()
        elif block_type == 2:
            self.moving_block = LBlock()
        elif block_type == 3:
            self.moving_block = JBlock()
        elif block_type == 4:
            self.moving_block = ZBlock()
        elif block_type == 5:
            self.moving_block = SBlock()
        elif block_type == 6:
            self.moving_block = IBlock()