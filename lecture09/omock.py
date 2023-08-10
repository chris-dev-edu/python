# 오목 보드 생성
board_size = 15
board = [["." for _ in range(board_size)] for _ in range(board_size)]


def print_board():
    print("   ", end="")
    for col in range(board_size):
        print(f"{col:2d}", end=" ")
    print()

    for row in range(board_size):
        print(f"{row:2d}", end=" ")
        for col in range(board_size):
            print(f"{board[row][col]:>2s}", end=" ")
        print()
    print()


def check_win(row, col, player):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 가로, 세로, 대각선 방향
    for dr, dc in directions:
        count = 1
        r, c = row + dr, col + dc
        while 0 <= r < board_size and 0 <= c < board_size and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        r, c = row - dr, col - dc
        while 0 <= r < board_size and 0 <= c < board_size and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        if count >= 5:
            return True
    return False


def play():
    player = "X"
    turns = 0

    print("오목 게임을 시작합니다!")
    print_board()

    while True:
        row = int(input(f"{player} 플레이어, 행 번호를 입력하세요 (0부터 {board_size - 1}): "))
        col = int(input(f"{player} 플레이어, 열 번호를 입력하세요 (0부터 {board_size - 1}): "))

        if board[row][col] == ".":
            board[row][col] = player
            print_board()

            if check_win(row, col, player):
                print(f"{player} 플레이어가 이겼습니다!")
                break

            turns += 1
            if turns == board_size * board_size:
                print("무승부입니다!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("이미 돌이 놓여있는 자리입니다. 다시 선택하세요.")


if __name__ == "__main__":
    play()