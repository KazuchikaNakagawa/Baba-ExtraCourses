class Board:
    """省略"""
    def erase_lines(self):
        # for文を使って、yを0からHEIGHT-1まで変化させる
        # (リストの高速列挙を利用すると行数がわからなくなるためrangeの使用を推奨します)
        for y in ...:
            # y行目が揃っているか調べる
            if ...:
                # y行目を消す
                ...
                # self.boardの先頭に[0,0,...,0](10個)を挿入して一行ずつ減らす。
                ...
