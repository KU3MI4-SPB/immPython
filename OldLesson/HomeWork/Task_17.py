import random


def generate_boards():
    successful_boards = []

    def is_valid_board(board):
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                if board[i][0] == board[j][0] or board[i][1] == board[j][1] or abs(board[i][0] - board[j][0]) == abs(
                        board[i][1] - board[j][1]):
                    return False
        return True

    while len(successful_boards) < 4:
        board = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if is_valid_board(board):
            successful_boards.append(board)

    return successful_boards


board_list = generate_boards()

print(generate_boards())
