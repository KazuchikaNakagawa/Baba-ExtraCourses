# もう作っていたら飛ばして大丈夫です
N = 0
E = 1
S = 2
W = 3

# OBlockの下あたりに書いてみましょう
# TBlockのクラスを作ります
# もうクラスの作り方は覚えましたでしょうか
"""この行を消して書いてみてください"""

    # クラスが作られた時に呼ばれる関数を作ります
    # 3.3.1を見ながら作ってみましょう
    """クラスが作られた時に呼ばれる関数"""
        # 色を決めます
        # クラス内にcolorという変数を作って
        # 色を入れておきます
        # 色はネットで調べて入れてみましょう
        """この行を消して書いてみてください"""

        # 最初の方角を設定します
        # クラスの中にrotationという変数を作って、
        # 最初は北向きの変数を入れます
        # ここで言う2行目で作ったやつです
        """方角を設定する行"""

    # ブロックの情報を計算して返す関数を作ります
    # OBlockと同様、表示されている位置が
    # 必要なので、cursorを引数に入れます
    def """ブロックの情報を計算して返す関数"""(self, cursor):
        # 最初はどうなるかわからないので[]を入れておきます
        # 後から座標を入れて、最後に返すようにします
        # 普通の変数resultに[]を入れましょう
        """この行を消して書いてみてください"""

        # カーソルの座標を取得します
        # カーソルの座標はcursor.xとcursor.yで取得できます
        # それを変数に入れておきます
        x = """上に書いた通り"""
        y = """上に書いた通り"""

        # ここからはTBlockの座標計算です
        # 自分の向きを見ます
        # もし北向きだったら
        if self.rotation == N:
            # 4つの座標を計算します
            # まずは中心の座標です
            # これはカーソルの座標そのままです
            # 座標は(x座標, y座標)の形でリストに入れます
            """34行目くらいに作った変数名""".append((x, y))

            # 次に上の座標です
            # これは中心の座標から上に1つ進んだ座標です
            """34行目くらいに作った変数名""".append((x, y - 1))

            # 次に左の座標です
            # これは中心の座標から左に1つ進んだ座標です
            """34行目くらいに作った変数名""".append((x - 1, y))

            # 次に右の座標です
            # これは中心の座標から右に1つ進んだ座標です
            """34行目くらいに作った変数名""".append((x + 1, y))
        # もし東向きだったら
        elif """ここを書いてみてください""":
            # 4つの座標を計算します
            # まずは中心の座標です
            # これはカーソルの座標そのままです
            # 座標は(x座標, y座標)の形でリストに入れます
            """34行目くらいに作った変数名""".append((x, y))

            # 次に上の座標です
            # これは中心の座標から上に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に下の座標です
            # これは中心の座標から下に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に左の座標です
            # これは中心の座標から左に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")
        # もし南向きだったら
        elif """ここを書いてみてください""":
            # 4つの座標を計算します
            # まずは中心の座標です
            # これはカーソルの座標そのままです
            # 座標は(x座標, y座標)の形でリストに入れます
            """34行目くらいに作った変数名""".append((x, y))

            # 次に上の座標です
            # これは中心の座標から上に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に左の座標です
            # これは中心の座標から左に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に右の座標です
            # これは中心の座標から右に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

        # もし西向きだったら
        elif """ここを書いてみてください""":
            # 4つの座標を計算します
            # まずは中心の座標です
            # これはカーソルの座標そのままです
            # 座標は(x座標, y座標)の形でリストに入れます
            """34行目くらいに作った変数名""".append((x, y))

            # 次に上の座標です
            # これは中心の座標から上に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に下の座標です
            # これは中心の座標から下に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

            # 次に右の座標です
            # これは中心の座標から右に1つ進んだ座標です
            """34行目くらいに作った変数名""".append("""ここを書いてみてください""")

        # 方角がなんであっても
        # 34行目くらいに作った変数には4つの座標が入っています
        # それを返します
        return """34行目くらいに作った変数名"""

    # クラスの中に回転する関数を作ってみます
    # 関数名はrotateとします
    def """回転する関数"""(self):
        # 方角を変えます
        # 方角はN, E, S, Wの順番で変えていきます
        # 一番最後にWになったらNに戻します
        # 描画も更新しないといけないような気がしますが、
        # 方角さえ変えてしまえば次にblock_infoが呼ばれる時に
        # 描画が変わるので大丈夫です
        """方角を変える行"""
