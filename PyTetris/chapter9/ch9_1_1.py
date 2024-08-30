def main():
    """省略"""

    # chapter 9 ブロックを落とす
    # ループ回数を数える変数を追加
    # 時間にかかわるものの名前はtimerになることが多いですね
    timer = 0

    while True:
        # timerを1増やします
        """この行を消して書いてみてください"""

        # Draw the board
        board.draw(screen)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            board.cursor_move_left()
            pygame.time.wait(100)
        if keys[pygame.K_RIGHT]:
            board.cursor_move_right()
            pygame.time.wait(100)
        if keys[pygame.K_DOWN]:
            board.cursor_move_down()
            pygame.time.wait(100)
        
        # chapter 9 ブロックを落とす
        # 一定時間ごとに下に動かします
        # もし、timerが60になったら下に動かし、リセットもします
        if timer == 60:
            board.cursor_move_down()
            timer = 0

        """あとは同じです"""
        # Update the display
        pygame.display.update()

        # Tick
        # 今回whileループが1秒に60回回るようにしています
        clock.tick(60)

if __name__ == "__main__":
    main()