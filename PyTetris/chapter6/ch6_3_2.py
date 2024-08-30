class OBlock:
    def __init__(self):
        self.color = YELLOW

    def block_info(self, cursor):
        """省略"""

    def rotate(self):
        pass

    # 左に動けるかを返すcan_go_left関数
    # 現在の座標を知るためにcursorを、盤面の情報を知るためにboard_dataを引数に取ります
    def can_go_left(self, cursor, board_data):
        # 今回はOブロックなので、cursorが0（左端）だと左に動けません
        if cursor.x == 0:
            return False
        # あと、カーソルの左と左下にブロックがあるときも左に動けません
        # ブロックが入っているということは、何かの色が入っているということです
        if board_data[cursor.y][cursor.x - 1] != BLACK:
            return False
        if board_data[cursor.y + 1][cursor.x - 1] != BLACK:
            return False
        # ここまで来たということは左に動けるということです
        return True
    
    # 右に動けるかを返すcan_go_right関数
    # 同じように作ってみましょう
    """この行を消して書いてみてください"""