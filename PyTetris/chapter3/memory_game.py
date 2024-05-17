import os

class Player:
    def __init__(self):
        self.name = input("プレイヤーの名前を入力してください: ")

class MemoryGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.words = []

        # ゲームオーバーかどうか
        self.game_over = False

        # 最初に単語を入力するのはplayer1
        self.words.append(input(f"{self.player1.name}は最初の単語を入力してください: "))

        # 最初に答えるのはplayer2
        self.current_player = self.player2 # current = 現在の
    
    def play(self):
        for word in self.words:
            data = input(f"{self.current_player.name}は単語を入力してください: ")
            if data != word:
                print(f"{self.current_player.name}の負けです")
                self.game_over = True
                return
            else:
                print("正解です, つづけてください")
        # 出力を消す
        os.system("clear")
        print("ターンクリア、新しく単語を入力してください")
        self.words.append(input(f"{self.current_player.name}は新しく覚える単語を入力してください: "))

        # プレイヤーを交代する
        if self.current_player.name == self.player1.name:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

player1 = Player()
player2 = Player()
game = MemoryGame(player1, player2)
while True:
    game.play()
    if game.game_over:
        break

