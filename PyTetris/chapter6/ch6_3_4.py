class Board:
    def __init__(self, tile_size):
        # 作る時にタイルサイズを指定する
        self.board = [[BLACK for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.TILE_SIZE = tile_size

        # Cursor
        self.cursor = Cursor()

        # chapter6 ブロックを動かす
        # 新たにmoving_blockという変数を追加します
        # 最初は何も動かしていないのでNoneを入れておきます
        # わからない時は3.3.1を見てみましょう
        """この行を消して書いてみてください"""

    def draw(self, screen):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pygame.draw.rect(screen, self.board[y][x], (x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))

        # Draw the cursor
        for y in range(HEIGHT):
            if self.board[y][self.cursor.x] == BLACK:
                pygame.draw.rect(screen, CURSOR_COLOR, (self.cursor.x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
    
        # chapter6 ブロックを動かす
        # ブロックを動かす処理を追加します
        # 動かすブロックがNoneではない時
        if """何が入るでしょうか""":
            # ブロックの情報を取得します
            # 座標がリストになって帰ってくるはずなので変数に入れておきます
            """この行を消して書いてみてください"""

            # 何色で塗るかはBlockのcolorという変数に入っています
            # 一旦変数にコピーしておきます
            """この行を消して書いてみてください"""

            # ブロックからもらった座標リストを一つずつ見ていきます
            # リストを一つずつ見ていくループはfor文を使います
            for """好きな変数の名前""" in """もらった座標リストを入れた変数""":
                # for文で決めた変数に座標が一つずつ入ってループされます
                # それぞれの座標の場所を塗ることが目標です

                # その0番目にx座標が入っているのでそれをxに入れます
                # 1番目にy座標が入っているのでそれをyに入れます
                x = """変数の名前"""[0]
                y = """変数の名前"""[1]
                
                # マスを塗りつぶします。この行はわからなくて大丈夫ですが
                # 色を入れた変数の名前を置き換えてください
                pygame.draw.rect(screen, """34行目の色の変数の名前""", (x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))

        # あとは前回と同じです
        # 順番を間違えるとブロックが線を上書きして表示されてしまうので
        # この順番です。書き足す位置を間違えないように気をつけてください
        # Draw the grid
        for y in range(HEIGHT):
            pygame.draw.line(screen, GRAY, (0, y * self.TILE_SIZE), (WIDTH * self.TILE_SIZE, y * self.TILE_SIZE))
        for x in range(WIDTH):
            pygame.draw.line(screen, GRAY, (x * self.TILE_SIZE, 0), (x * self.TILE_SIZE, HEIGHT * self.TILE_SIZE))

    def window_size(self):
        return (WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE)
    
    # chapter6 ブロックを動かす
    # cursorの動く機能をカプセル化します
    # cursor_move_leftという関数を追加します
    def cursor_move_left(self):
        # cursorのmove_left関数を呼び出します
        # 引数にはmoving_blockとboardを渡します
        self.cursor.move_left(self.moving_block, self.board)
    
    # 残りの動きも同じようにします