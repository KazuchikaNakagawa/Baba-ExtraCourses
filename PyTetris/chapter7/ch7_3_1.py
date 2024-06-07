# もう作っていたら飛ばして大丈夫です
N = 0
E = 1
S = 2
W = 3

# OBlockの下あたりに書いてみましょう
# TBlockのクラスを作ります
# もうクラスの作り方は覚えましたでしょうか
"""この行を消して書いてみてください"""

    """ 省略 rotate関数の下ぐらいに書いてください """

    # OBlockと名前を同じにしないといけないので気をつけてください。
    # 左に動けるか判定する関数を作ります
    def """左に動けるか判定する関数"""(self, cursor, board_data):
        if """方角がNの時""":
            # 左に1マスは必要なので、左端1マス前にいる時は動けません
            if cursor.x == 1:
                return False
            
            # 左に1マス動いた時に壁に当たるか判定します
            # 本体ブロックは左に一つあるので、左に2つ目が壁かどうかを見ます
            if board_data[cursor.y][cursor.x - 2] != BLACK:
                return False
            # 下のマスも壁に当たるか判定します
            if board_data[cursor.y + 1][cursor.x - 1] != BLACK:
                return False
            return True
        elif """方角がEの時""":
            # ここも同じように考えてください
            # 方角がEということは-|の形になっています
            """この行を消して書いてみてください"""
        """方角がSの時とWの時も書いてみてください"""
    def """右に動けるか判定する関数"""(self, cursor, board_data):
        """左に動けるか判定する関数を参考に書いてみましょう"""

    def """下に動けるか判定する関数"""(self, cursor, board_data):
        """左に動けるか判定する関数を参考に書いてみましょう"""

    def """上に動けるか判定する関数"""(self, cursor, board_data):
        """左に動けるか判定する関数を参考に書いてみましょう"""