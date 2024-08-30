
def main():
    """省略"""
    # chapter 10 
    # ブロックを生成する処理
        if timer == 60:
            # board.cursor_move_down()から変更
            # 下に動かすだけでなく、動けない場合は新しいブロックを生成するようになります
            board.update()
            timer = 0
        # Update the display
        pygame.display.update()

        # Tick
        clock.tick(60)

if __name__ == "__main__":
    main()