import os
player1_name = input("プレイヤー1の名前を入力してください: ")
player2_name = input("プレイヤー2の名前を入力してください: ")

words = []

# 最初に単語を入力するのはplayer1
words.append(input(f"{player1_name}は最初の単語を入力してください: "))

# 最初に答えるのはplayer2
player = player2_name
while True:
    for i in range(len(words)):
        data = input(f"{player}は{i+1}番目の単語を入力してください: ")
        if data != words[i]:
            print(f"{player}の負けです")
            # 終了
            exit()
        else:
            print("正解です, つづけてください")
    # 出力を消す
    os.system("clear")
    print("ターンクリア、新しく単語を入力してください")
    words.append(input(f"{player}は新しく覚える単語を入力してください: "))
    
    # プレイヤーを交代する
    if player == player1_name:
        player = player2_name
    else:
        player = player1_name